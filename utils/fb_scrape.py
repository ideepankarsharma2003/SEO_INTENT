import os
import re
import requests
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio


# Scrapping Facebook
PATH = "research/edge drivers/msedgedriver"
print(
    os.path.exists(PATH)
)
reg1= '"mime_type":"audio\\\\/mp4","codecs":"[^"]+","base_url":"[^"]+'
reg2= '"mime_type":"audio\\\\/mp4","codecs":"[^"]+","base_url":"'
def extract_url_from_source(html_content: str):
    base_url= ""
    print(type(html_content))
    # soup= BeautifulSoup(html_content, "html.parser")
    # for script in soup.body.find_all("script"):
        # contents= script.contents
    contents= [html_content]
    if True:
        if len(contents)>0:
            reg1_test= re.search(reg1, contents[0])
            if reg1_test:
                base_url_match= contents[0][reg1_test.start():reg1_test.end()]
                url= re.search(reg2, base_url_match)
                base_url= base_url_match[url.end():].replace('\\','')
                print(f"base url: {base_url}")
                return base_url
    else:
        print("[No base_url for given url]")
        return None
    
    
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    # "cookie": f'sessionid={SESSIONID};'
}


def extract_fbvideo_from_url(url:str):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True, channel="msedge")
    page = browser.new_page()
    page.goto(url)
    page_source = page.content()
    base_url = extract_url_from_source(page_source)
    return base_url




























