import argparse

import quake_funcs as qf
from utils import get_json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    return parser.parse_args()


def print_quakes(quakes):
    print('Earthquakes:')
    print('------------')
    for q in quakes:
        print(q)


def get_menu_choice():
    print('\nOptions:\n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit\n')
    return input('Choice: ').lower()


def sort_quakes(quakes):
    sort_type = input(
        'Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? '
    ).lower()

    if sort_type == 'm':
        quakes.sort(key=lambda q: q.mag, reverse=True)
    elif sort_type == 't':
        quakes.sort(key=lambda q: q.time, reverse=True)
    elif sort_type == 'l':
        quakes.sort(key=lambda q: q.longitude)
    elif sort_type == 'a':
        quakes.sort(key=lambda q: q.latitude)

    return quakes


def filter_quakes(quakes):
    filter_by = input('Filter by (m)agnitude or (p)lace? ').lower()

    if filter_by == 'm':
        lower = float(input('Lower bound: '))
        upper = float(input('Upper bound: '))

        return qf.filter_by_mag(quakes, lower, upper)

    if filter_by == 'p':
        place = input('Search for what string? ')

        return qf.filter_by_place(quakes, place)

    return quakes


def get_new_quakes(quakes):
    quakes_dict = get_json(
        'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/'
        '1.0_hour.geojson')

    has_new_quake = False

    for new_feature in quakes_dict['features']:
        new_quake = qf.quake_from_feature(new_feature)
        if new_quake not in quakes:
            quakes.append(new_quake)
            has_new_quake = True

    if has_new_quake:
        print('\nNew quakes found!!!')

    return quakes


def main():
    args = parse_args()

    with open(args.filename) as f:
        quakes = qf.read_quakes_from_file(f)

    print_quakes(quakes)

    while (choice := get_menu_choice()) != 'q':
        if choice == 's':
            quakes_to_print = sort_quakes(quakes)
        elif choice == 'f':
            quakes_to_print = filter_quakes(quakes)
        elif choice == 'n':
            quakes_to_print = get_new_quakes(quakes)

        print()
        print_quakes(quakes_to_print)

    with open(args.filename, 'w') as f:
        for q in quakes:
            print(q.mag, q.longitude, q.latitude, q.time, q.place, file=f)


if __name__ == '__main__':
    main()
