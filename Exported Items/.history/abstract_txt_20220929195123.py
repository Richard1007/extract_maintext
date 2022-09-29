from bs4 import BeautifulSoup
with open('EBSCOhost50.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find(id = "records")
txt = records.get_text()

new_txt = txt.replace('Business Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")

lst = new_txt.split('partitionmark')
article = []
for i in range(1,len(lst),2):
    article.append(lst[i])
