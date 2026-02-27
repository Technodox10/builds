
import requests


def no_auth_checks(url):
    r = requests.get(url)
    return {
        "test":  "no auth check",
        "status code": str(r.status_code),
        "len": len(r.text)
        }

def auth_checks_with_fake_token(url):
    header = {
        "Authorization":"Bearer 12345677"
    }
    r = requests.get(url, headers=header)
    return {
        "test":  "with fake auth ",
        "status code": str(r.status_code),
        "len": len(r.text)
        }

def auth_checks_with_token(url,token):  
    header = {
        "Authorization ": token
    }  
    r = requests.get(url, headers=header)
    return {
        "test":  " auth with token",
        "status code": str(r.status_code),
        "len": len(r.text)
        }
        