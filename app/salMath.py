import math

n = int(input())
dic = {}
for i in range(n):
    room = input()
    if(room in dic):
        dic[room][0] += 1
    else:
        dic[room] = [1,0]

    people_in_this_room = dic[room][0]
    difference = people_in_this_room - 2
    
    if difference < 0:
        difference = 0

    dic[room][1] +=int(math.factorial(people_in_this_room)/ (math.factorial(2) * math.factorial(difference)))
    print(dic[room][1])