from bs4 import BeautifulSoup
with open('EBSCOhost3\.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find(id = "records")
text = records.get_text()
print(type(text),len(text))
# print(type(records), len(records))
# print(records[1])
# print(text[:1000])
mydivs = soup.find( "div", {"class": "print-citation"})
print(len(mydivs))


# print(mydivs[0])