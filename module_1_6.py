my_dict = {'Valera': 1992, 'Stas': 2003, 'Gena': 2000, 'Igor': 1995}
print(my_dict)
print(my_dict.get('Gena'))
print(my_dict.get('Egor'))
my_dict.update({'Sasha': 1996, 'Fedot': 2002})
dict_f = my_dict.pop('Igor')
print(dict_f)
print(my_dict)
#2
my_set = {1,2,3,4,5,3,4,2,1, 'wow', 'hey', 'wow', (1,2,3), (3,2,4), True}
print(my_set)
my_set.update([11,'doll'])
my_set.discard('wow')
print(my_set)
# =D
