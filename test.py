
import requests

helloworld = requests.get('http://127.0.0.1:5000/helloworld')

print(helloworld.json().json())