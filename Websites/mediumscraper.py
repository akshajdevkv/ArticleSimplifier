from bs4 import BeautifulSoup
import requests
from string import Template
import os

output_path = os.environ.get('output_path')
template_path = os.environ.get('template_path')

url = 'https://medium.com/illumination-curated/elon-musks-one-rule-for-learning-smarter-faster-and-better-b08bb30499'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
heading = soup.find('h1')
sub_heading = soup.find('h2')
content = ''

for i in soup.find_all(['p','ul','ol','h1','h2','blockquote','figure'])[3:-20]:
    if '<figure' in str(i):
        image  = i.find('img') 
        content += str(image).replace('/60/','/1000/').replace('width','id').replace('height','class')
    else:
        content += str(i)
 
with open(template_path,'r') as f:
    html_content = f.read() 
    t = Template(html_content)

with open(output_path,'w') as f:
    f.write(t.safe_substitute({'content': content,'title':heading.text,'heading':heading.text,'sub_heading':sub_heading.text}))

