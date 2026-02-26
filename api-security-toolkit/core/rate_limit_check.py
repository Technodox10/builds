
  
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


  