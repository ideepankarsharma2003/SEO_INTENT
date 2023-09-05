import requests
from bs4 import BeautifulSoup

# dict_tags= {
#     'title': 'title',
#     'p': 'text',
#     'link': 'link',
    
# }

class HTML_Tag_Extractor:
    def __init__(self) -> None:
        pass
    
    def generate_html_template(self, element):
        if element.name == 'script' or element.name =='style'or element.name =='noscript' :
            return
        # if element.name == 'p' or element.name == 'div' or element.name == 'td':
        #     self.s+=(f"<{element.name}>")
        #     self.s+=(f"</{element.name}>")
        #     return
        if element.name not in ['meta', 'link']:
            self.s+=(f"<{element.name}>")
        for child in element.children:
            if child.name:
                self.generate_html_template(child)
            elif child.strip() and element.name!='[document]':
                # self.s+=(child)
                self.s+= f'text'
                # self.s+= f'dummy_placeholder_text'
                # print("child= ", child)
        
        if element.name == 'script' or element.name =='style' or element.name =='meta' or element.name =='link' or element.name =='img'or element.name =='br'or element.name =='hr' or element.name =='input':
            return
                
        self.s+=(f"</{element.name}>")
        
    
    def extract_html_template(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.s= ''
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')
                # print(soup)
                self.generate_html_template(soup)
                # 
                return self.s.replace('\n', '')
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return ''
        
    
    def print_html_raw(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.s= ''
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')
                print(soup)
                # self.generate_html_template(soup)
                
                # return self.s.replace('\n', '')
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return ''
        
        
        
html_tag_extractor= HTML_Tag_Extractor()
        
        