import requests
import csv
import os
import time 

count = 0

origdir = os.getcwd()
with open('input.csv') as csvfile:
   filereader = csv.reader(csvfile, delimiter = ',')
   for row in filereader:
    for item in row: #item is record
    
        ip = item
        print (ip)
        try:
            os.mkdir(ip)
        except Exception as e:
            print(e)
            
        os.chdir(ip)
        url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
        params = {'apikey':'INSERT API FROM VIRUSTOTAL HERE','ip':ip}
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
        
        printer = 'Message: '+serials['verbose_msg']+' '+ip+'\n'
        
        try:
            printer += 'Network: '+serials['network']+'\n'   
        except:
            pass
        try:
            printer += 'Continent: '+serials['continent']+'\n'
               
        except:
            pass
        try:
            printer += 'Country: '+str(serials['country'])+'\n'
            
        except:
            pass
        try:
            printer += '*******************WHOIS LOOKUP***********************\n'+serials['whois']+\
                '\n*******************WHOIS END***********************************\n'
        except:
            pass
        try:
            printer += 'ASN: '+str(serials['asn'])+'\n'
                
        except:
            pass
        try:
            printer += 'Owner: '+serials['as_owner']+'\n'+'undetected_urls: '
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
        time.sleep(16)
		
