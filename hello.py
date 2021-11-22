import requests
from json2html import *
r = requests.get("https://reqres.in/api/users?page=2")
response_val = dict(r.json())
val = response_val.get('data')
for ele in val:
    avatar = ele['avatar']
    ele['avatar'] = '<img src="' + avatar + '"' + '/>'
html_data = json2html.convert(json=val)
print(html_data)
file1 = open("index.html", "w")
file1.write(html_data)
