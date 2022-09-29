from bs4 import BeautifulSoup
import csv

with open('/Users/richardpang/Desktop/extract_maintext/extract_maintext/Exported Items/EBSCOhost50.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
records = soup.find(id = "records")
txt = records.get_text()

new_txt = txt.replace('Business Source Complete', "partitionmark")
new_txt = new_txt.replace('Footnotes', "partitionmark")
new_txt = new_txt.replace('Supplemental Material', "partitionmark")

partition = new_txt.split('partitionmark')
print("partition", len(partition))
f = open('articles50.csv', 'w')
writer = csv.writer(f)

header = ['Number', "Body"]
writer.writerow(header)
count = 1
for i in range (len(partition)):
    if len(partition[i]) > 40000:
        print(count,partition[i][:30])
        row = [count, partition[i]]
        writer.writerow(row)
        count += 1
