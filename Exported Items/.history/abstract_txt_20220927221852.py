from bs4 import BeautifulSoup
with open('EBSCOhost3\.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find(id = "records")
text = records.get_text()
# print(type(text),len(text))

print(len(text))
# # print(text[:1000])
# mydivs = soup.find( "div", {"class": "print-citation"})
# print(len(mydivs))
piece = text.split('Business Source Completed')
print(len(piece))
print(piece[1])