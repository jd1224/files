import requests
import csv

out = 'output.csv'
f = open(out, 'w')
with f:
    
    ip = '80.80.80.80'
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey':'2fb1db9bbb2b4b5b400e54e7375415192664475038c5bd8c9dfcd7693d277339','ip':ip}
    response = requests.get(url, params=params)
    serials = response.json()
    fnames = ['response_code','verbose_msg','asn','country','resolutions','undetected_urls','undetected_referrer_samples','whois','whois_timestamp','detected_urls','undetected_downloaded_samples','detected_communicating_samples','undetected_communicating_samples','network','detected_downloaded_samples','as_owner','detected_referrer_samples','continent']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
 
    print (serials['continent'])
    print (len(serials['detected_referrer_samples']))
    print (serials['as_owner'])
    print (len(serials['detected_downloaded_samples']))
    print (serials['network'])
    print (len(serials['undetected_communicating_samples']))
    print (len(serials['detected_communicating_samples']))
    print (len(serials['undetected_downloaded_samples']))
    print (len(serials['detected_urls']))
    print (serials['whois_timestamp'])
    print (serials['whois'])
    print (len(serials['undetected_referrer_samples']))
    print (len(serials['undetected_urls']))
    print (len(serials['resolutions']))

    with open('output.csv') as output:
        writer.writerow(serials)
