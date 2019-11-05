import itertools
import sys
sys.stdin = open('input.txt', 'r')


def inning(idx):
    global score
    outs = 0
    play = ''
    while outs < 3:
        if arr[idx] == '0':
            outs += 1
        else:
            play += arr[idx]

        idx = (idx + 1) % 9

    if play not in dict_score:
        string = ''
        for i in range(len(play)):
            if play[i] == '1':
                string += '1'
            elif play[i] == '2':
                string += '10'
            elif play[i] == '3':
                string += '100'
            else:
                string += '1000'

        dict_score[play] = string[:-3].count('1')
        score += dict_score[play]

    else:
        score += dict_score[play]

    return idx


N = int(input())    # N 은 이닝 수
hits = [list(input().split()) for _ in range(N)]

orders = list(itertools.permutations(list(range(1, 9))))
max_score = 0
dict_score = {}
for order in orders:
    score = 0
    first = 0
    for n in range(N):
        arr = []
        for i in range(8):
            arr.append(hits[n][order[i]])
        arr.insert(3, hits[n][0])
        # print(arr)
        first = inning(first)
    if max_score < score:
        max_score = score

print(max_score)


