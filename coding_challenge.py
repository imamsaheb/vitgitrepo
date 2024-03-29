import requests
from json2html import *
import pdfkit
import os


class challenge():

    def __init__(self):
        pass

    def unit_test(self, url):
        r = requests.get(url)
        return r.status_code
    
    def fetch_users_generate_report(self):
        r = requests.get("https://reqres.in/api/users?page=2")
        response_val = dict(r.json())
        val = response_val.get('data')
        print("json data", val)
        print("----------------------------------------------------------------------")
        open_tag = "<"
        closed_tag = ">"
        val1 = json2html.convert(json=val)
        for ele in val:
            avatar = ele['avatar']
            ele['avatar'] = open_tag + 'img src="' + avatar + '"' + closed_tag
        print("after adding img src", val)
        print("----------------------------------------------------------------------")
        html_data = json2html.convert(json=val)
        print("json to html", html_data)
        print("----------------------------------------------------------------------")
        data1 = html_data.replace("&lt;", "<")
        data2 = data1.replace("&gt;", ">")
        data3 = data2.replace("&quot;", '"')
        print("after replacing special character", data3)
        print("----------------------------------------------------------------------")
        file1 = open("users.html", "w")
        file1.write(data3)
        pdfkit.from_string(val1, 'users_pdf.pdf')

obj = challenge()
obj.fetch_users_generate_report()
