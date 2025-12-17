from playwright.sync_api import expect


def test_example_domain_page(page,setup):
    # Task 3: Open browser & navigate
    page.goto("https://example.com")

    # Verify page title
    expect(page).to_have_title("Example Domain")

    # Verify page contains text "Example Domain"
    expect(page.locator("h1")).to_have_text("Example Domain")

    # Task 4: Verify full paragraph text
    expect(page.locator("body")).to_contain_text(
        "This domain is for use in documentation examples without needing permission."
    )

    # Task 5: Negative scenario – incorrect title should NOT match
    actual_title = page.title()
    assert actual_title != "Wrong Page Title"
