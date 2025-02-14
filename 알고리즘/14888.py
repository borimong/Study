from itertools import permutations

N = int(input())

numbers = list(map(int, input().split()))

operators = list(map(int, input().split()))

symbols = []
symbols += ['+'] * operators[0]
symbols += ['-'] * operators[1]
symbols += ['*'] * operators[2]
symbols += ['/'] * operators[3]

resultSymbols = list(set(permutations(symbols))) #중복순열로 형성된 값 
[]



def calculate(operators):
    result = numbers[0]
    for i in range(len(numbers) - 1): # operator 의 len 으로 하면 안됨
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '-':
            result -= numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '/':
            if(result < 0):
                convert = numbers[i + 1] * -1
                result //= convert
                result *= -1
            else: result //= numbers[i + 1]

    return result

answer = []

for operator in resultSymbols:
    answer.append(calculate(operator))

print(max(answer))
print(min(answer))