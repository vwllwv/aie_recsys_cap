import streamlit as st
import tensorflow as tf
import tensorflow_recommenders as tfrs

import os
import pprint
import tempfile

from typing import Dict, Text

import pandas as pd
import numpy as np


#### Data prep, similarity match below
import difflib
import re

# Contains User actions (buy/play associated with games - the users game library w/metadata for each game)
df_users = pd.read_csv('../clean_datasets/final2/user_steam_lib_final.csv') 
# Contains Games (unique games by their appid and metadata e.g. price, ratings, genre, tags)
df_games = pd.read_csv('../clean_datasets/final2/games_list_final.csv')   

# converting "appid", "english", and other columns from float to int
df_games = df_games.astype({"name":'string', "og_name": 'string', "appid":'int', "release_date":'string',
                            "english":'int', "developer":'string', "publisher":'string', "platforms":'string',
                            "required_age":'int', "categories":'string', "genres":'string', 
                            "steamspy_tags":'string', "achievements": 'int', "positive_ratings":'int', 
                            "negative_ratings":'int', "average_playtime":'int', "median_playtime":'int',
                            "owners":'string', "price":'float64'
                           }) 
df_users = df_users.astype({ "user_id":'string', "name":'string', "play":'int', "purchase":'int', 
                            "og_name": 'string', "appid":'int', "release_date":'string',
                            "english":'int', "developer":'string', "publisher":'string', "platforms":'string',
                            "required_age":'int', "categories":'string', "genres":'string', 
                            "steamspy_tags":'string', "achievements": 'int', "positive_ratings":'int', 
                            "negative_ratings":'int', "average_playtime":'int', "median_playtime":'int',
                            "owners":'string', "price":'float64'
                           }) 

# Extract out the columns of user_id and appid (the user game library)
df_user_lib = df_users[["user_id", "appid"]]
df_user_lib = df_user_lib.astype({"appid":'int'})
df_user_lib = df_user_lib.astype({"user_id":'string',"appid":'string'})
uniq_user_ids = df_user_lib.user_id.unique()

# Important to convert dataframe into a dictionary to process, key is user, values is list of appids the user owns
d = df_user_lib.groupby('user_id')['appid'].apply(list).to_dict()

# iterate through the unique_user_ids list, compute similarity with the user_input_list
# return a list where the first element is the most similar user ID, 2nd element is the similarity score
def find_similarity(user_lib_dict, user_input_list, unique_user_ids):
    most_id = 'dummy'
    most_sim = 0
    results = []
    for x in unique_user_ids: 
        sm = difflib.SequenceMatcher(None, user_lib_dict.get(x), user_input_list)
        smr = sm.ratio()
        if smr > most_sim:
            most_id = x
            most_sim = smr
    results = [most_id, most_sim]
    return results



#### Streamlit app below

URL = 'https://store.steampowered.com/app/'
PATH = '../tf_models/model'
games_list = []  # list of game recs

# Load tf model back; can also be done in TensorFlow Serving.
loaded = tf.saved_model.load(PATH)

container = st.container() # create a container element to order page elements

def recommend():
	collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
	g_list = collect_numbers(numbers) # take in a list of numbers user input
	g_str_list = [str(x) for x in g_list] # turn list of int appid to str
	#container.write(g_str_list)

	user_id_input = find_similarity(d, g_str_list, uniq_user_ids)
	container.write('Most Similar User ID to your game choices:')
	container.write(user_id_input[0])
	
	_, titles = loaded([user_id_input[0]])
	byte_string = titles[0].numpy().tolist() # convert from tensor to list
	new_string = [s.decode() for s in byte_string] # byte_string to string
	for num, i in enumerate(new_string): # write the URLs for each rec game
		games_list.append(str(num+1)+'.'+' '+URL+i)
		#st.write(str(num+1)+'.'+' '+URL+i)
	for g in games_list:
		container.write(g)

with container:
	st.title('Give me 10 Steam game recommendations! :video_game:') 
	#games_input = st.text_input('Input Games App ID', )
	
	numbers = st.text_input("Please enter game app_ID numbers:")
	
	st.button('Recommend', on_click=recommend)



