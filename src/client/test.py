files = {0: 'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}

from pprint import pprint

text = {}
for x, val in files.items():
    for y in range(1,9):
        text[val + str(y)] = {'x': x, 'y':y-1}

pprint(text)