def compare_response(resp1, resp2):
    difference = {}
    if resp1["status code"] != resp2["status code"]:
        difference["status code"] = (resp1["status code"], resp2["status code"])
    if resp1["len"] != resp2["len"]:
        difference["len"] = (resp1["len"], resp2["len"])
    else:
        return "No difference found"
    return difference