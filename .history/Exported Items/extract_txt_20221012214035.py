from bs4 import BeautifulSoup
import csv
import pandas as pd

html_article = 'Exported Items/JM2021-2022.html'
output_file = 'Output/2021-2022JM.csv'
# Get all titles
titles_lst = []
with open(html_article, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
titles=soup.find_all('h1',{'class':"delivery-title"})

for i in titles:
    title = i.get_text().replace(u'\xa0', u'')
    titles_lst.append(title)


# Locate articles
records = soup.find(id = "records")

# Remove keywords
for p in records.find_all('p', {"class":"body-paragraph"}):
    if p.get_text()[:9] == 'Keywords:':
        p.string = 'KEYWORDS_SPLIT'

# Delete tables
for table in records.find_all('table'):
    i = table.extract()
txt = records.get_text()

# Split
new_txt = txt.replace('Database:\n\t\t\t\t\t\tBusiness Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")
new_txt = new_txt.replace('Supplemental Material', "partitionmark")
partition = new_txt.split('partitionmark')

# Export files
f = open(output_file, 'w')
writer = csv.writer(f)
header = ['Number', "Title", 'Abstract','Body' ]
writer.writerow(header)
count = 1
for i in range (len(partition)):
    text = partition[i]
    # If this text is a main text of an article
    if len(text) > 40000:
        if text[0].isupper():
            abstract = text.split('KEYWORDS_SPLIT',1)[0]
            body = text.split('KEYWORDS_SPLIT',1)[1]
            for title in titles_lst:
                # Check if the first part of abstract is in title_lst
                if abstract[:50] in title:
                    # Remove title from abstract
                    abstract = abstract[len(title):]
                    row = [count, title, abstract, body]
                    writer.writerow(row)
                    count += 1
print("Total articles:", count-1)