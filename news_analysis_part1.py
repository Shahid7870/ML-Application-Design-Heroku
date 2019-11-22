# -*- coding: utf-8 -*-
import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
import spacy
from spacy import displacy
import pandas as pd
import wordcloud
import matplotlib.pyplot as plt

channel_name='www.ndtv.com'
categories=['business','education','science','india-news',
            'entertainment','opinion']
for category in categories:
    url='https://'+channel_name+'/'+category
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'html.parser')
    filename=category+'.txt'
    with open(filename,'w') as f:
        for link in soup.find_all('a',href=True):
            temp_link=link['href']
            if url in temp_link and '/video' not in temp_link \
                and '/photos' not in temp_link:
                    if '?' in temp_link:
                        link,_=temp_link.split('?')
                    else:
                        link=temp_link
                    title=link.split('/')[-1]
                    title_list=title.split('-')
                    if len(title_list)>3:
                        f.write(link)
                        f.write('\n')