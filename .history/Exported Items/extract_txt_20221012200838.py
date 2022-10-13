from bs4 import BeautifulSoup
import csv


with open('/Users/richardpang/Desktop/extract_maintext/extract_maintext/Exported Items/EBSCOhost50.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
titles=soup.find_all('h1',{'class':"delivery-title"})
titles_lst = []

# Get titles
for i in titles:
    title = i.get_text().replace(u'\xa0', u'')
    if title != 'Acknowledgments':
        titles_lst.append(title)
print("The number of titles: ", len(titles_lst))

# Records consist of articles
records = soup.find(id = "records")

# Replace keywords with a splitter
for p in records.find_all('p', {"class":"body-paragraph"}):
    if p.get_text()[:9] == 'Keywords:':
        p.string = 'partitionmark'

# Delete tables
for table in records.find_all('table'):
    i = table.extract()
txt = records.get_text()

new_txt = txt.replace('Business Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")
new_txt = new_txt.replace('Supplemental Material', "partitionmark")
partition = new_txt.split('partitionmark')

# Export text 
f = open('articles50.csv', 'w')
writer = csv.writer(f)
header = ['Number', "Body"]
writer.writerow(header)
count = 0
for i in range (len(partition)):
    # print(i,len(partition[i]))
    if len(partition[i]) > 40000:
        if partition[i][0].isupper():
        # print(count,partition[i][:30])
            row = [count, partition[i]]
            writer.writerow(row)
            count += 1
print("The number of main text:", count)

