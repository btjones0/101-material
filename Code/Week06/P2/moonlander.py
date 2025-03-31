import lander_funcs


def main():
    lander_funcs.show_welcome()

    time = 0
    vel = 0
    rate = 0
    alt = lander_funcs.get_altitude()
    fuel = lander_funcs.get_fuel()

    print("\nLM state at retrorocket cutoff")

    while alt > 0:
        if fuel > 0:
            lander_funcs.display_lm_state(time, alt, vel, fuel, rate)
            print()
            rate = lander_funcs.get_fuel_rate(fuel)
            fuel = lander_funcs.update_fuel(fuel, rate)
        else:
            print("OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: "
                  "%7.2f" % (time, alt, vel))
            rate = 0

        time += 1
        accel = lander_funcs.update_acceleration(1.62, rate)
        alt = lander_funcs.update_altitude(alt, vel, accel)
        vel = lander_funcs.update_velocity(vel, accel)

    print("\nLM state at landing/impact")
    lander_funcs.display_lm_state(time, alt, vel, fuel, rate)
    print()
    lander_funcs.display_lm_landing_status(vel)


if __name__ == '__main__':
    main()
