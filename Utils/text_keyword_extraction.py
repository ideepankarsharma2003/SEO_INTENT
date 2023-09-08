from Utils.client import generate_top_urls
from Utils.basic_cleaner import clean
import spacy
import spacy_transformers

# nlp = spacy.load('en_core_web_trf')
nlp = spacy.load('en_core_web_sm')


import pytextrank
nlp.add_pipe("textrank")

def generate_keyword_list(keyword, num_queries=10):
    top_10_urls= generate_top_urls(keyword, 10)
    cleaned_text= ""
    for i in top_10_urls[:9]:
        print(i)
        cleaned_text_i= clean(i)
        # print(cleaned_text)
        # if cleaned_text_i:
        cleaned_text+=cleaned_text_i+''
        
        print('**'*30)
    cleaned_text= (cleaned_text).lower()
    doc = nlp(cleaned_text)
    
    print(f"Number of characters: {len(doc)}")
    # try:
        # doc = nlp(cleaned_text)
    # except: 
        # return f"Token Size exceeded ,try setting num_queries < {num_queries}"
    
    keyword_list= []
    for phrase in doc._.phrases[:200]:
        keyword_list.append(f"{phrase.text}, rank={phrase.rank}, #count={phrase.count}\n")
    return keyword_list

def generate_keyword_list_v2(url_list, num_queries=10):
    # top_10_urls= generate_top_urls(keyword, 10)
    cleaned_text= ""
    retrieved_url= []
    for i in url_list:
        print(i)
        cleaned_text_i= clean(i)
        # print(cleaned_text)
        if cleaned_text_i!='':
            retrieved_url.append(i)
        cleaned_text+=cleaned_text_i+'\n'
        
        print('**'*30)
    cleaned_text= (cleaned_text).lower()
    doc = nlp(cleaned_text)
    
    print(f"Number of characters: {len(doc)}")
    # try:
        # doc = nlp(cleaned_text)
    # except: 
        # return f"Token Size exceeded ,try setting num_queries < {num_queries}"
    
    keyword_list= []
    for phrase in doc._.phrases[:200]:
        keyword_list.append(f"{phrase.text}, rank={phrase.rank}, #count={phrase.count}")
    return (keyword_list, retrieved_url)
    
    
    
    
print("so far so good")