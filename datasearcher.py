#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import code
from bs4 import BeautifulSoup as Soup

data = pd.read_csv("/home/allison/dream5/DataBase.csv", encoding="utf-8")
df = pd.DataFrame(data)

def join_materials(*materials):
    """Joins the keywords to make one search term"""
    materials = '|'.join(*materials)
    return materials

def run_search(*materials):
    """Looks for all rows that have one of the strings of
    the keywords contained in the row named 'Materials'"""
    materials = join_materials(*materials)
    df2 = df.loc[df['Materials'].str.contains(materials)]
    pd.set_option('display.max_colwidth', -1) #displays the whole text
    pd.set_option('display.encoding', 'utf-8') #changes the encoding
    return df2.to_html(index=False, escape=False)
