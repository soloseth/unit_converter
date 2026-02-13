conversions = {
    "kg_lbs": 2.20462,
    "lbs_kg": 0.453592,
    "oz_ml": 29.5735,
    "ml_oz": 1 / 29.5735,
    "m_ft": 3.28084,
    "ft_m": 1 / 3.28084,
}

time_in_seconds = {
    "S": 1,
    "MIN": 60,
    "H": 3600,
    "D": 86400,
    "W": 604800,
    "MO": 2629800,
    "YR": 31557600,
}

def convert(value, factor):
    return value  * factor

def convert_time(value, from_unit, to_unit):
    seconds = value * time_in_seconds[from_unit]
    return seconds / time_in_seconds[to_unit]


def main():
    while True:
        choice = input("\nConcert (M)ass, (V)olume, (L)ength, (T)ime or (Q)uit?: ").strip().upper()

        if choice == "Q":
            print("Goodbye!")
            break

        value = float(input("Enter value: "))

        if choice == "M":
            unit = input("Convert to (K)g of (L)bs?: ").strip().upper()
            if unit == "K":
                result = convert(value, conversions["kg_lbs"])
                print(f"{value} kg = {result:.2f} lbs")
            elif unit == "K":
                result = convert(value, conversions["lbs_kg"])
                print(f"{value} lbs = {result:.2f} kg")
            else:
                print("Invalid unit.")

        elif choice == "V":
            unit = input("Convert to (M)l or (O)z?: ").strip().upper()
            if unit == "M":
                result = convert(value, conversions["oz_ml"])
                print(f"{value} oz = {result:.2f} ml")
            elif unit == "O":
                result = convert(value, conversions["ml_oz"])
                print(f"{value} ml = {result:.2f} oz")
            else:
                print("Invalid unit.")

        elif choice == "L":
            unit = input("Convert to (M)eters or (F)eet?: ").strip().upper()
            if unit == "F":
                result = convert(value, conversions["m_ft"])
                print(f"{value} m = {result:.2f} ft")
            elif unit == "M":
                result = convert(value, conversions["ft_m"])
                print(f"{value} ft = {result:.2f} m")
            else:
                print("Invalid unit.")

        elif choice == "T":
            print("Convert to (S)econds, (MIN)utes, (H)ours, (D)ays, (W)eeks, (MO)nths or (YR) years?")
            from_unit = input("Convert from: ").strip().upper()
            to_unit = input("Convert to: ").strip().upper()

            if from_unit in time_in_seconds and to_unit in time_in_seconds:
                result = convert_time(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.4f} {to_unit}")
            else:
                print("Invalid time unit.")

        else:
            print("Invalid choice.")

if __name__ ==  "__main__":
    main()
