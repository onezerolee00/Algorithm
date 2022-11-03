cnt = 0

def recursion(str, left, right):
    global cnt
    cnt += 1
    if(left >= right):
        return 1
    elif(str[left] != str[right]):
        return 0
    else:
        return recursion(str, left+1, right-1)

def isPalindrome(str):
    return recursion(str, 0, len(str)-1)

for _ in range(int(input())):
    input_str = input()
    print(isPalindrome(input_str), cnt)
    cnt = 0

"""
recursion 함수를 호출하여 left와 right에 해당하는 문자를 비교한다.
만약 left >= right면 문자열을 모두 검사했으며 팰린드롬이라는 뜻이므로 return 1
만약 s[left] != s[right]면 팰린드롬이 아니므로 return 0
이외에 경우에는 인덱스를 옮겨 재귀호출

문제에 주어진 알고리즘에 cnt만 추가했다.
global 사용법을 익힐 수 있는 문제.
"""