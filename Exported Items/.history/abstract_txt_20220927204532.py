from bs4 import BeautifulSoup
with open('EBSCOhost3\.html', 'r') sa f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.prettify())
