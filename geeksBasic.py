# print('type(-100)')

# #print functionalities

# ## Separator in print by dafult it is for end = '\n' 
# ## so it always prints to next line

# print('a')
# print('b')
# print('c')

# # to print on the same line with some separator
# print('a', sep=" ", end="-")
# print('b', sep=" ", end="-")
# print('c', sep=" ", end="")

# print('---------------------------------')
# print('a', sep="/", end="-")
# print('b', sep="/", end="-")
# print('c', sep="/", end="")

# print('---------------------------------')
# # arithmatic operation on boolean will give diffrent result
# # True == 1 and False == 0
# # Try performing logical withuse of logical AND/OR

# print(True + True)
# print(True + False)

# #typecasting 
# ## a string which holds only numbers or float no alphabets 
# ## can be typecasted to int()

# print(int(float(' 10.23')))
# b = int(float(' 10.23'))
# c = float('0.57')
# print(c)
# print(bool(b))  # true since any no -ve or +ve will return true
# print(bool(c))
# print(bool('ashish'))  #even string gives True
# ## only converting zero or 0.00  or bool(' ')will give false
# print(bool(''))

# print('----------------------------------------')
# ## string operation

# # print('Ashish'[start:end:skip index])
# print('Ashish')
# print('AshiSh'[::2])
# print('AshiSh'[:4:])

# print ('Ashish Dwivedi   '.strip())  # this removes spaces from start and end of str

# # title() Does Camel Casing while capitalize does first character
# print('ashish kumar dwivedi '.capitalize(), end='-')
# print('ashish kumar dwivedi'.title())

# print('-' * 30)
# print('ashish'.center(30,'_'))
# print('Data cleaning'.ljust(30, '*'))
# print('Data cleaning'.rjust(30, '*'))

# print('--' * 20)
# l = ' ashish'.strip()
# ##print(l + 'length is : ' len(l))

# ##Stripping removes leading and trailing whitespace from a string using strip(), lstrip(), or rstrip().
# print('ashish   a'.strip())
# print(' '.strip())

##python data structure 
print('python data structure'.center(50, '-'))
lst = ['Ashish', "prisha", 'anurag', 'Ankit']
numlist = [1, 6, 3,6, 8, 0,2]

print(lst)
# slst = sorted(lst)
# print(sorted(lst))
print(numlist.sort(reverse=True))
print(sorted(numlist))

## to find index on any element
print(lst.index('Ankit'))

## iterating any list in reverse order use range and give start position at len
## end position , step -1 means backward, -1 means till first occurance
print('--'*20)
for i in range(len(lst)-1,-1,-1):
    print(lst[i], sep='__', end=' ')

lst.append('ankur')
print(lst)

## extending means adding multiple values at one go
lst.extend(['value1', 'value2', 'Ankita'])
print(lst)

## creating multidimentional list
print('_' * 30)
multilist = [[i for i in range(1,4)] for j in range(3)]
print(multilist)
print([[i +j for i in range(1,4)] for j in range(3)])
print('-----------diifeence -----------')
print([[(j, i) for i in range(4)] for j in range(3)])

def tuple_in_list(m,n):

    x  = [[(j, i) for i in range(m)] for j in range(n)]
    return x

print('---------------using function---------------')
print(tuple_in_list(3, 3))

## list comprehensions 
### printing odd numbers from range
print([i for i in range(20) if i % 2 != 0])

### geeting matrix for even or odd 
def even_no_list(m, n, even=True):
    if even: 
        even_matrix = [[(j, i) for i in range(m) if i % 2 == 0] for j in range(n) if j % 2 == 0]
        return even_matrix
    else:
        odd_matrix = [[(j, i) for i in range(m) if i % 2 != 0] for j in range(n) if j % 2 != 0]
        return odd_matrix
print(even_no_list(5,5, False))

