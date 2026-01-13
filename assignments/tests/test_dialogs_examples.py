from playwright.sync_api import expect

def test_js_alert(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # Handle alert
    page.on("dialog", lambda dialog: dialog.accept())

    page.click("button:text('Click for JS Alert')")

    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")


def test_js_confirm_dismiss(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.dismiss())

    page.click("button:text('Click for JS Confirm')")

    expect(page.locator("#result")).to_have_text("You clicked: Cancel")


def test_js_prompt_accept(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_prompt(dialog):
        dialog.accept("Playwright Hero")

    page.on("dialog", handle_prompt)

    page.click("button:text('Click for JS Prompt')")

    expect(page.locator("#result")).to_have_text("You entered: Playwright Hero")
