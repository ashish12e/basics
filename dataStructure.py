my_dict = {'name':'Rose','age':24, 'gender':'Female'}

print('-----------my dict examples ----------------')
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for i in my_dict.items():
    print(i)
    print(f'keys is {i[0]} and value is {i[1]}')

multidimensional_dict = {
        'first_level': {
             'second_level_1': {
                     'third_level_1': 1,
                     'third_level_2': 2
               },
        'second_level_2': {
                    'third_level_3': 3,
                    'third_level_4': 4
                   }
              },
 'another_first_level': {
                'second_level_3': {
                             'third_level_5': 5,
                             'third_level_6': 6
                             },
              'second_level_4': {
                            'third_level_7': 7,
                            'third_level_8': 8
                    }
             }
        }

print('------------multidimentional dictionary-------------')
# for i in multidimensional_dict:
#     print(i, multidimensional_dict[i])

## first get first level keys and dict_values(second) as values 
## from dict_values get items and iterate over it
## do it untill you get the desired values
for first_level, first_level_values in multidimensional_dict.items():
    print(first_level, first_level_values)
    print('-'*30)
    for seocnd_level, seocnd_level_values in first_level_values.items():
        print(seocnd_level, first_level_values[seocnd_level])

lst = [1,2,3,4]
lst[0] = 5
print(lst[0])

# tup = (1,2,3,4)
# ## this assignment is not possible
# tup[0] = 5
# print(tup[0])

def greet(name= 'user'):
    print('Hello : ', name)
def greet_new(name= 'user'):
    return ('Hello : ', name)
print(greet('Ashish'))
print(greet_new('Prisha'))