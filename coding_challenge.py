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
        open_tag = "<"
        closed_tag = ">"
        for ele in val:
            avatar = ele['avatar']
            ele['avatar'] = open_tag + 'img src="' + avatar + '"' + closed_tag
        print(val)
        html_data = json2html.convert(json=val)
        data1 = html_data.replace("&lt;", "<")
        data2 = data1.replace("&gt;", ">")
        data3 = data2.replace("&quot;", '"')
        file1 = open("users.html", "w")
        file1.write(data3)
        pdfkit.from_file(data3, 'users_pdf.pdf')

obj = challenge()
obj.fetch_users_generate_report()
