
from utils.client import generate_seo_metatitle
from utils.cleaner import extract_paragraphs
from keybert import KeyBERT
# kw_model = KeyBERT(model='thenlper/gte-base')
# kw_model = KeyBERT(model='all-MiniLM-L6-v2')
# kw_model = KeyBERT(model='Cohere/Cohere-embed-multilingual-light-v3.0')
# kw_model = KeyBERT(model='Cohere/Cohere-embed-multilingual-v3.0')
# kw_model = KeyBERT(model='TaylorAI/gte-tiny')


# from deepsparse.sentence_transformers import SentenceTransformer
# model = SentenceTransformer('zeroshot/gte-small-quant', export=False)
kw_model = KeyBERT(model="thenlper/gte-small")
# kw_model = KeyBERT(model="andersonbcdefg/bge-small-4096")

# kw_model = KeyBERT(model='intfloat/multilingual-e5-large')
import time



def generate_keywords_around_seed(
    seed_keyword:str,
    num_keywords: int= 50,
    num_urls: int=10,
    top_n: int= 7
):
    metatitle= generate_seo_metatitle(seed_keyword, num_query_results=num_urls)
    keywords_list= []
    for i in range(1, top_n):
        keywords = kw_model.extract_keywords(metatitle, 

                                     keyphrase_ngram_range=(1, i), 

                                     stop_words='english', 

                                     highlight=False,
                                     
                                    #  use_mmr=True, 
                                     
                                    #  diversity=0.7,

                                     top_n=num_keywords//2,
                                     
                                    #  nr_candidates=2*num_keywords
                                     nr_candidates=2*num_keywords
                                     )

        keywords_list+= keywords
    
    keywords_list= list(set(keywords_list))
    return ( sorted(keywords_list,
                    key=lambda x: x[1],reverse=True)[:num_keywords], 
            
            
            
            )



def generate_keywords_Ngram(
    keywords_in: list[str],
    num_keywords: int,
    top_n: int,
    start_time=time.time()
):
    
    
    metatitle= ' \n'.join(keywords_in)
    keywords_list= []
    for i in range(1, top_n):
        keywords = kw_model.extract_keywords(metatitle, 

                                     keyphrase_ngram_range=(1, i), 

                                     stop_words='english', 

                                     highlight=False,
                                     
                                    #  use_mmr=True, 
                                     
                                    #  diversity=0.7,

                                     top_n=num_keywords,
                                     
                                     nr_candidates=3*num_keywords
                                     )

        keywords_list+= keywords
    
        
    print("--- %s seconds ---[GENERATED KEYWORD LIST]" % (time.time() - start_time), flush=True)
    
    keywords_list= list(set(keywords_list))
    print("--- %s seconds ---[GENERATED KEYWORD LIST-DEDUPED]" % (time.time() - start_time), flush=True)
    # keywords_list= [list(i) for i in keywords_list]
    max_count= 1
    for i in range(len(keywords_list)):
        temp= list(keywords_list[i])
        mc_i= metatitle.count(
                ' '+ temp[0]+' ')
        temp.append(
            mc_i
        )
        max_count= max(max_count, mc_i)
        keywords_list[i]= temp
    
    print("--- %s seconds ---[GENERATED KEYWORD LIST-COUNT]" % (time.time() - start_time), flush=True)
    return sorted(keywords_list,
                    key=lambda x: x[1] if (x[2]>2 and x[1]>0.8) else (x[2]/max_count)-0.25,
                    reverse=True)[:num_keywords]
        