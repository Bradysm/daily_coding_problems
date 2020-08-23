
import re

comma_delimeter = r'\s*\,\s*'
axis_coordinate = r'(\-?\d+)'



def kth_closest_pair():
    input_points = input("Enter three dimensional points as (x, y, z): ")
    pattern = re.compile(r'{p}{c}{p}{c}{p}'.format(c=comma_delimeter, p=axis_coordinate))

    # finds all points and converts the string into an int
    try:
        points = [(int(p[0]), int(p[1]), int(p[2])) for p in pattern.findall(input_points)]
    except:
        print("error parsing input.")
        exit(1)

    print("\n", points)


def find_all_numbers():
    # create regex and then compile it into a regex object
    regex = r'[+-]?\d+'
    pattern = re.compile(regex)

    # ask for an input from  the user
    input_str = input("Enter a string with numbers: ")

    # find all numbers within the string using the regex
    print("\nALL NUMBERS WITHIN THE STRING:")
    for num in pattern.findall(input_str):
        print(num)

kth_closest_pair()