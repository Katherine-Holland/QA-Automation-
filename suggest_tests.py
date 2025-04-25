import requests
from bs4 import BeautifulSoup

def suggest_tests(url):
    suggestions = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    forms = soup.find_all('form')
    buttons = soup.find_all('button')
    inputs = soup.find_all('input')

    # Suggest form-related test
    if forms:
        suggestions.append((
            "✅ Form detected – Suggest testing valid and invalid form submissions.",
            "# Example: await page.fill('input[name=\"example\"]', 'test')\n# await page.click('button[type=\"submit\"]')"
        ))

    # Suggest input field validations
    for input_field in inputs:
        name = input_field.get('name') or input_field.get('id') or 'unknown'
        input_type = input_field.get('type', 'text')
        if input_type in ['email', 'password', 'text']:
            suggestions.append((
                f"📌 Validate input field '{name}' (type: {input_type}).",
                f"# Example: await page.fill('input[name=\"{name}\"]', 'test input')"
            ))

    # Suggest button click tests
    for btn in buttons:
        label = btn.text.strip() or btn.get('aria-label') or 'Unnamed Button'
        suggestions.append((
            f"🧪 Test clicking button '{label}'.",
            f"# Example: await page.get_by_role('button', name='{label}').click()"
        ))

    # Starter Playwright template
    suggestions.append((
        "📜 Starter Playwright Test Template",
        f'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("{url}")
    # 👉 Add actions/assertions below
    browser.close()
'''
    ))

    return suggestions