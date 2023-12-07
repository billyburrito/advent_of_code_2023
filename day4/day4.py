sum = 0
idx = 0
tag = {}
sum2 = 0

with open('input') as fp:
    for line in fp:

        data = line.strip().split(':')
        win, num = data[1].split('|')
        arr_win = win.strip().split()
        arr_num = num.strip().split()

        if not idx in tag:
            tag[idx] = 1
        else:
            tag[idx] = tag[idx] + 1

        # for loop here for mult tickets, 
        # we will go through at least once for all lines
        actual = list(set(arr_num).intersection(arr_win))
        count = len(actual)
        for y in range(tag[idx]):
            for x in range(count):
                z = idx + x + 1
                if z in tag:
                    tag[z] = tag[z] + 1
                else:
                    tag[z] = 1

        value = 0
        if count > 0:
            value = 1
            for x in range(count-1):
                value = value * 2
            sum = sum + value
            value = 0

        # increment
        idx = idx + 1

print("part 1: " + str(sum))
for ent in tag.values():
    sum2 = sum2 + ent
print("part 2: " + str(sum2))
