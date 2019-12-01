modules = open("data/day1_input.txt").readlines()
mass_modules = [int(m) for m in modules]


def compute_fuel(mass: int):
    """Read input module value and compute the fuel

    Parameters
    ----------
    mass : [int]
        The mass of each module

    Returns
    -------
    [int]
        Fuel for each module based on mass
        fuel = round(mass/3) - 2
    """
    return round(mass // 3) - 2


assert compute_fuel(12) == 2
assert compute_fuel(14) == 2
assert compute_fuel(1969) == 654
assert compute_fuel(100756) == 33583

fuel_counter_upper = sum(map(compute_fuel, mass_modules))
print(f"fuel_counter_upper {fuel_counter_upper}")


def compute_total_fuel(mass):
    """Read input module value and compute the Total fuel using recursion

    Parameters
    ----------
    mass : [int]
        The mass of each module

    Returns
    -------
    [int]
        Fuel for each module based on mass and the computation for fuel.
        total_fuel = (round(mass/3) - 2)  + (round(fuel1/3) - 2) + ...
    """
    module_fuel = compute_fuel(mass)
    total_fuel = [module_fuel]
    while compute_fuel(module_fuel) > 0:
        total_fuel.append(compute_fuel(module_fuel))
        module_fuel = compute_fuel(module_fuel)
    return sum(total_fuel)


assert compute_total_fuel(12) == 2
assert compute_total_fuel(14) == 2
assert compute_total_fuel(1969) == 966
assert compute_total_fuel(100756) == 50346
total_fuel_value = sum(map(compute_total_fuel, mass_modules))
print(f"total_fuel_value {total_fuel_value}")
