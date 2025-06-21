from playwright.sync_api import sync_playwright
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wwwgoogle.com")

    browser.close()