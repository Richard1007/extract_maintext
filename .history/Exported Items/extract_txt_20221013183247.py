from bs4 import BeautifulSoup
import pandas as pd
import csv


# Record titles
def find_articles(html_article,output_file):
    titles_abstract = []
    with open(html_article, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    titles=soup.find_all('h1',{'class':"delivery-title"})

    for i in titles:
        title = i.get_text().replace(u'\xa0', u'')
        # Get abstract
        abstract = i.findNext('p').get_text()
        titles_abstract.append([title,abstract])

    # Read articles
    records = soup.find(id = "records")
    print('records: ',len(records))

    # Delete keywords
    for p in records.find_all('p', {"class":"body-paragraph"}):
        if p.get_text()[:9] == 'Keywords:':
            p.string = ''
        if p.get_text()[:18] == 'Online Supplement:':
            p.string = ''

    # Delete tables
    for table in records.find_all('table'):
        i = table.extract()
    txt = records.get_text()

    new_txt = txt.replace('Database:\n\t\t\t\t\t\tBusiness Source Complete', "partitionmark")
    new_txt = new_txt.replace('Footnotes', "partitionmark")
    new_txt = new_txt.replace('Supplemental Material', "partitionmark")
    partition = new_txt.split('partitionmark')
    # print("partition", len(partition))

    f = open(output_file, 'w')
    writer = csv.writer(f)
    header = ['Number', 'Word Count',"Title", 'Abstract','Body' ]
    writer.writerow(header)
    count = 1
    for i in range (len(partition)):
        # print(i,len(partition[i]))
        text = partition[i]
        if len(text) > 20000:
            for pair in titles_abstract:
                title = pair[0]
                abstract = pair[1]
                if text[:50] in title:
                    text = text[len(title)+1:]
                    text = text[len(abstract):]
                    row = [count,len(text),title,abstract,text]
                    writer.writerow(row)
                    count += 1
    print("Number of articels:", count-1)




html_article = '/Users/richardpang/Desktop/extract_maintext/extract_maintext/JM dataset/JM2001-2005.html'
output_file = '/Users/richardpang/Desktop/extract_maintext/extract_maintext/JM outpout/2001-2005JM.csv'

find_articles(html_article,output_file)