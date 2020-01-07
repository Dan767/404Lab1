import requests
#Printing the version of request
print(requests.__version__)

google = requests.get("https://www.google.com")
#Printing the response from google (should be 200!)
print(google)