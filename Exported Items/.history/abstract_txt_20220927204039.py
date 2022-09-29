from bs4 import BeautifulSoup
soup = BeautifulSoup('EBSCOhost3\.html', 'html.parser')

print(soup.prettify())
