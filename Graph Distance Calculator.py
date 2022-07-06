while True:
    print("[Press 2 for 2D, Press 3 for 3D, Press 4 for 4D]")   # instructions for user
    d = int(input("Enter the graph type : "))  # d is for store the number of dimensions
    if d > 1:   # validation for d
        break
    print("Invalid Input. Please Try again\n")

coordinates = {}
i = 0  # for loop 1
t = 0  # for loop 2
x = 0
ii = 1
while i < (2 * d):  # loop 1 - for input coordinates
    if i % d == 0:
        print("\nPoint " + str(x + 1))
        print("===================" + "\n")
        x = x + 1
    if (i + 1) > d:
        ii = 1

    coordinates[i] = float(input("\nEnter X" + str(ii) + " coordinate : "))
    i = i + 1
    ii = ii + 1

p_length = 0
while t < d:    # loop 2 - for calculate the power of the length
    p_length = p_length + ((coordinates[t] - coordinates[t + d]) ** 2)
    t = t + 1

length = p_length ** 0.5    # calculate length
print("Distance between two points " + str(length))
