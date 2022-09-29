from email import header
from bs4 import BeautifulSoup
import csv
with open('Exported Items/EBSCOhost20..html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find(id = "records")
txt = records.get_text()

new_txt = txt.replace('Business Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")

partition = new_txt.split('partitionmark')

f = open('articles.csv', 'w')
writer = csv.writer(f)

header = ['Number', "Body"]
writer.writerow(header)
count = 1
for i in range (len(partition)):
    if len(partition[i]) > 40000:
        row = [count, partition[i]]
        writer.writerow(row)
