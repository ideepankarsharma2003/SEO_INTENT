import uvicorn
import sys
import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response, JSONResponse
from starlette.responses import RedirectResponse
# from main import (
#     # generate_base_embeddings, 
#     # generate_large_embeddings, 
#     # str_2_list_of_str, 
#     # generate_bge_large_embeddings,
#     # generate_e5_large_v2_embeddings,
#     generate_intent_v2  
#     )
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

from utils.get_keywords_utils import (
                                      generate_keywords_around_seed,
                                      generate_keywords_Ngram
                                      )

from pydantic import BaseModel

class KeyBertKeywords(BaseModel):
    seed_keyword:str= ""
    num_keywords: int= 50
    num_urls: int=10
    top_n: int= 7
    
class KeyBertKeywordsNGrams(BaseModel):
    keywords: list[str]= [""]
    num_keywords: int= 50
    top_n: int= 4

class Keyword(BaseModel):
    url_list: list

class Url(BaseModel):
    keyword: str=""
    num_urls: int=10
    keyword_list: list[str]= [""]

class Intent(BaseModel):
    keyword_list: list[str] or str= [""]


import json

from Utils.text_keyword_extraction import generate_keyword_list, generate_keyword_list_v2, generate_keyword_list_v3
from Utils.client import generate_top_urls
from Utils.get_intent_bert_basedANN import  get_intent_bulk
# from Utils.get_sentence_status import complete_sentence_analysis
# from Utils.bert_fine_tuned_intent import get_intent
# from main import generate_intent_v2





app= FastAPI()
print("initializing app")

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')
    # return "Hello world!"

'''
@app.get('/train')
async def trainRoute():
    os.system("python train.py")
    # os.system("dvc repro")
    return "Training done successfully!"

'''

# @app.get('/intent')
# async def intent(text):
    
#     try: 
#         # text= str_2_list_of_str(text)
#         # text= text.get("text")
        
#         intent, score, similarity= generate_intent_v2(text)
#         # embeddings= embeddings.reshape(1, -1)
        
#         # print(f"n_urls: {len(text)}")
#         # print(f"embeddings: {embeddings.shape}")

#         # return (embeddings[0][0].item())
#         return intent, score
#     except Exception as e:
#         return Response(f'Error occured: {e}')
#         # return Response(f'Error occured: {e}')

'''
@app.get('/intent_bert_based')
async def intent_bert_based(text):
    
    try: 
        # text= str_2_list_of_str(text)
        # text= text.get("text")
        
        return get_intent(text)
        return
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
'''

# @app.get('/intent_bert_based_v2')
# async def intent_bert_based_v2(text):
    
#     try: 
#         # text= str_2_list_of_str(text)
#         # text= text.get("text")
        
#         intent= get_intent_one_by_one(text)
#         # embeddings= embeddings.reshape(1, -1)
        
#         # print(f"n_urls: {len(text)}")
#         # print(f"embeddings: {embeddings.shape}")

#         # return (embeddings[0][0].item())
#         return intent
#     except Exception as e:
#         return Response(f'Error occured: {e}')
#         # return Response(f'Error occured: {e}')
        
@app.post('/intent_bert_based_v2_bulk')
async def intent_bert_based_v2_bulk(keyword:Intent):
    
    try: 
        
        intent= get_intent_bulk(keyword.keyword_list)

        return intent
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')



# @app.get('/sentence_analysis')
# async def sentence_analysis(text):
    
#     try: 
#         # text= str_2_list_of_str(text)
#         # text= text.get("text")
        
#         analysis= complete_sentence_analysis(text)
#         # embeddings= embeddings.reshape(1, -1)
        
#         # print(f"n_urls: {len(text)}")
#         # print(f"embeddings: {embeddings.shape}")

#         # return (embeddings[0][0].item())
#         return analysis
#     except Exception as e:
#         return Response(f'Error occured: {e}')
#         # return Response(f'Error occured: {e}')
        

'''
@app.get('/intent_bert')
async def intent_bert(text):
    
    try: 
        # text= str_2_list_of_str(text)
        # text= text.get("text")
        
        intent= get_intent(text)
        # embeddings= embeddings.reshape(1, -1)
        
        # print(f"n_urls: {len(text)}")
        # print(f"embeddings: {embeddings.shape}")

        # return (embeddings[0][0].item())
        return intent
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
'''

@app.get('/get_keywords')
async def intent(text):
    
    try: 
        # text= str_2_list_of_str(text)
        # text= text.get("text")
        
        keyword_list= generate_keyword_list(text)
        # embeddings= embeddings.reshape(1, -1)
        
        # print(f"n_urls: {len(text)}")
        # print(f"embeddings: {embeddings.shape}")

        # return (embeddings[0][0].item())
        return keyword_list
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
        

@app.post('/get_keywords_keybert')
async def get_keywords_keybert(kbtext: KeyBertKeywords):
    
    try: 
        
        keyword_list= generate_keywords_around_seed(
            kbtext.seed_keyword,
            kbtext.num_keywords,
            kbtext.num_urls,
            kbtext.top_n
        )
        return keyword_list
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
        
        

@app.post('/get_keywords_keybert_ngrams')
async def get_keywords_keybert_ngrams(kbtext: KeyBertKeywordsNGrams):
    
    try: 
        
        keyword_list= generate_keywords_Ngram(
            kbtext.keywords,
            kbtext.num_keywords,
            kbtext.top_n
        )
        return keyword_list
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
        
        
        
@app.post('/get_top_urls')
async def get_top_urls(text:Url):
    
    try: 
        # text= str_2_list_of_str(text)
        # n_urls= int(text.get("num_urls"))
        # text= text.get("text")
        # print(text)
        # print(type(text))
        list_of_urls= generate_top_urls(text.keyword, text.num_urls)
        # print('list_of_urls', list_of_urls)
        return list_of_urls
        # return get_top_urls(text)
        # return JSONResponse({
        #     "embeddings": (get_top_urls(text))
        # }, media_type='application/json')
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')

        
@app.post('/get_keywords_from_urls_list')
async def post_top_urls(keyword:Keyword):
    
    try: 
        # text= str_2_list_of_str(text)
        # n_urls= int(text.get("num_urls"))
        # url_list= text.get("text")
        url_list= keyword.url_list
        # print(text)
        # print(type(text))
        list_of_keywords= generate_keyword_list_v2(url_list)
        # print('list_of_urls', list_of_urls)
        return list_of_keywords
        # return get_top_urls(text)
        # return JSONResponse({
        #     "embeddings": (get_top_urls(text))
        # }, media_type='application/json')
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
        
        
@app.post('/post_top_urls_metadescription')
async def post_top_urls_metadescription(url:Url):
    
    try: 
        # text= str_2_list_of_str(text)
        # n_urls= int(text.get("num_urls"))
        # url_list= text.get("text")
        keyword= url.keyword
        num_urls= url.num_urls
        # print(text)
        # print(type(text))
        list_of_keywords= generate_keyword_list_v3(keyword, num_urls)
        # print('list_of_urls', list_of_urls)
        return list_of_keywords
        # return get_top_urls(text)
        # return JSONResponse({
        #     "embeddings": (get_top_urls(text))
        # }, media_type='application/json')
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')




if __name__=='__main__':
    # uvicorn.run(app, host='127.0.0.1', port=9003)
    # uvicorn.run(app, host='127.0.0.1', port=8081)
    uvicorn.run(app, host='0.0.0.0', port=8081)