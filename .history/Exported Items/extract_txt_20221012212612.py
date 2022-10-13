from bs4 import BeautifulSoup
import csv
import pandas as pd

# Record titles
titles_lst = []
with open('/Users/richardpang/Desktop/extract_maintext/extract_maintext/Exported Items/EBSCOhost50.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
titles=soup.find_all('h1',{'class':"delivery-title"})
# Get titles
for i in titles:
    title = i.get_text().replace(u'\xa0', u'')
    # if title != 'Acknowledgments':
    print(title)
    titles_lst.append(title)
print("Number of titles: ",len(titles_lst))
titles_lst_df = pd.DataFrame(titles_lst)
titles_lst_df.to_csv('titles.csv')
# Records consist of articles
records = soup.find(id = "records")
# # Wrap keywords
# keywords = soup.new_tag('keywords')
# for p in records.find_all('p', {"class":"body-paragraph"}):
#     if p.get_text()[:9] == 'Keywords:':
#         p.wrap(keywords)

# # Replace "Keywords: ...." with "keywords_delete_this"
# for keywords in records.find_all('keywords'):
#     for p in keywords.find_all('p'):
#         p.string = " XXXXXXXXX "
#     print(keywords.get_text())

# Wrap keywords

for p in records.find_all('p', {"class":"body-paragraph"}):
    if p.get_text()[:9] == 'Keywords:':
        p.string = 'KEYWORDS_SPLIT'

# Delete tables
for table in records.find_all('table'):
    i = table.extract()
txt = records.get_text()

new_txt = txt.replace('Database:\n\t\t\t\t\t\tBusiness Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")
new_txt = new_txt.replace('Supplemental Material', "partitionmark")
partition = new_txt.split('partitionmark')
# print("partition", len(partition))


f = open('articles50.csv', 'w')
writer = csv.writer(f)
header = ['Number', "Title", 'Abstract','Body' ]
writer.writerow(header)
count = 1
for i in range (len(partition)):
    # print(i,len(partition[i]))
    text = partition[i]
    if len(text) > 40000:
        if text[0].isupper():
        # print(count,partition[i][:30])
        # partition[i] is the main text
            abstract = text.split('KEYWORDS_SPLIT',1)[0]
            body = text.split('KEYWORDS_SPLIT',1)[1]
            for title in titles_lst:
                if abstract[:50] in title:
                    # print(title,abstract[:50])
                    # print(abstract[:50])
                    abstract = abstract[len(title):]
                    # print(abstract)
                    row = [count, title, abstract, body]
                    writer.writerow(row)
                    count += 1
print(count-1)