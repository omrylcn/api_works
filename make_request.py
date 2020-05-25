import requests
import sys


try:    
    parameter=sys.argv[2]

except IndexError:
    print("Index error")
    
    

data={"name":"zeynep",
      "description":"mystery",
      "price":-1,
      "tax":-1}

expression=sys.argv[1]+"_"+sys.argv[2]

if sys.argv[1]=="get":
    resp=requests.get("http://127.0.0.1:5000/{}".format(expression))

else:
    resp=requests.post("http://127.0.0.1:5000/{}".format(expression),json=data)

print(resp.json())#print(type(resp.json()))

