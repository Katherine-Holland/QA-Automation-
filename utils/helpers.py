from playwright.sync_api import Page

def dismiss_netflix_popups(page: Page):
    try:
        # Try to click the "Accept" or "Reject" cookie banner if visible
        if page.locator('#onetrust-accept-btn-handler').is_visible():
            page.locator('#onetrust-accept-btn-handler').click()
        elif page.locator('#onetrust-reject-all-handler').is_visible():
            page.locator('#onetrust-reject-all-handler').click()
    except Exception as e:
        print(f"⚠️ Popup dismissal failed or skipped: {e}")
