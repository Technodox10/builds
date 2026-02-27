import argparse

from core.auth_checks import *
from core.idor_checks import idor
from core.rate_limit_check import rate_limit
from utils.response_diff import compare_response
parser = argparse.ArgumentParser(prog="API Security Toolkit", description="Performs an API Security Test")
parser.add_argument('--url', type=str,help="URL to test")
args = parser.parse_args()
no_auth = no_auth_checks(args.url)
fake_auth = auth_checks_with_fake_token(args.url)
with_tokens = auth_checks_with_token(args.url, "Bearer: 'rando'")
idorcheck = idor(args.url)
print("No Auth Checks: " + str(no_auth_checks(args.url)))
print("Auth Checks with fake tokens: " + str(auth_checks_with_fake_token(args.url)))

print("Auth Checks: " + str(auth_checks_with_token(args.url, "Bearer: 'rando'")))
print("IDOR Checks: " + str(idor(args.url)))

print("For no auth and fake auth: " + str(compare_response(no_auth, fake_auth)))
print("For fake auth and with token: " + str(compare_response(fake_auth, with_tokens)))
print("For no auth and with token: " + str(compare_response(no_auth, with_tokens)))
rate_limit(args.url)
parser.print_help()

