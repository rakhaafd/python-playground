counter = 0
def func():
    while True:
        global counter
        input(f"counter anda sekarang {counter}, ENTER untuk menambah")
        counter += 1
    
func()