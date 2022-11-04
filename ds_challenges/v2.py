def solution(inputString):
    if len(inputString) == 1:
        return True
    elif len(inputString) > 1:
        i = len(inputString) - 1
        build_string = ""
        while i >= 0:
            build_string += inputString[i]
            i -= 1
        return build_string == inputString

def better_solution(inputString):
    return inputString == inputString[::-1]

if __name__ == '__main__':
    print(better_solution("aabaa"))