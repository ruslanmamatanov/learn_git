import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

numbers = [1, 2, 3]
x = numbers
c = numbers
print(ref_count(id(numbers)))
