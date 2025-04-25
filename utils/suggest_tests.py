import requests
from bs4 import BeautifulSoup

def suggest_tests(url):
    suggestions = []
    generated_test_code = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    forms = soup.find_all('form')
    inputs = soup.find_all('input')
    buttons = soup.find_all('button')
    links = soup.find_all('a')
    headings = soup.find_all(['h1', 'h2', 'h3'])

    # --- Suggest tests ---
    if forms:
        suggestions.append("✅ Form detected – Suggest testing valid and invalid form submissions.")

    for input_field in inputs:
        name = input_field.get('name') or input_field.get('id') or 'unknown'
        input_type = input_field.get('type', 'text')
        if input_type in ['email', 'password', 'text']:
            suggestions.append(f"📌 Input field '{name}' (type: {input_type}) – Suggest input validation test.")
            generated_test_code.append(f"""# Arrange
page.fill('[name="{name}"]', 'test input')

# Act
# (Submit form or proceed)

# Assert
# (Check for success/failure message)
""")

    for btn in buttons:
        label = btn.text.strip() or btn.get('aria-label') or 'Unnamed Button'
        if label != 'Unnamed Button':
            suggestions.append(f"🧪 Button '{label}' – Suggest click test.")
            generated_test_code.append(f"""# Arrange

# Act
page.get_by_role("button", name="{label}").click()

# Assert
# (Check page navigated or success message appeared)
""")

    for link in links:
        href = link.get('href')
        if href and not href.startswith('#'):
            text = link.text.strip()
            if text:
                suggestions.append(f"🔗 Link '{text}' – Suggest navigation test.")
                generated_test_code.append(f"""# Arrange

# Act
page.get_by_role("link", name="{text}").click()

# Assert
# (Check URL or page title)
""")

    for heading in headings:
        level = heading.name
        text = heading.text.strip()
        if text:
            suggestions.append(f"📝 Heading ({level}): '{text}' – Suggest content visibility test.")
            generated_test_code.append(f"""# Arrange

# Act

# Assert
page.get_by_role("heading", name="{text}").is_visible()
""")

    # --- Sample Playwright starter ---
    starter = f"""
# Example Playwright script
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("{url}")

    # --- Suggested Actions ---
""" + "\n".join(generated_test_code) + """

    browser.close()
"""

    return suggestions, starter
