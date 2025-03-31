import math

from utils import time_to_str


class Earthquake:
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return (
            self.place == other.place and
            math.isclose(self.mag, other.mag) and
            math.isclose(self.longitude, other.longitude) and
            math.isclose(self.latitude, other.latitude) and
            self.time == other.time
        )

    def __str__(self):
        return (
            f'({self.mag:.2f}) {self.place:>40s} at {time_to_str(self.time)} '
            f'({self.longitude:8.3f},{self.latitude:7.3f})'
        )

    @classmethod
    def from_feature(cls, feature):
        return cls(
            feature['properties']['place'],
            feature['properties']['mag'],
            feature['geometry']['coordinates'][0],
            feature['geometry']['coordinates'][1],
            feature['properties']['time'] // 1000)


def quake_from_feature(f):
    return Earthquake.from_feature(f)
#     return Earthquake(
#         f['properties']['place'],
#         f['properties']['mag'],
#         f['geometry']['coordinates'][0],
#         f['geometry']['coordinates'][1],
#         f['properties']['time'] // 1000)


def read_quakes_from_file(file):
    quakes = []

    for line in file:
        mag, long, lat, time, place = line.strip().split(maxsplit=4)
        quakes.append(Earthquake(
            place, float(mag), float(long), float(lat), int(time)))

    return quakes


def filter_by_mag(quakes, low, high):
    return [q for q in quakes if low <= q.mag <= high]


def filter_by_place(quakes, word):
    return [q for q in quakes if word.lower() in q.place.lower()]
