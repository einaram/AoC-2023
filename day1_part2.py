# %%
import re
with open("data/day1.txt") as f:
# with open("data/day1_test2.txt") as f:
    data = f.readlines()

NUMBERS = {   
'one':1,
'two':2, 
'three':3,
 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':'9',
 '1':1,'2':2,'3':3,'4':4,'5':5,'6':6, '7':7,'8':8,'9':9

}


# %%
def find_all_occurrences(main_string, patterns):
    occurrences = {}
    for pattern in patterns:
        occurrences[pattern] = [m.start() for m in re.finditer(pattern, main_string)]
    min_idx = min([min(x) for x in occurrences.values()if x])
    max_idx = max([max(x) for x in occurrences.values() if x])

    first = NUMBERS.get([x for x in occurrences.keys() if min_idx in occurrences[x]][0])
    last = NUMBERS.get([x for x in occurrences.keys() if max_idx in occurrences[x]][0])

    return int(f'{first}{last}')


print(sum([find_all_occurrences(x,NUMBERS.keys() ) for x in data]))
    

