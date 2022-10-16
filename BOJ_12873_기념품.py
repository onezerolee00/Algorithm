# import sys, math
#
# n = int(sys.stdin.readline())
#
# participants = list(range(1, n+1, 1))
# print(participants)
# level = 1
#
# while(len(participants)>1):
#     if(len(participants)>=int(math.pow(level, 3))):
#         participants.pop(int(math.pow(level, 3))-1)
#     else:
#         if(int(math.pow(level, 3))%len(participants)==0):
#             participants.pop()
#         else:
#             print(-(int(math.pow(level, 3)) % len(participants) + 1))
#             participants.pop(-(int(math.pow(level, 3))%len(participants)+1))
#     print(participants)
#     level += 1

# import sys, math
# from collections import deque
#
# n = int(sys.stdin.readline())
#
# participants = list(range(1, n+1, 1))
# participants = deque(participants)
#
# level = 1
#
# while(len(participants)>1):
#     if(len(participants)>=int(math.pow(level, 3))):
#         del participants[int(math.pow(level, 3))-1]
#         participants.rotate(-(int(math.pow(level, 3))-1))
#     else:
#         del participants[-(int(math.pow(level, 3)) % len(participants) + 1)]
#         participants.rotate(-(int(math.pow(level, 3)) % len(participants)))
#     level += 1
#
# print(participants.pop())

import sys, math
from collections import deque

n = int(sys.stdin.readline())

participants = list(range(1, n+1, 1))
participants = deque(participants)

level = 1

while(len(participants)>1):
    if(int(math.pow(level, 3)) % len(participants)==1):
        del participants[0]
    else:
        participants.rotate(-(int(math.pow(level, 3)) % len(participants)-1))
        del participants[0]

    level += 1

print(participants.pop())