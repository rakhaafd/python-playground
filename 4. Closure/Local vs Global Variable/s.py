def print_local ():
    global counter
    counter = 'ini counter'
    print('local variable: ', counter)

print_local()
print('global variable: ', counter)