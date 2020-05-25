import requests
import sys


try: 
    parameter=sys.argv[1]

except IndexError:
    raise


resp=requests.get("http://127.0.0.1:5000/{}".format(parameter))

print(resp.json())