# Lambda function hanya boleh memiliki satu expression tapi boleh memiliki beberapa parameter.

# lambda [parameter1,parameter2,...] : [expression]

angka1 = 4
angka2 = 8
add = lambda x, y: x + y
print(add(angka1, angka2))

while True: print(eval(input('> ')))