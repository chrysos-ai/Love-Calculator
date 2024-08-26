
def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    true = 'TRUE'
    love = 'LOVE'
    true_count = 0
    love_count = 0
    for letters in true:
        for char in name1:
            if letters == char:
                true_count += 1
        for char in name2:
            if letters == char:
                true_count += 1

    for letters in love:
        for char in name1:
            if letters == char:
                love_count += 1
        for char in name2:
            if letters == char:
                love_count += 1
    print(f'''
T = {name1.count('T') + name2.count('T')}
R = {name1.count('R') + name2.count('R')}
U = {name1.count('U') + name2.count('U')}
E = {name1.count('E') + name2.count('E')}
Total TRUE = {true_count}

L = {name1.count('L') + name2.count('L')}
O = {name1.count('O') + name2.count('O')}
V = {name1.count('V') + name2.count('V')}
E = {name1.count('E') + name2.count('E')}
Total LOVE = {love_count}
''')
    total_count = int(f'{true_count}{love_count}')

    print(f'total love score is: {total_count}')
calculate_love_score()