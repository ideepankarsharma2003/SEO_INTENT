from Utils.client import generate_seo_metatitle_train
import pandas as pd
df= pd.read_csv('data/keyword_intent.csv')
# df.head()
import pickle
from tqdm import tqdm


reverse_intent= {
    0: 'informational',
    1: 'navigational',
    2: 'transactional',
    3: 'commercial',
    4: 'local'
}
print("<<<<<<<<<<<<<<<<<<<    TRAINING STARTED   >>>>>>>>>>>>>>>>")

from main import generate_base_embeddings



df_informational= df[df.intent=='Informational']
informational_keywords= list(df_informational.keyword)
# informational_keywords
informational_keywords_embeddings= []
for i in tqdm(informational_keywords):
    s_i= generate_seo_metatitle_train(i)
    e_i= generate_base_embeddings(s_i)
    informational_keywords_embeddings.append(e_i)
    
informational= sum(informational_keywords_embeddings)/len(informational_keywords_embeddings)


print("Successfully generated the Informational Embeddings")





df_navigational= df[df.intent=='Navigational']
navigational_keywords= list(df_navigational.keyword)
navigational_keywords

# navigational_keywords= [
#     't mobile town east',
#     'starbucks',
#     'tech crunch',
#     'elevenlabs'
# ]
navigational_keywords_embeddings= []
for i in tqdm(navigational_keywords):
    s_i= generate_seo_metatitle_train(i)
    e_i= generate_base_embeddings(s_i)
    navigational_keywords_embeddings.append(e_i)
    
navigational= sum(navigational_keywords_embeddings)/len(navigational_keywords_embeddings)


print("Successfully generated the Navigational Embeddings")





df_transactional= df[df.intent=='Transactional']
transactional_keywords= list(df_transactional.keyword)
transactional_keywords
# transactional_keywords= [
#     't mobile town east',
#     # 'llama',
#     'tire patch kit',
#     'cat shelves'
# ]
transactional_keywords_embeddings= []
for i in tqdm(transactional_keywords):
    s_i= generate_seo_metatitle_train(i)
    e_i= generate_base_embeddings(s_i)
    transactional_keywords_embeddings.append(e_i)

transactional= sum(transactional_keywords_embeddings)/len(transactional_keywords_embeddings)
print("Successfully generated the Transactional Embeddings")



df_commercial= df[df.intent=='Commercial']
commercial_keywords= list(df_commercial.keyword)
commercial_keywords
# commercial_keywords= [
#     'citalopram vs prozac',
#     'duffel bags',
#     'screen protector'
# ]
commercial_keywords_embeddings= []
for i in tqdm(commercial_keywords):
    s_i= generate_seo_metatitle_train(i)
    e_i= generate_base_embeddings(s_i)
    commercial_keywords_embeddings.append(e_i)
    
commercial= sum(commercial_keywords_embeddings)/len(commercial_keywords_embeddings)

print("Successfully generated the Commercial Embeddings")




df_local= df[df.intent=='Local']
local_keywords= list(df_local.keyword)
local_keywords
# local_keywords= [
#     'chinese food delivery near me'
# ]
local_keywords_embeddings= []
for i in tqdm(local_keywords):
    s_i= generate_seo_metatitle_train(i)
    e_i= generate_base_embeddings(s_i)
    local_keywords_embeddings.append(e_i)
    
local= sum(local_keywords_embeddings)/len(local_keywords_embeddings)
print("Successfully generated the Local Embeddings")



intent_embeddings= [informational, navigational, transactional, commercial, local]



pickle.dump(intent_embeddings, open('Utils/intent_embeddings.pkl', 'wb'))

print("Successfully dumped Embeddings")
print("<<<<<<<<<<<<<<<<<<<    TRAINING COMPLETED    >>>>>>>>>>>>>>>>")
