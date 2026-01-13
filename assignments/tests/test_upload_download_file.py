
import os
from playwright.sync_api import Page, expect

def test_fileUploadDownload(page: Page):
    page.goto("https://demoqa.com/upload-download")

    file_path = "C:/Users/unthinkable-lap/Downloads/test_doc.pdf"
    page.set_input_files("#uploadFile", file_path)

    expect(page.get_by_text("test_doc.pdf")).to_be_visible()

    os.makedirs("downloads", exist_ok=True)

    with page.expect_download() as download_info:
        page.locator("#downloadButton").click()

    download = download_info.value
    download_path = "downloads/test_download.pdf"
    download.save_as(download_path)

    assert os.path.exists(download_path)
