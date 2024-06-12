import asyncio
from pyppeteer.errors import NetworkError
from utilities.BrowserScripts import (parseBusinessAddressScript, parseBusinessNameScript, parseBusinessPhoneScript, parseBusinessWebsiteScript)

class DataExtractor:
    @staticmethod
    async def extract_data(page, url):
        business_data = []

        try:
            print(f"Parsing URL: {url}\n")

            await page.goto(url, {'waitUntil': 'domcontentloaded', 'timeout': 0})

            if not page.isClosed():
                await asyncio.sleep(1.3)
                business_name = await page.evaluate(parseBusinessNameScript)
                business_address = await page.evaluate(parseBusinessAddressScript)
                business_phone = await page.evaluate(parseBusinessPhoneScript)
                business_website_raw = await page.evaluate(parseBusinessWebsiteScript)

                try:
                    business_website = business_website_raw.replace("/url?q=", "").split('&opi=')[0]
                except:
                    business_website = "Not Found"

                business_data.append([business_name, business_address, business_phone, business_website])
            else:
                print(f"Couldn't get data for URL: {url}\n")

        except NetworkError:
            pass

        return business_data
