import math


def pounds_to_kg(pounds):
    return pounds * 0.453592


def get_mass_object(obj):
    if obj == 't':
        return 0.1
    elif obj == 'p':
        return 1.0
    elif obj == 'r':
        return 3.0
    elif obj == 'g':
        return 5.3
    elif obj == 'l':
        return 9.07
    else:
        return 0.0


def get_velocity_object(distance):
    return math.sqrt(9.8 * distance / 2)


def get_velocity_skater(mass_skater, mass_object, vel_object):
    return mass_object * vel_object / mass_skater
