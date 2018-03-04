#geektechstuff
#!/bin/python3

#import required libraries
import json,turtle,urllib.request,time

#opens JSON file containing ISS crew information
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#opens JSON file containing ISS location information
url2 = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())

#prints information on who is on the ISS
print('People in space:', result['number'])
people = result['people']
for p in people:
    print(p['name'],"in",p['craft'])

#collects information from location JSON
location = result2['iss_position']
lat = location['latitude']
lat = float(lat)
lon = location['longitude']
lon = float(lon)
print('ISS current location:')
print('Latitude:',lat)
print('Longitude:',lon)

#shows a map of planet Earth
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

#creates a Turtle for ISS
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

#set location for ISS turtle
iss.penup()
iss.goto(lon, lat)

#set marker location for Manchester, UK
lat_man = 53.483959
lon_man = -2.244644
location_man = turtle.Turtle()
location_man.penup()
location_man.color('yellow')
location_man.goto(lon_man,lat_man)
location_man.dot(5)
location_man.hideturtle()

#when will ISS pass over Manchester, UK
url_man = 'http://api.open-notify.org/iss-pass.json?lat=53.48&lon=-2.244'
response_man = urllib.request.urlopen(url_man)
result_man = json.loads(response_man.read())
over_man = result_man['response'][1]['risetime']

#print on map when ISS will pass over Manchester, UK
style = ('Arial',6,'bold')
location_man.write(time.ctime(over_man),font=style)



