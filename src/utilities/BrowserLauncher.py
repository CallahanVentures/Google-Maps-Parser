import asyncio
from pyppeteer import launch

class BrowserLauncher:
    @staticmethod
    async def initialize_browser():
        browser = await launch(headless=True)
        page = await browser.newPage()
        return browser, page
