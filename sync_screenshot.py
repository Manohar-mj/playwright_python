from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://placementdriveinsta.in/")
    page.screenshot(path="demo.png")
    browser.close()

