# Konsep function di dalam suatu function disebut nested function. Berbeda dengan function yang terletak di luar, ia dapat dengan bebas membaca variabel dari function induknya atau outer function.

def decorate(style = 'italic'):
    def italic (s):
        return '<i>' + s + '<i>'
    def bold (s):
        return '<b>' + s + '<b>'
    
    if style == 'italic':
        return italic
    else:
        return bold
    
dec = decorate()
print(dec('hello'))
dec2 = decorate('bold')
print(dec2('hello'))


def induk():
    print('hello dek')

def outer():
    return induk()

outer()