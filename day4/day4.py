sum = 0
idx = 0
tag = {}
sum2 = 0

with open('input') as fp:
    for line in fp:
        #print("==============================")
        #print("idx: " + str(idx))

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
            #print(" y is: " + str(y))
            for x in range(count):
                #print("  x is: " + str(x))
                z = idx + x + 1
                #print("  z is: " + str(z))
                if z in tag:
                    tag[z] = tag[z] + 1
                else:
                    tag[z] = 1
                #print("tag: " + str(tag))

        #print("actual: " + str(actual))
        #print("len: " + str(len(actual)))

        value = 0
        if count > 0:
            value = 1
            for x in range(count-1):
                value = value * 2
            #print("value: " + str(value))
            sum = sum + value
            #print("sum: " + str(sum))
            value = 0

        # increment
        idx = idx + 1

print("part 1: " + str(sum))
#print(tag)
for ent in tag.values():
    sum2 = sum2 + ent
print("part 2: " + str(sum2))
