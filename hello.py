import requests
from json2html import *

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
file1 = open("repor.html", "w")
file1.write(data3)
