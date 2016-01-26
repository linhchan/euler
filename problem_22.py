"""
https://projecteuler.net/problem=22
The answer is 871198282
"""
import string

file = 'names.txt'
def dict_alpha():
    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
    	values[letter] = index + 1
    return values

def name_list():
    list_name = []
    with open(file, 'r') as f:
        for line in f:
            for word in line.split('","'):
                list_name.append(word)
    return sorted(list_name)

def sum_name(name):
    sum = 0
    for each in name:
        sum += dict_alpha()[each]
    return sum

def get_score(name):
    return sum_name(name) * (name_list().index(name) + 1)

def main():
    sum = 0
    for each in name_list():
        sum += get_score(each)
    print sum

if __name__ == '__main__':
    main()