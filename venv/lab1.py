import requests
#Printing the version of request
print(requests.__version__)

google = requests.get("https://www.google.com")
#Printing the response from google (should be 200!)
print(google)

var = requests.get("https://raw.githubusercontent.com/Dan767/404Lab1/master/404Lab1.py")
print(var.content)