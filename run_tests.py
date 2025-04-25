from playwright.sync_api import sync_playwright, expect

def run_tests():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context()
        page = context.new_page()
        context.set_default_timeout(10000)

        # ARRANGE
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_selector('input[name="username"]')

        # TEST 1: Invalid login
        try:
            page.fill('input[name="username"]', 'invalid_user')
            page.fill('input[name="password"]', 'wrong_password')
            page.click('button[type="submit"]')
            expect(page.locator(".oxd-alert-content-text")).to_have_text("Invalid credentials")
            results.append(("Invalid Login Test", True))
        except Exception:
            results.append(("Invalid Login Test", False))

        # TEST 2: Valid login
        try:
            page.fill('input[name="username"]', 'Admin')
            page.fill('input[name="password"]', 'admin123')
            page.click('button[type="submit"]')
            page.wait_for_selector('h6.oxd-topbar-header-breadcrumb-module')
            expect(page.locator('h6.oxd-topbar-header-breadcrumb-module')).to_have_text("Dashboard")
            results.append(("Valid Login Test", True))
        except Exception:
            results.append(("Valid Login Test", False))

        browser.close()
    return results
