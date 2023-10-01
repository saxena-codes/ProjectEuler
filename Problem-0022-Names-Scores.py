"""
Problem 22 - Names Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from pathlib import Path
path = Path('Problem-0022-names.txt')
names_list = path.read_text()
#n_1000 = digits_1000.replace("\n", "")
names_list = names_list.replace('"','')
names_list = list(names_list.split(","))

#sorted list
names_list.sort()

def alphabatical_value(a):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp = characters.split(a)
    value = len(temp[0]) + 1
    return value

sum_name_scores = 0
name_position = 1
for value in names_list:

    name_score = 0

    word = list(value)
    alphabet_value = 0
    for alphabet in word:
        alphabet_value += alphabatical_value(alphabet)

    name_score = name_position * alphabet_value

    sum_name_scores += name_score
    name_position += 1

print("Answer:")
print(sum_name_scores)