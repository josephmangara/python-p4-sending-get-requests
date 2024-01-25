import requests
import json

url = "https://rickandmortyapi.com/api/character//1,2,3,4,5,6,7,8,9,10,11,12,13"

response = requests.get(url)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))
print(response.text)


#simple fetch request
# url = "https://rick-and-morty-lyart-psi.vercel.app/"
# response = requests.get(url)
# print(response.text)
