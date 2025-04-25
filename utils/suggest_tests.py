# utils/suggest_tests.py

import requests
from bs4 import BeautifulSoup

def suggest_tests(url):
    sections = {
        "Forms": [],
        "Inputs": [],
        "Buttons": [],
        "Navigation Links": []
    }

    if not url.startswith("http"):
        url = "https://" + url

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Detect forms
    if soup.find('form'):
        sections["Forms"].append((
            "Form detected",
            "Test valid and invalid form submissions.",
            '''# Example: Form submission test
page.fill('input[name="email"]', 'test@example.com')
page.fill('input[name="password"]', 'wrongpassword')
page.click('button[type="submit"]')
assert page.url != "YOUR_LOGIN_PAGE", "Form submission failed as expected."
'''
        ))

    # Inputs
    for input_tag in soup.find_all('input'):
        name = input_tag.get('name') or input_tag.get('id') or 'unnamed'
        itype = input_tag.get('type', 'text')
        if itype in ['email', 'password', 'text']:
            sections["Inputs"].append((
                f"Test input field '{name}'",
                f"Validate {itype} input handling.",
                f'''# Example: Validate input field '{name}'
page.fill('input[name="{name}"]', 'test input') 
assert page.get_attribute('input[name="{name}"]', 'value') == 'test input'
'''
            ))

    # Buttons
    for button in soup.find_all('button'):
        label = button.text.strip() or button.get('aria-label') or 'Unnamed Button'
        sections["Buttons"].append((
            f"Click button '{label}'",
            f"Ensure button '{label}' performs expected action.",
            f'''# Example: Click button '{label}'
page.click('button:has-text("{label}")')
'''
        ))

    # Navigation Links
    for link in soup.find_all('a', href=True):
        if link.text.strip():
            sections["Navigation Links"].append((
                f"Test navigation link '{link.text.strip()}'",
                f"Click link and verify page change.",
                f'''# Example: Test link '{link.text.strip()}'
page.click('text="{link.text.strip()}"')
assert page.url != "{url}", "Navigation did not happen."
'''
            ))

    # Sample starter script
    sample_test = f'''
# 🧪 Example starter test for {url}
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # ARRANGE
    page.goto("{url}")

    # ACT
    page.click('text="Get Started"')  # Adjust this selector if needed

    # ASSERT
    assert page.url != "{url}", "Page did not navigate!"

    browser.close()
'''

    return sections, sample_test