# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint:
    def __init__(self, name, LatLon):
        self.name = name
        self.lat = LatLon.lat
        self.lon = LatLon.lon

    def __str__(self):
        return f'Waypoint -> Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache:
    def __init__(self, difficulty, size, Waypoint):
        self.name = Waypoint.name
        self.difficulty = difficulty
        self.size = size
        self.lat = Waypoint.lat
        self.lon = Waypoint.lon

    def __str__(self):
        return f'Geocache -> Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}, Difficulty: {self.difficulty}, Size: {self.size}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
latlon1 = LatLon(41.70505, -121.51521)
waypoint = Waypoint("Catacombs", latlon1)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
latlon2 = LatLon(44.052137, -121.41556)
waypoint2 = Waypoint("Newberry Views", latlon2)
geocache = Geocache(1.5, 2, waypoint2)
# Print it--also make this print more nicely
print(geocache)
