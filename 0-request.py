import requests
import sys


try: 
    parameter=sys.argv[1]

except IndexError:
    raise

url="http://127.0.0.1:5000/files/"
files = {'media': open('test.png', 'rb')}
resp=requests.post(url, files=files)

#resp=requests.get("http://127.0.0.1:5000/{}".format(parameter))

print(resp.json())


# go  http://127.0.0.1:5000/docs
# alternative http://127.0.0.1:5000/redoc

