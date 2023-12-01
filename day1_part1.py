# %%
import re


# with open("data/day1.txt") as f:
with open("data/day1_test2.txt") as f:
    data = f.readlines()


numbers = {
    
'one':1,
'two':2, 
'three':3,
 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
}

for number_str, number  in numbers.items():
    data = [x.replace(number_str, str(number)) for x in data]
print(data)

lines = []

digits = [re.findall('\d',x) for x in data]

res= [[int(x[0]+x[-1])] for x in digits]
print(res)
summed = sum([sum(x) for x in res])
print(summed)
# %%
