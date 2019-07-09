import requests
import csv

out = 'output.csv'
f = open(out, 'w')
with f:
 fnames = ['source','category','activity','confidence','last_updated','name','intention','first_seen','metadata','tor','rdns_parent','link','org','os','asn','rdns']
 writer = csv.DictWriter(f, fieldnames=fnames)
 writer.writeheader()
 with open('output.csv') as output:
  with open('input.csv') as csvfile:
   filereader = csv.reader(csvfile, delimiter = '\n')
   for row in filereader:
    for item in row: #item is record
     print (item)
     data = {
     'ip': item
     }
     response = requests.post('http://api.greynoise.io:8888/v1/query/ip', data=data)
     try:
      serials =  response.json()
     except Exception as e:
       print (e)
       print (response)
     try:
      y=0
      for x in range(0,499):
       serials['records'][x]['source'] = item
       writer.writerow(serials['records'][x])
       y+=1
     except:
      neg = {'source': item, 'category': str(y) + ' Hits'}
      writer.writerow(neg)
