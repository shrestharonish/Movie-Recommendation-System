import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

"""
Works for imdb pages recommend using all the pages with
genres information discards all the ones with less than 3 genres type
"""

def get_all_titles(soup):
    result_topics = []
    all_topics = soup.find_all('h3', {"class":"lister-item-header"})
    # print(all_topics)
    for topic in all_topics:
        topic=topic.find('a')
        # topic=str(topic.find('a'))
        # topic=topic.replace("<", '=')
        # topic=topic.replace(">","=")
        # topic=topic.split('=')
        # topic=topic[int(len(topic)/2)]
        result_topics.append(topic.getText())
    
    return result_topics


def data_set(url):
    data_set=pd.DataFrame(columns= ["Movie", "Primary Genre", "Secondary Genre", "Tertiary Genre"])
    #Initially get the page from the url and from the content extract all the things properly so page is extracted
    page = requests.get(url)

    #Soup is created where all the content is parsed as html format so it can be extracted as seen in webpages.
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    ##############################################################################################################
    title = get_all_titles(soup)
    print(title)
    # genres = get_all_genres(genres)
    # genres = post_process(genres)
    # data_set["Movie"]=pdSeries(title)
    # data_set["Primary Genre"] =pd.Series(genre)
    # data_set["Primary Genre"] =data_set("Primary Genre").apply(check_repeated_comma)
    # data_set["Secondary Genre"] = data_set("Secondary Genre").fillno("To Be filled")

import os
os.system('cls')
print("IMDB Scrapper")
number_of_pages = int(input("Enter the number of various pages to scrap:"))
for i in range(number_of_pages):
    url = input("Enter the url: ")
    data_set(url)