
import math
import datetime

def getnormaldate(unixdate):
    timestamp=unixdate
    normal_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
    print("la valeur en date normal vaut",normal_dt.strftime("%Y-%m-%d %H:%M:%S")) 
    return normal_dt
#You have a millisecond-precise timestamp 
#so first divide it by 1000 then feed it to datetime.datetime.fromtimestamp() 
#for local timezone (or pass datetime.tzinfo of the target timezone as a second argument) or datetime.datetime.utcfromtimestamp() for UTC. Finally, use datetime.datetime.strftime() to turn it into a string of your desired format.








def Main():
    timestamp1 = "1523126888080"
    timestamp2 = "1594051724615"
    getnormaldate(timestamp1)
    getnormaldate(timestamp2)
   
   
    
if __name__=="__main__":
    Main()