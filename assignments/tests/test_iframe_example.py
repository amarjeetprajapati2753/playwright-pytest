from playwright.sync_api import expect

def test_iframe_text(page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    page.locator("div[aria-label='Close']").click()
    frame = page.frame_locator("#mce_0_ifr")


    editor = frame.locator("#tinymce")

    editor.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    editor.type("I rule the frames!")

    expect(editor).to_have_text("Your content goes here.")
