# Project 2 - Moonlander
#
# Name: Brian Jones

# show_welcome {{{1
def show_welcome():
    print(
        "\nWelcome aboard the Lunar Module Flight Simulator\n\n"
        "   To begin you must specify the LM's initial altitude\n"
        "   and fuel level.  To simulate the actual LM use\n"
        "   values of 1300 meters and 500 liters, respectively.\n\n"
        "   Good luck and may the force be with you!\n\n"
    )


# get_altitude {{{1
def get_altitude():
    alt = int(input(
        "Enter the initial altitude of the LM (in meters): "))

    while alt < 1 or alt > 9999:
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please "
              "try again\n")

        alt = int(input(
            "Enter the initial altitude of the LM (in meters): "))

    return alt


# get_fuel {{{1
def get_fuel():
    fuel = int(input(
        "Enter the initial amount of fuel on board the LM (in liters): "))

    while fuel < 1 or fuel > 9999:
        print("ERROR: Amount of fuel must be positive, please try again\n")
        fuel = int(input(
            "Enter the initial amount of fuel on board the LM (in liters): "))

    return fuel


# display_lm_state {{{1
def display_lm_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
    print("Elapsed Time: %4d s" % elapsed_time)
    print("        Fuel: %4d l" % fuel_amount)
    print("        Rate: %4d l/s" % fuel_rate)
    print("    Altitude: %7.2f m" % altitude)
    print("    Velocity: %7.2f m/s" % velocity)


# get_fuel_rate {{{1
def get_fuel_rate(current_fuel):
    rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, "
                     "9=max thrust): "))

    while rate < 0 or rate > 9:
        print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")

        rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant "
                         "velocity, 9=max thrust): "))

    if rate > current_fuel:
        return current_fuel
    else:
        return rate


# display_lm_landing_status {{{1
def display_lm_landing_status(velocity):
    if velocity >= -1:
        print("Status at landing - The eagle has landed!")
    elif velocity > -10:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")


# update_acceleration {{{1
def update_acceleration(gravity, fuel_rate):
    return gravity * (fuel_rate / 5.0 - 1.0)


# update_altitude {{{1
def update_altitude(altitude, velocity, acceleration):
    new_altitude = altitude + velocity + acceleration / 2

    if new_altitude < 0:
        return 0
    else:
        return new_altitude


# update_velocity {{{1
def update_velocity(velocity, acceleration):
    return velocity + acceleration


# update_fuel {{{1
def update_fuel(fuel, fuel_rate):
    return fuel - fuel_rate
