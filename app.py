import uvicorn
import sys
import os
from fastapi import FastAPI, HTTPException, status, APIRouter
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
from keys import fastapi_key
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'
import time

# from utils.get_keywords_utils import (
#                                       generate_keywords_around_seed,
#                                       generate_keywords_Ngram
#                                       )

from pydantic import BaseModel

class KeyBertKeywords(BaseModel):
    seed_keyword:str= ""
    num_keywords: int= 50
    num_urls: int=10
    top_n: int= 7
    # fastapi_key: str=""
    
class KeyBertKeywordsNGrams(BaseModel):
    keywords: list[str]= [""]
    num_keywords: int= 50
    top_n: int= 4
    # fastapi_key: str=""

class Keyword(BaseModel):
    url_list: list
    # fastapi_key: str=""

class Url(BaseModel):
    keyword: str=""
    num_urls: int=10
    keyword_list: list[str]= [""]
    # fastapi_key: str=""

class Intent(BaseModel):
    keyword_list: list[str] or str= [""]
    # fastapi_key: str=""


import json

from Utils.text_keyword_extraction import generate_keyword_list, generate_keyword_list_v2, generate_keyword_list_v3
from Utils.client import generate_top_urls
from Utils.get_intent_bert_basedANN import  get_intent_bulk
# from Utils.get_sentence_status import complete_sentence_analysis
# from Utils.bert_fine_tuned_intent import get_intent
# from main import generate_intent_v2




from fastapi.security import APIKeyHeader
from fastapi import Security

api_key_header= APIKeyHeader(name="X-API-Key")
api_keys = [
    fastapi_key
]  # This is encrypted in the database


def api_key_auth(api_key: str = Security(api_key_header)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid FAST_API_ENDPOINT_KEY"
        )

app = FastAPI()
router= APIRouter(dependencies=[Security(api_key_auth)])



print("initializing app")

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')
    # return "Hello world!"


@router.post('/intent_bert_based_v2_bulk')
async def intent_bert_based_v2_bulk(keyword:Intent):
    
    try: 
        
        
        intent= get_intent_bulk(keyword.keyword_list)

        return intent
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')


@router.get('/get_keywords')
async def get_keywords(text):
    
    try: 
        # text= str_2_list_of_str(text)
        # text= text.get("text")
        
        keyword_list= generate_keyword_list(text)

        return keyword_list
    except Exception as e:
        return Response(f'Error occured: {e}')
        # return Response(f'Error occured: {e}')
     
        
@router.post('/get_top_urls')
async def get_top_urls(text:Url):
    
    try: 
        
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

        
@router.post('/get_keywords_from_urls_list')
async def post_top_urls(keyword:Keyword):
    
    try: 
        
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
        
        
@router.post('/post_top_urls_metadescription')
async def post_top_urls_metadescription(url:Url):
    
    try: 
        
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