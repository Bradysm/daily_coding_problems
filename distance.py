
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

    print(points)

kth_closest_pair()