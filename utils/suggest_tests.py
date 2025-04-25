import requests
from bs4 import BeautifulSoup

def suggest_tests(url):
    suggestions = []
    
    if not url.startswith("http"):
        url = "https://" + url

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Detect forms
    if soup.find('form'):
        suggestions.append(("Form detected", "Test valid and invalid form submissions."))

    # Inputs
    for input_tag in soup.find_all('input'):
        name = input_tag.get('name') or input_tag.get('id') or 'unnamed'
        itype = input_tag.get('type', 'text')
        if itype in ['email', 'password', 'text']:
            suggestions.append((f"Test input field '{name}'", f"Validate {itype} input handling."))

    # Buttons
    for button in soup.find_all('button'):
        label = button.text.strip() or button.get('aria-label') or 'Unnamed Button'
        suggestions.append((f"Click button '{label}'", f"Ensure button '{label}' performs expected action."))

    # Links
    for link in soup.find_all('a', href=True):
        if link.text.strip():
            suggestions.append((f"Test navigation link '{link.text.strip()}'", f"Click link and verify page change."))

    # Sample test code with ARRANGE / ACT / ASSERT
    sample_test = f'''
# 🧪 Example starter test for {url}
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # ARRANGE
    page.goto("{url}")

    # ACT
    page.click('text="Get Started"')  # Adjust this selector

    # ASSERT
    assert page.url != "{url}", "Page did not navigate!"

    browser.close()
'''

    return suggestions, sample_test
