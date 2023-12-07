sum = 0

with open('input') as fp:
    for line in fp:
        data = line.strip().split(':')
        win, num = data[1].split('|')
        arr_win = win.strip().split()
        arr_num = num.strip().split()

        actual = list(set(arr_num).intersection(arr_win))
        #print("\nactual: " + str(actual))
        #print(len(actual))
        count = len(actual)
        value = 0
        if count > 0:
            value = 1
            for x in range(count-1):
                value = value * 2
            #print("value: " + str(value))
            sum = sum + value
            #print("sum: " + str(sum))
            value = 0

print("part 1: " + str(sum))