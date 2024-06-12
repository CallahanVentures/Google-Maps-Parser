import ctypes
import warnings
import time
import asyncio

from utilities.QueryLoader import QueryLoader
from utilities.BackupManager import BackupManager
from utilities.BrowserManager import BrowserManager
from utilities.LinkExtractor import LinkExtractor
from utilities.FileWriter import FileWriter
from utilities.BrowserLauncher import BrowserLauncher
from utilities.DataExtractor import DataExtractor
from utilities.CSVWriter import CSVWriter
from utilities.LinkLoader import LinkLoader

# Part 1: Extracting Links Using Selenium
print("Welcome To The Google Maps Link Suite!\n")
ctypes.windll.kernel32.SetConsoleTitleW("Google Link Scraper")
warnings.filterwarnings('ignore')

print("Backing Up Last Session..")
BackupManager.backup_old_links_files()

print("Starting Parser Agent")
driver = BrowserManager.initialize_browser() 

print(f"Parsed Agent Started, Please Wait As It Loads")
queries = QueryLoader.load_queries()
extracted_links = LinkExtractor.extract_links_from_queries(driver, queries)

if extracted_links:
    print("Writing Links To File For Parsing.")
    if FileWriter.write_links_to_file("google_maps_links.txt", extracted_links):
        print("Please Wait 5 Seconds While The Link Parser Loads!")
        time.sleep(5)
        print("Loaded!")
        driver.quit()
    else:
        print("Failed To Write Links To File Writing To linksBackup/links_backup.txt, Please Copy This File Elsewhere Or It Will Be Overwritten!")
        if FileWriter.write_links_to_file("linksBackup/links_backup.txt", extracted_links):
            print("Links Written To Backup, Exiting.")
            exit()
        else:
            print("Failed To Write Links To Backup File, Exiting.")
            exit()
else:
    print("No Links Were Extracted Please Check Terminal For Any Errors, Then Try Again.")

# Part 2: Parsing Extracted Links Using Pyppeteer
ctypes.windll.kernel32.SetConsoleTitleW("Google Link Parser")
warnings.filterwarnings('ignore')

async def main(urls):
    browser, page = await BrowserLauncher.initialize_browser()
    business_data = []

    for url in urls:
        data = await DataExtractor.extract_data(page, url)
        business_data.extend(data)

    await browser.close()
    print("Finished")

    CSVWriter.write_to_csv(business_data)

links_file = "google_maps_links.txt"
urls = LinkLoader.load_links(links_file)

if urls:
    print(f'{len(urls)} URLs Loaded!')
    print(f'Estimated Parsing Time: {len(urls)*2} Seconds.')

    try:
        asyncio.get_event_loop().run_until_complete(main(urls))
    except Exception as e:
        print(f"Error during processing: {e}")
else:
    print("No URLs loaded. Exiting.")
