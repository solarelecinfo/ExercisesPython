
import math
import datetime
import re

def getnormaldate(unixdate):
    timestamp=unixdate
    normal_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
    print("la valeur en date normal vaut",normal_dt.strftime("%Y-%m-%d %H:%M:%S")) 
    return normal_dt
#You have a millisecond-precise timestamp 
#so first divide it by 1000 then feed it to datetime.datetime.fromtimestamp() 
#for local timezone (or pass datetime.tzinfo of the target timezone as a second argument) or datetime.datetime.utcfromtimestamp() for UTC. Finally, use datetime.datetime.strftime() to turn it into a string of your desired format.


def isUrlValid(url_string):
        result=False
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        result=re.match(regex, url_string)
        print("le url %s, est valid %s" % (url_string,result))
        return result
    
def isUrlValid2(url_string):
        result=False
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if(re.match(regex, url_string)):
           result=True
        else:
           result=False
        print("le url %s, est valid %s" % (url_string,result))
        return result

def isUrlValid3(url_string):
        result=False
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
     
        if(re.match(regex, url_string)):
            result=True
            print("URL correct")
        else:
            result=False
            print("URL format in correct_exception")
            raise ValueError
        return result








def Main():
    timestamp1 = "1523126888080"
    timestamp2 = "1594051724615"
    getnormaldate(timestamp1)
    getnormaldate(timestamp2)
    
    isUrlValid("http://www.example.com")
    isUrlValid("httwww.example.com")
    isUrlValid("http://www.example.com/")
    print ("\n \n -------")
    isUrlValid2("http://www.example.com")
    isUrlValid2("httwww.example.com")
    isUrlValid2("http:/Swww.example.com/")
    isUrlValid2("tt://streetsmart.parkeon.com/nexus/repository/binary/temp/terminal/low_level/streetsmart_v1/0.34.12.1/BSM-hardware-config/OTA/config-bsm/0.34.12.3-12082020_0913_dev_cashless/BSM-hardware-config.zip")
   
    try:
        if( isUrlValid2("http://www.example.com")):
            print("URL est valid")
        else:
            raise ValueError
    except ValueError:
        print("URL est INNNNNNNNNNvalid")
        return
   
   
  
    try:
        isUrlValid3(str("http://www.example.com"))
    except ValueError:
        print("ABORT EXECUTION")
        return
    
    try:
        isUrlValid3("http://www.example.com")
    except ValueError:
        print("ABORT EXECUTION")
        return

    isUrlValid3("http//www.example.com")
    try:
        isUrlValid3("http//www.example.com")
    except ValueError:
        print("ABORT EXECUTION")
        return
    
    
    
    
    print("fin program")
    
   

  
   
    
if __name__=="__main__":
    Main()