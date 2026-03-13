import sys

input = sys.stdin.readline

while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0 and input_list[1] == 0 and input_list[2] == 0:
        break
        
    input_list.sort()
    
    if (input_list[0] ** 2 + input_list[1] ** 2) == input_list[2] ** 2:
        print("right")
    else:
        print("wrong")


