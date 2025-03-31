class Earthquake:
    """A class to represent an Earthquake."""
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time


def quake_from_feature(feature):
    pass


# NOTE: This function takes an already open file as input.  You *will not*
# be opening anything in this function.
def read_quakes_from_file(file):
    pass


def filter_by_mag(quakes, low, high):
    pass


def filter_by_place(quakes, word):
    pass
