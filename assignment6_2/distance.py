import math

def calculate_distance_between_points(point1, point2):
    distance = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return distance

def calculate_total_distance(point_list):
    tot_distance = 0.0
    for i in range(len(point_list)-1):
        distance = calculate_distance_between_points(point_list[i], point_list[i+1])
        tot_distance += distance
    return tot_distance


def main():
    lukulista = []
    print("Enter the coordinates in the format 'x,y'. Stop with an empty line.")
    x_y = input()
    while x_y != "":
        osat = x_y.split(",")
        if len(osat) == 2:
            x = float(osat[0])
            y = float(osat[1])
            lukulista.append([x, y])
        else:
            print("Enter the coordinates in the format 'x,y'.")
        x_y = input("Enter the coordinates:\n")
    if len(lukulista) < 2:
        print("Not enough data.")
    else:
        etaisyys = calculate_distance_between_points(lukulista[0], lukulista[-1])
        total_distance = calculate_total_distance(lukulista)
        print("The total distance going through all the points is {:.2f} units long.".format(total_distance))
        print("The straight line from the starting point to the end is {:.2f} units long.".format(etaisyys))

main()