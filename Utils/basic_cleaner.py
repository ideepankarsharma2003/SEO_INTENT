import requests
from bs4 import BeautifulSoup


def clean(url, tries=0):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unnecessary elements (styles, scripts, etc.)
        for script in soup(['script', 'style', 'a', 'img', 'video']):
            script.extract()
        
        cleaned_text = soup.get_text()
        cleaned_text= cleaned_text.strip()
        cleaned_text= cleaned_text.replace('\n', ' ')
        cleaned_text= cleaned_text.replace('\t', ' ')
        
        return cleaned_text.replace('    ', '')
            
    else:
        print ("Failed to retrieve the webpage: ", url)
        if tries==3:
            return ''
        print("Retrying over scrapper....")
        return clean("http://api.scraperapi.com?api_key=f86bd0a9f5e74a8b616c494a7682f4d2&url="+url, tries+1)


