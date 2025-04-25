from playwright.sync_api import sync_playwright, expect

def run_tests():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        context.set_default_timeout(5000)

        # ARRANGE: Go to Netflix and go to login
        page.goto("https://netflix.com")
        page.locator('a[href="/login"]').click()

        # ACT 1: Invalid Email Test
        page.locator('input[name="userLoginId"]').fill("invalidemail@email.com")
        page.locator('input[name="password"]').fill("invalidpassword")
        page.locator('[data-uia="sign-in-button"][role="button"]').click()

        try:
            expect(page.get_by_text("Incorrect password for")).to_be_visible()
            results.append(("Invalid Email Test", "✅ PASS"))
        except:
            results.append(("Invalid Email Test", "❌ FAIL"))

        # ACT 2: Toggle Eye Icon Test
        page.goto("https://netflix.com")
        page.locator('a[href="/login"]').click()
        page.locator('[name="password"][data-uia="field-password"]').fill("mypassword")

        try:
            page.locator('[data-uia="icon-button"]').click()
            revealed_value = page.locator('[name="password"][data-uia="field-password"]').input_value()
            if revealed_value == "mypassword":
                results.append(("Toggle Eye Icon Visibility Test", "✅ PASS"))
            else:
                results.append(("Toggle Eye Icon Visibility Test", "❌ FAIL (not visible)"))
        except:
            results.append(("Toggle Eye Icon Visibility Test", "❌ FAIL (exception)"))

        browser.close()
    return results
