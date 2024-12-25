message = 'Hello from global!'
def modify_variable():
    message = 'Hello from local!'
    print(message)
modify_variable()
print(message)