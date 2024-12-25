def multiplier(n):
    def multiply(x):
        return n * x
    return multiply

double = multiplier(2)  # Fungsi multiplier menghasilkan fungsi `multiply` dengan n = 2
triple = multiplier(3)  # Fungsi multiplier menghasilkan fungsi `multiply` dengan n = 3

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
