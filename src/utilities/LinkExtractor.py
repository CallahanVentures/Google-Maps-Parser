from utilities.BrowserScripts import parseBusinessLinksScript
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LinkExtractor:
    @staticmethod
    def extract_links_from_queries(driver, queries):
        extracted_links = []
        for query in queries:
            print(f"\nEntering Query Provided: '{query}'")
            driver.get("https://www.google.com/maps/place/")
            driver.find_element(By.ID, "searchboxinput").send_keys(query)
            driver.find_element(By.ID, "searchboxinput").send_keys(Keys.ENTER)
            print("Submitted, Waiting For Results, Please Wait 5 Seconds.")
            time.sleep(5)
            print("Finding Scroll Wheel Element")
            xpath_element = '//div[contains(@aria-label, "Results for")]'
            fBody = driver.find_element(By.XPATH, xpath_element)
            scroll = 0
            if fBody:
                print("Scroll Wheel Element Found, Scrolling Through Results.")
            else:
                print("Error Finding Scroll Wheel Element, Please Check Lines 75-95 In parseLinksFromGMaps.py")
            while scroll < 20:
                try:  
                    fBody.send_keys(Keys.PAGE_DOWN)
                    scroll += 1
                    time.sleep(1)
                except Exception as e:
                    print("Scroll Wheel Element Raised An Error:")
                    print(e)
            print("Scrolling Finished, Extracting Google Maps Links.")
            links = driver.execute_script(parseBusinessLinksScript)
            if links:
                extracted_links.extend(links)
                print(f"\n{len(links)} Links Extracted For Query: '{query}'\n")
            else:
                print(f"Failed To Extract Links For Query: '{query}'\n")
        return extracted_links
