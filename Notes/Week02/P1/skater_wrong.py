from funcs import (
    pounds_to_kg, get_mass_object, get_velocity_object, get_velocity_skater)


def main():
    mass_skater = pounds_to_kg(int(input("How much do you weigh (pounds)? ")))
    distance = int(input("How far away is your professor (meters)? "))
    mass_obj = get_mass_object(input(
        "Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, "
        "(l)ight saber, or lawn (g)nome? "
    ))

    vel_obj = get_velocity_object(distance)
    vel_skater = get_velocity_skater(mass_skater, mass_obj, vel_obj)

    print("\nNice throw!", end=" ")

    if mass_obj <= 0.1:
        print("You're going to get an F!")
    elif mass_obj <= 1.0:
        print("Make sure your profesor is OK.")
    elif distance < 20:
        print("How far away is the hospital?")
    else:
        print("RIP professor.")

    print(f"Velocity of skater: {vel_skater:.5f} m/s")

    if vel_skater < 0.2:
        print("My grandmother skates faster than you!")
    elif vel_skater >= 1.0:
        print("Look out for that railing!!!")


if __name__ == '__main__':
    main()
