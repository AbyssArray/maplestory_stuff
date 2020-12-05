from itertools import combinations

nodestones = []
nodestones.append(123)
nodestones.append(134)
nodestones.append(125)
nodestones.append(124)
nodestones.append(146)
nodestones.append(214)
nodestones.append(214)
nodestones.append(234)
nodestones.append(234)
nodestones.append(246)
nodestones.append(214)
nodestones.append(315)
nodestones.append(314)
nodestones.append(346)
nodestones.append(316)
nodestones.append(356)
nodestones.append(416)
nodestones.append(413)
nodestones.append(415)
nodestones.append(436)
nodestones.append(523)
nodestones.append(524)
nodestones.append(512)
nodestones.append(523)
nodestones.append(526)
nodestones.append(625)
nodestones.append(614)
nodestones.append(615)

complexity = 4 # how many nodes per set
values = 6 # number of desired values (1,2,3,4,5,6)
results = []


####
# Creates every combination of nodes (no duplicates), then creates a new list of valid sets
####


# this method creates the list of all possible combinations, and removes duplicates
def comb(data):
    data = list(dict.fromkeys(data))
    print(f"Unique {len(data)} nodes")
    return list(combinations(data, complexity))


# this method creates the list of verified sets
def verify(node_list):
    for node_set in node_list:
        primaries = []
        secondaries = []
        tertiaries = []
        for node in node_set:
            primaries.append(int(str(node)[0]))
            secondaries.append(int(str(node)[1]))
            tertiaries.append(int(str(node)[2]))
        counts = []
        for i in range(values):
            counts.append(counting(primaries, secondaries, tertiaries, i+1))
        # adds to list if primaries are all different
        if len(set(primaries)) == 4:
            # print(f"{node_set} = {counts}")
            check = True
            for c in counts:
                if c != 2:
                    check = check & False
            if check:
                results.append(node_set)


# helper function to count the number of values
def counting(pri, sec, ter, n):
    if len(pri) != len(set(pri)):
        return 0
    else:
        return pri.count(n) + sec.count(n) + ter.count(n)


# main program
def main():
    print(f"Entering {len(nodestones)} nodes")
    nodes = comb(nodestones)
    verify(nodes)

    i = 1
    for r in results:
        print(i, r)
        i = i + 1


main()
