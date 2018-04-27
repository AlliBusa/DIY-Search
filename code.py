#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
abspath = os.path.dirname("/home/allison/dream5/webpy-webpy-817c979/web")
sys.path.append(abspath)
os.chdir(abspath)
import web
from pprint import pprint
import datasearcher


urls = (
  '/', 'index',
  '/results', 'results'
)

render = web.template.render('/home/allison/dream5/templates/')

class index:
    def GET(self, name=None):
        return render.index()



class results:
    def GET(self):
        data_list = []
        result = web.input() #takes the url
        for key in result: #takes the keyword and appends to list
            data_list.append(key)

        data = datasearcher.run_search(data_list) #searches the database with the list
        return render.results(data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
