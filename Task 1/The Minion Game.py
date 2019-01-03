def minion_game(string):
    vowels = 'AEIOU'
    l =  len(s)
    K = sum([l - i for i in range(l) if string[i] in vowels])
    S = sum([l - i for i in range(l) if string[i] not in vowels])
    if K > S:
        print('Kevin {}'.format(K))
    elif K < S:
        print('Stuart {}'.format(S))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)