from bs4 import BeautifulSoup
with open('EBSCOhost3\.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
text = soup.get_text()
print(type(text),len(text))