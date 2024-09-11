import random
def clean_data(temp_list):
    """
        This function returns a list of temperature between 85 and 120 not inclusive.
    :param temp_list:
    :return: temp_list
    """
    for element in temp_list:
        if element < 85 or element > 120:
            temp_list.remove(element)
    return temp_list

def longest_heat_wave(temp_list):
    """
        This function returns the longest days in a row where temperature was above 100.
    :param temp_list:
    :return: longest_streak, heat_lisr
    """

    # Initialize the variables
    heat_list = []
    current_streak = 0
    longest_streak = 0

    # If the element of the list is above 100 and if it current streak is bigger than the longest streak.
    #   Updates the longest_streak counter
    # Otherwise sets the current streak to 0
    for element in temp_list:
        if element > 100:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                heat_list.append(element)
        else:
            current_streak = 0
    return longest_streak, heat_list

def longest_cold_wave(temp_list):
    cold_list = []
    current_streak = 0
    longest_streak = 0

    # If the element of the list is less 32 and if it current streak is bigger than the longest streak.
    #   Updates the longest_streak counter
    # Otherwise sets the current streak to 0
    for element in temp_list:
        if element < 32:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                cold_list.append(element)
        else:
            current_streak = 0

    return longest_streak, cold_list

def main():

    weather_temp = []
    for i in range(1, 366):
        rand = round(random.uniform(-40.0, 130.0), 2)
        weather_temp.append(rand)

    cleaned_temps = clean_data(weather_temp)
    heat_streak, heat_list = longest_heat_wave(cleaned_temps)
    cold_streak, cold_list = longest_cold_wave(cleaned_temps)

    print(f"The longest heat streak in Arizona was {heat_streak} days. \n\tTemperatures: {heat_list}")
    print(f"The longest cold streak in Arizona was {cold_streak} days. \n\tTemperatures: {cold_list}")


main()