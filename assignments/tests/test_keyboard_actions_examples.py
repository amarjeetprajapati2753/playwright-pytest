from playwright.sync_api import expect

def test_keyboard_form_interaction(page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.keyboard.type("Playwright User")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    page.keyboard.type("Keyboard Master")
    page.keyboard.press("Enter")

    expect(page.locator("h1")).to_have_text("Form submitted")
