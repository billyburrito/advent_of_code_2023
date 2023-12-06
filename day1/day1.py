import re

sum = 0
sum2 = 0

map = {'one': 1,
       "two": 2,
       'three': 3,
       'four': 4,
       'five': 5,
       'six': 6,
       'seven': 7,
       'eight': 8,
       'nine': 9,
       }

with open('input') as fp:
    for line in fp:
        data =  re.search(r"\D*(\d).*", line).groups()
        data = data + re.search(r".*(\d)\D*", line).groups()
        
        sum = sum + int(''.join(data))
        
        data2 = re.search(r"(one|two|three|four|five|six|seven|eight|nine|\d)", line).groups()
        data2 = data2 + re.search(r".*(one|two|three|four|five|six|seven|eight|nine|\d).*$", line).groups()

        if len(data2[0]) != 1:
            out2 = str(map[data2[0]])
        else:
            out2 = str(data2[0])
        if len(data2[1]) != 1:
            out2 = out2 + str(map[data2[1]])
        else:
            out2 = out2 + str(data2[1])
                
        sum2 = sum2 + int(out2)



print("part 1: " + str(sum))
print("part 2: " + str(sum2))

