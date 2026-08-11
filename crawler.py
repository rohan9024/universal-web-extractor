from playwright.sync_api import sync_playwright


def crawl_page(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        context = browser.new_context(
            ignore_https_errors=True
        )

        page = context.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=30000
        )

        page.wait_for_timeout(
            3000
        )

        html = page.content()

        browser.close()

        return html