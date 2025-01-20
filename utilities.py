def greet(name='User'):
    return 'Welcome ', name

def even_filter(lst):
    return [i for i in lst if i % 3 == 0]

def odd_filter(lst):
    return [i for i in lst if i % 2 != 0]

def reverse_funct(str):
    return str[::-1]

def list_of_odd_even(lst):
    final_list = even_filter(lst) + odd_filter(lst)
    return final_list

