import re

arr_data = []

with open('sample4') as fp:
    for line in fp:
        arr_data.append(list(line.strip()))

num = ''
num_idx = []
min = 0
xmax = len(arr_data) - 1
ymax = len(arr_data[0]) - 1

hit = False

for idx, row in enumerate(arr_data):
    #print(idx,row)
    for idy, col in enumerate(row):
        #print(idy,col)
        
        
        if re.match(r"\d", arr_data[idx][idy]):
            print("num  pre: " + num)
            num = num + arr_data[idx][idy]
            print("num post: " + num)
            
            print(arr_data[idx][idy])
            # check for chars
            # NSEW
            if idx - 1 >= min:
                if not re.match(r"\d|\.", arr_data[idx-1][idy]):
                    hit = True
                    print(arr_data[idx-1][idy])
            if idx + 1 <= xmax:
                if not re.match(r"\d|\.", arr_data[idx+1][idy]):
                    hit = True
                    print(arr_data[idx+1][idy])
            if idy - 1 >= min:
                if not re.match(r"\d|\.", arr_data[idx][idy-1]):
                    hit = True
                    print(arr_data[idx][idy-1])
            if idy + 1 <= ymax:
                if not re.match(r"\d|\.", arr_data[idx][idy+1]):
                    hit = True
                    print(arr_data[idx][idy+1])
            # diags
            if idx - 1 >= min and idy - 1 >= min:
                if not re.match(r"\d|\.", arr_data[idx-1][idy-1]):
                    hit = True
                    print(arr_data[idx-1][idy-1])
            if idx + 1 <= xmax and idy + 1 <= ymax:
                if not re.match(r"\d|\.", arr_data[idx+1][idy+1]):
                    hit = True
                    print(arr_data[idx+1][idy+1])
            if idy - 1 >= min and idx + 1 <= xmax:
                if not re.match(r"\d|\.", arr_data[idx+1][idy-1]):
                    hit = True
                    print(arr_data[idx+1][idy-1])
            if idy + 1 <= ymax and idx - 1 >= min:
                if not re.match(r"\d|\.", arr_data[idx-1][idy+1]):
                    hit = True
                    print(arr_data[idx-1][idy+1])
            # fringe case that the number ends in the bottom corner
            if idx == xmax and idy == ymax:
                if num and hit:
                    print(num)
                    num_idx.append(int(num))
                num = ''
                hit = False
            # another fringe case where a number ends at the end of a line
            # elif idx == xmax:
            #     if num and hit:
            #         print(num)
            #         num_idx.append(int(num))
            #     num = ''
            #     hit = False
            
        else:
            if num and hit:
                print(num)
                num_idx.append(int(num))
            num = ''
            hit = False
            
        


print(num_idx)
print("part 1: " +  str(sum(num_idx)))