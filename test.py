import requests
url="http://localhost:5000/predict"
data={"features":[1.2,3.5,5.3,4.8]}
response=requests.post(url,json=data)
print(response.json())