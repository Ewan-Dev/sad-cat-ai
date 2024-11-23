from playwright.sync_api import sync_playwright
def upload(file_path, name, username, password, channel_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=5, args=["--disable-blink-features=AutomationControlled"])
        page = browser.new_page()
        page.goto(channel_url)
        page.fill("input#identifierId", username)
        page.click("button:has-text('Next')")
        page.wait_for_selector("input[name='Passwd']")
        page.fill("input[name='Passwd']", password) 
        page.click("button:has-text('Next')")
        page.wait_for_selector("a.item.style-scope.ytcp-quick-actions")
        page.click("a.item.style-scope.ytcp-quick-actions")
        page.set_input_files("input[name='Filedata']", file_path)
        page.wait_for_selector("div#textbox[contenteditable='true']")
        page.fill("div#textbox[contenteditable='true']", name)
        page.click("ytcp-button#toggle-button")
        page.wait_for_selector("ytcp-checkbox-lit#notify-subscribers")
        page.click("ytcp-checkbox-lit#notify-subscribers")
        page.click("ytcp-checkbox-lit#has-autoplaces-mentioned-checkbox")
        for i in range(3):
            page.wait_for_selector("ytcp-button#next-button")
            page.click("ytcp-button#next-button")
        page.wait_for_selector("tp-yt-paper-radio-button[name='PRIVATE']")
        page.click("tp-yt-paper-radio-button[name='PRIVATE']")
        page.click("tp-yt-paper-radio-button[name='PUBLIC']")
        page.click("ytcp-button#done-button")
        page.wait_for_selector("ytcp-button#close-button")
        page.click("ytcp-button#close-button")
        browser.close()
        print("uploaded")  