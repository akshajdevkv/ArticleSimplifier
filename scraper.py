from bs4 import BeautifulSoup
import requests
from string import Template
import webbrowser

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

url = 'http://opensource.guide/starting-a-project/'
r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.text,'html.parser')
heading = soup.find('h1')
sub_heading = soup.find('h2')
raw_contents = soup.find_all(['p','ul','ol','h1','h2','figure','blockquote'])[3:-20]
contents = ''


for i in raw_contents:
    if '<figure' in str(i):
        image  = i.find('img')
        contents += (str(image).replace('/60/','/1000/'))
    else:
        contents += str(i)
 
with open('/home/akshajdev/Desktop/Python Projects/Article Simplifier/template.html','r') as f:
    html_content = f.read() 
    t = Template(html_content)

with open('/home/akshajdev/Desktop/Python Projects/Article Simplifier/original.html','w') as f:
    f.write(t.safe_substitute({'content': contents,'title':heading.text,'heading':heading.text,'sub_heading':sub_heading.text}))

