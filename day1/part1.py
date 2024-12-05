with open("./day1/input.txt", "r") as fo:
    leftlist, rightlist = [], []
    
    for line in fo.readlines():
        leftlist.append(int(line.split()[0]))  # Append first column
        rightlist.append(int(line.split()[1]))  # Append second column
    
    # Sort both lists
    leftlist = sorted(leftlist)
    rightlist = sorted(rightlist)
    
    # Calculate the sum of absolute differences
    diff = 0
    for i in range(len(leftlist)):
        diff += abs(leftlist[i] - rightlist[i])

print(diff)
