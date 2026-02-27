
'''
Pseudocode for rate limit 
goal: to check rate limiting on an endpoint
input: takes url rate limiting with auth and without auth
steps: 
 1. take url  
   a) with auth
   b) without auth
 2. Burst test
  send continous get requests for 3s
  store status code and response time
 3. medium test
 send continous get requests for 15s, store status code and response time
 4. stress test
  send continous get requests for 30s, store status code and response time 
Responses: 
 if statuscode is 429
  respond rate limiting present 
 elif statuscode 403/captcha
  request blocked   
 elif response time incresing 
  respond possible throlling
 else 
  respond rate limiting absent     
Output:
  number of responses till block and time trend 
  status codes 
  difference between auth and unauth
checklist:
429?
Retry-After?
Response delay?
Same token blocked?
New token works?
'''
#def ratelimit(url):
from datetime import datetime

import requests
import re

sec = datetime.now().time().second 
times = []
def status(stat):
 pattern = re.compile("[4^]")
 for (key, value) in iter(stat.items()): 
     if key == "status":
       if value == 429:
         print("Rate limit in place")
       elif pattern.search(str(value)):
          print("Unauthorised access ")   
       elif times[len(times)-1] > times[len(times)-2]:
         print("Possible Throttling")
       else:
          print("No rate limit")

      
def rate_limit(url):
    time_after_3sec = sec + 3
    time_after_15sec = sec + 15
    time_after_30sec = sec + 30
    stat_3 = {}
    stat_15 = {}
    stat_30 = {}
    for i in range(time_after_3sec):
      req = requests.get(url)
      time_elapsed = (req.elapsed.seconds * 1e+6) + req.elapsed.microseconds
      times.insert(i,time_elapsed)
      stat_3 = {
         "time" : i,
         "status": req.status_code,
         "elasped ": time_elapsed
      }
      status(stat_3)
      

    for j in range(time_after_15sec):
       req = requests.get(url)
       time_elapsed = (req.elapsed.seconds * 1e+6) + req.elapsed.microseconds 
       times.insert(i,time_elapsed)
       stat_15 = {
         "time" : j,
         "status": req.status_code,
         "elapsed": time_elapsed
      }
       status(stat_15)
    
    for k in range(time_after_30sec):
       req = requests.get(url)
       time_elapsed = (req.elapsed.seconds * 1e+6) + req.elapsed.microseconds
       times.insert(i,time_elapsed)
       stat_30 = {
         "time" : k,
         "status": req.status_code,
         "elapsed": time_elapsed
      }
       status(stat_30)
    
    
        

  