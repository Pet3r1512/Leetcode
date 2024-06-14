# Provide code blocks which:
# 1. Receive a String (S) and a positive integer (N) as Inputs
# 2. Reverse N letters from S as Output
# 3. Return Output'

inp = input("Enter string: ")
num = int(input("Enter number: "))

def solution(inp: str, num: int):
    if (num > len(inp)):
        return print("Number is larger than string's length")
    return print(inp[0: num][::-1])

solution(inp, num)