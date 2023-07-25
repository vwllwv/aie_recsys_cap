import streamlit as st
import tensorflow as tf
import tensorflow_recommenders as tfrs

import os
import pprint
import tempfile

from typing import Dict, Text

import pandas as pd
import numpy as np

URL = 'https://store.steampowered.com/app/'
PATH = '/home/vern/aiedge_capstone/aie_recsys_cap/STEAM/model'

# Load it back; can also be done in TensorFlow Serving.
loaded = tf.saved_model.load(PATH)

st.title('Give me Steam game recommendations! :video_game:') 
user_id_input = st.text_input('Input User_id', )

def recommend():
	_, titles = loaded([user_id_input])
	byte_string = titles[0].numpy().tolist() # convert from tensor to list
	new_string = [s.decode() for s in byte_string] # byte_string to string
	for num, i in enumerate(new_string): # write the URLs for each rec game
		st.write(str(num+1)+'.'+' '+URL+i)


st.button('Recommend', on_click=recommend)