from bs4 import BeautifulSoup
with open('EBSCOhost3\.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find("div", {"id": "records"})
text = records.get_text()
# print(type(text),len(text))
print(records)