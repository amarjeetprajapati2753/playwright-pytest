from playwright.sync_api import expect

def test_end_to_end_interactions(page):
    # Dialog
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda d: d.accept("Playwright Hero"))
    page.click("button:text('Click for JS Prompt')")
    expect(page.locator("#result")).to_contain_text("Playwright Hero")

    # Mouse
    page.goto("https://demoqa.com/buttons")
    page.dblclick("#doubleClickBtn")
    expect(page.locator("#doubleClickMessage")).to_be_visible()


    # Frame
    page.goto("https://the-internet.herokuapp.com/iframe")
    page.locator("div[aria-label='Close']").click()
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")

    editor.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    editor.type("Your content goes here.")
    expect(editor).to_have_text("Your content goes here.")
