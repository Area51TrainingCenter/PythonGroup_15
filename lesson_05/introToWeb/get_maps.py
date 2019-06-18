import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
address = 'area51 training center'
params = {
    'key': 'AIzaSyApQ5kfKn0c-ulrM0VFKasllA5WY7ZMNPg',
    'address': address
}
r = requests.get(url=url, params=params)
data = r.json()
print(data)

location = data['results'][0]['geometry']['location']
lat, long = location['lat'], location['lng']
print(lat, long)
