import re, requests
def idor(url):
    try:
        match = re.search(r'(\d+)', url)
        if match > "10000000000" :
          return {"error":"id too large"}
           
        repl = str(int(match.group(0))+1)
        modified_url = url.replace(r'(\d+)',repl)
        r = requests.get(modified_url)
        if match:
            return {
        "test":  "idor ",
        "status code": str(r.status_code),
        "len": len(r.text)
        }
        else:
          return {
        "original id":match,
        "modified id": repl, 
        "test":  "idor",
        "error": "no numeric id ",
        "modfied_url": modified_url
        }
    except:
      return "No idor is applicable "
    finally:
       print("IDOR Script Ran Successful")


