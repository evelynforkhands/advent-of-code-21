def parse_bracket_sequence(seq):
    stack = []
    score = 0
    for c in seq:
        if c not in penalties.keys():
            stack.append(c)
        else:
            curr = stack.pop()
            if curr in closing_brackets.keys():
                if closing_brackets[curr] == c:
                    continue
                else:
                    score += penalties[c]
                    break
    return score


def read_input():
    f = open('inputs/test.txt', 'r')
    return f.read().split('\n')[:-1]


closing_brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
penalties = {')': 3, '}': 1197, ']': 57, '>': 25137}


print(sum([parse_bracket_sequence(seq) for seq in read_input()]))
