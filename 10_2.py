def calculate_score(completion_seq):
    score = 0
    for c in completion_seq:
        score *= 5
        score += scores[c]
    return score


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
    if score > 0:
        return score
    else:
        completion = ''
        while len(stack) > 0:
            completion += closing_brackets[stack.pop()]
        return completion


def read_input():
    f = open('inputs/input 10.txt', 'r')
    return f.read().split('\n')[:-1]


closing_brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
penalties = {')': 3, '}': 1197, ']': 57, '>': 25137}
scores = {')': 1, ']': 2, '}': 3, '>': 4}

incomplete_seqs = [calculate_score(parse_bracket_sequence(seq)) for seq in read_input() if type(parse_bracket_sequence(seq)) == str]
incomplete_seqs.sort()

print(incomplete_seqs[int(len(incomplete_seqs)/2)])
