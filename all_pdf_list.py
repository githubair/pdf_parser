from bs4 import BeautifulSoup
import requests

url = 'http://compalg.inf.elte.hu/~attila/materials/'
ext = 'pdf'

f = open('text.txt', 'w')

def listing(url, ext='\n'):
    page = requests.get(url).text
    # print (page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + i.get('href') + '\n' for i in soup.find_all('a') if i.get('href').endswith(ext)]

for file in listing(url, ext):
    print (file)
    f.write(file)


f.close()

