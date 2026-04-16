# using match case

def status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server issue"
        case _:
            return "unknown status"        
print(status(1001))            



