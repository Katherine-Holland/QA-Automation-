from playwright.sync_api import sync_playwright, expect
from utils.helpers import dismiss_netflix_popups

def run_tests():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context()
        page = context.new_page()
        context.set_default_timeout(20000)

        # === TEST 1: Invalid Email ===
        # ARRANGE
        page.goto("https://netflix.com")
        dismiss_netflix_popups(page)
        page.locator('a[href="/login"]').click()

        # ACT
        page.locator('input[name="userLoginId"]').fill("invalidemail@email.com")
        page.locator('input[name="password"]').fill("invalidpassword")
        page.locator('[data-uia="sign-in-button"][role="button"]').click()

        # ASSERT
        try:
            expect(page.get_by_text("Incorrect password for")).to_be_visible()
            results.append(("❌ Invalid Email / Password", "✅ PASS"))
        except:
            results.append(("❌ Invalid Email / Password", "❌ FAIL"))

        # === TEST 2: Toggle Eye Icon Visibility ===
        # ARRANGE
        page.goto("https://netflix.com")
        dismiss_netflix_popups(page)
        page.locator('a[href="/login"]').click()
        page.locator('[name="password"][data-uia="field-password"]').fill("mypassword")

        # ACT & ASSERT
        try:
            page.locator('[data-uia="icon-button"]').click()
            revealed_value = page.locator('[name="password"][data-uia="field-password"]').input_value()
            if revealed_value == "mypassword":
                results.append(("👁️ Toggle Eye Icon Visibility", "✅ PASS"))
            else:
                results.append(("👁️ Toggle Eye Icon Visibility", "❌ FAIL (not revealed)"))
        except:
            results.append(("👁️ Toggle Eye Icon Visibility", "❌ FAIL (exception)"))

        browser.close()
    return results
