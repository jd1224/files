import requests
import csv
import os

origdir = os.getcwd()
with open('input.csv') as csvfile:
   filereader = csv.reader(csvfile, delimiter = ',')
   for row in filereader:
    for item in row: #item is record
     
        ip = item

        try:
            os.mkdir(ip)
        except Exception as e:
            print(e)
            
        os.chdir(ip)
        url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
        params = {'apikey':'2fb1db9bbb2b4b5b400e54e7375415192664475038c5bd8c9dfcd7693d277339','ip':ip}
        response = requests.get(url, params=params)
        serials = response.json()
        fields = ['undetected_downloaded_samples','detected_downloaded_samples',\
                'detected_referrer_samples','undetected_referrer_samples','resolutions',\
                'detected_communicating_samples',\
                'detected_urls',\
                'undetected_communicating_samples']
        '''
        for item in fields:
            try:
                for field in serials[item][0]:
                    print (item+' FIELD '+field)
            except:
                print(item+' NO FIELD')
        '''
        
        printer = 'Message: '+serials['verbose_msg']+' '+'ip'+'\n'
        
        try:
            printer += 'Network: '+serials['network']+'\n'+\
                ''''Continent: '+serials['continent']+'\n'\
                +'Country: '+str(serials['country'])+'\n'+'*******************WHOIS LOOKUP***********************\n'+serials['whois']+\
                '\n*******************WHOIS END***********************************\n'\
                +'ASN: '+str(serials['asn'])+'\n'\
                +'Owner: '+serials['as_owner']+'\n'+'undetected_urls: '''
        except:
            pass
                
        try:        
            for url in serials['undetected_urls']:
                printer += url[0]+'\n'
        except:
            pass
        report = open(ip+'report.txt','w')
        report.write(printer)
        report.close()

        for item in fields:
            #print ('in for loop')
            out = ip+'_'+item+'_'+'output.csv'
            f = open(out,'w')
            fnames = []
            '''
            try:
                for field in serials[item][0]:
                    print (item+' FIELD '+field)
            except:
                print(item+' NO FIELD')
            '''
            try:
                for field in serials[item][0]:
                    fnames.append(field)
            except:
                pass
            '''
            for x in fnames:
                print (item + str(x))
            '''
            with f:
                writer = csv.DictWriter(f, fieldnames=fnames)
                writer.writeheader()
            
                with open(out) as output:
                    try:
                        writer.writerows(serials[item])
                    except Exception as e:
                        pass
        os.chdir(origdir)
        '''
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
            
            print (response)
            print (serials['resolutions'][0])
            
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
        '''