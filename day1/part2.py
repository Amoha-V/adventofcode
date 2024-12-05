from collections import Counter
with open("./day1/input.txt", "r") as fo:
    leftlist, rightlist = [], []
    
    for line in fo.readlines():
        leftlist.append(int(line.split()[0]))  # Append first column
        rightlist.append(int(line.split()[1]))  # Append second column
    
    # Sort both lists
    leftlist = sorted(leftlist)
    rightlist = sorted(rightlist)

    similarityscore=0
    freqofrightlist=Counter(rightlist)
    for i in leftlist:
        similarityscore+=i*freqofrightlist[i]
    print(similarityscore)
