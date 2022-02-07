import requests 

data = requests.get('https://dog.ceo/api/breeds/list/all').json()


for raza in data['message']:
    print(raza)
    if(len(data['message'][raza])>=1):
        for subraza in data['message'][raza]:
            print ("  -  "+ subraza)


print()
raza=input("Introduzca la raza a buscar: ")
dataImages = (requests.get(('https://dog.ceo/api/breed/hound/images').replace("hound", raza))).json()
for image in dataImages['message']:
    print(image)