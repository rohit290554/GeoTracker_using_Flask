import flask
from flask import Flask

'''
from geopy.geocoders import Nominatim

app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# Initialize Nominatim API
def geotracker():
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Assign Latitude & Longitude
    Latitude = "26.4969"
    Longitude = "80.3246"

    # Displaying Latitude and Longitude
    print("Latitude: ", Latitude)
    print("Longitude: ", Longitude)

    # Get location with geocode
    location = geolocator.geocode(Latitude + "," + Longitude)
    print(type(location))
    # Display location
    print("\nLocation of the given Latitude and Longitude:")
    return str(location)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
'''

app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address

app.run(host="0.0.0.0", port=8080)