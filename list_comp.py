# coding: utf-8
import string
ls = [x for x in string.ascii_lowercase if string.ascii_lowercase.index(x) < 10]
print ls
new_ls = [lambda n: [n, n+n, n+n+n] for n in ls]
print new_ls
make_three = lambda n: [n, n+n, n+n+n]
new_ls = [make_three(n) for n in ls]
new_ls
add_two = lambda x, y: x + y
reduce(add_two, new_ls[])
reduce(add_two, new_ls[len(new_ls)])
reduce(add_two, new_ls[, 0])
reduce(add_two, new_ls[0, len(new_ls) - 1])
print len(new_ls)
reduce(add_two, new_ls)
print ls
list = reduce(add_two, [make_three_entries(x) for x in ls])
list = reduce(add_two, [make_three(x) for x in ls])
list
[new_ls[x][x%3] = new_ls[x][0].capitalize() for x in new_ls]
print new_ls
[[new_ls[x][x%3] = new_ls[x][0].capitalize()] for x in new_ls]
[[y[x%3].capitalize() for x in y] for y in new_ls]
list = [[y[x%3].capitalize() for x in y] for y in new_ls]
print lst
print list
print new_list
print new_ls
# i didn't get to the last part of part 1... might not get to finish it  over the weekend because i have three midterms next week.
