with open("data/day4.txt") as f:
# with open("data/test4.txt") as f:
    data = f.readlines()

def row_to_card(row):
    winning, my_numbers = row.split('|')
    winning = winning.split(':')[-1].strip().split()
    my_numbers = my_numbers.strip().split()
    return set(winning), set(my_numbers)

cards = [row_to_card(row) for row in data ]

my_wins = [winning.intersection(my_numbers) for winning, my_numbers in cards ]

win_sum = [1*2**(len(win)-1) for win in  my_wins if win]
print("part1",sum(win_sum))

assert(sum(win_sum) == 19135)
