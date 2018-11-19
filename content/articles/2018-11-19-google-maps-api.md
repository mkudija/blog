Title: Get Coordinates from Google Maps API
date: 2018-11-19 06:00
updated: 2018-11-19 06:00
authors: Matthew Kudija
comments: true
slug: google-maps-api
tags: Google Maps API, python

<!-- PELICAN_BEGIN_SUMMARY -->

<p style="text-align:center;"><img src="{filename}/downloads/code/google-maps-api/googleMaps.png" width="100%" height="100%"></p>

The Google Maps Platform offers a number of APIs to get maps, routes, and places information. In this example, I will demonstrate how to get coordinates of an address using the Geocoding API.


<!-- PELICAN_END_SUMMARY -->

# Google Maps API

While access to the Google Maps APIs used to be free for small requests, since July 2018 you must provide billing information and register for an API key. Not to worry, for small requests this should still be free. 

First navigate to the [Google Maps Platform](https://cloud.google.com/maps-platform/) page and select "Get Started". Follow the steps to get your API key, something that will look like this: **`AIzaSyAqDsnMnOTAyNKXKt3HRuIvLTCctaFVCLQ`** (note this API key has been disabled, so you will need to provide your own). Save this API key in a `.txt` file for later use.

In the Google Cloud Platform dashboard you can see the APIs you have access to. To get the coordinates of an address we will use the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/start). If the Geocoding API is not show in your list of **In Use APIs** select it from **Unused APIs** and select "Enable". 

<p style="text-align:center;"><img src="{filename}/downloads/code/google-maps-api/APIs.png" width="100%" height="100%"></p>

As shown in the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/start), we can get information about an address by accessing a URL of the form: **`https://maps.googleapis.com/maps/api/geocode/json?address=1600+Pennsylvania+Ave,+Washington,+DC&key=YOUR_API_KEY`**

If you replace **`YOUR_API_KEY`** in the above with your actual API key and drop the URL in a browser you will get a result like this:

<p style="text-align:center;"><img src="{filename}/downloads/code/google-maps-api/APIresult.png" width="100%" height="100%"></p>

Scrolling down you'll notice that this contains the coordinates data we want. Great! Now we just need to automate getting this information with Python.

# Geocoding API with Python

Using the Python requests library we can quickly get the coordinates for multiple addresses. We can write a `get_lat_lng` function that constructs the URL given an address and the API key and returns the latitude and longitude. Note that we read the API key from a local file to keep it private.

The full [`google-maps-geocoding.py`]() script is below:
```python
def get_lat_lng(apiKey, address):
    """
    Returns the latitude and longitude of a location using the Google Maps Geocoding API. 
    API: https://developers.google.com/maps/documentation/geocoding/start
    
    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    address                 [str]

    # RETURN ------------------------------------------------------------------
    lat                     [float] 
    lng                     [float] 
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng


if __name__ == '__main__':
    # get key
    fname = '/Desktop/GoogleMapsAPIKey.txt'
    file  = open(fname, 'r')
    apiKey = file.read()

    # get coordinates 
    address = '1 Rocket Road, Hawthorne, CA'
    lat, lng = get_lat_lng(apiKey, address)
    print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(address,lat, lng))
```

Running this script produces the following output:

```console
$ python google-maps-api.py

1 Rocket Road, Hawthorne, CA Coordinates:
Latitude:  33.9206814°
Longitude: -118.3280263°
```


# Distance Matrix API with Python

Similarly, we can get information about the distance or drive time between locations using the [Google Maps Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/start). 


The full [`google-maps-distance.py`]() script is below:
```python
def get_drive_time(apiKey, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start

    
    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    drive_tim               [float] (minutes)
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'),
                   destination.replace(' ','+'),
                   apiKey
                  )
          )
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value']/60
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0
    return drive_time


if __name__ == '__main__':
    # get key
    fname = '/Users/matthewkudija/Desktop/GoogleMapsAPIKey.txt'
    file  = open(fname, 'r')
    apiKey = file.read()

    # get coordinates 
    origin = '1 Rocket Road, Hawthorne, CA'
    destination = '1 Rocket Road, McGregor, TX'
    drive_time = get_drive_time(apiKey, origin, destination)
    print('Origin:      {}\nDestination: {}\nDrive Time:  {} hr'.format(origin, destination, drive_time/60))
```

Running this script produces the following output:

```console
$ python google-maps-distance.py

Origin:      1 Rocket Road, Hawthorne, CA
Destination: 1 Rocket Road, McGregor, TX
Drive Time:  20.6625 hr
```

---

- *You can view the original [code and files](https://github.com/mkudija/blog/tree/master/content/downloads/code/google-maps-api).*

*Versions:*
```
Python      3.6.3
```