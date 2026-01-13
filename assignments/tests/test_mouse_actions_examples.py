from playwright.sync_api import expect

def test_double_click(page):
    page.goto("https://demoqa.com/buttons")

    page.dblclick("#doubleClickBtn")

    expect(page.locator("#doubleClickMessage")).to_be_visible()


def test_right_click(page):
    page.goto("https://demoqa.com/buttons")

    page.click("#rightClickBtn", button="right")

    expect(page.locator("#rightClickMessage")).to_be_visible()



def test_normal_click(page):
    page.goto("https://demoqa.com/buttons")

    page.get_by_text("Click Me", exact=True).click()


    expect(page.locator("#dynamicClickMessage")).to_be_visible()
