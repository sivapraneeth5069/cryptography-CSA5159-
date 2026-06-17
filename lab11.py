import math
keys = math.factorial(25)
power2 = math.log2(keys)
unique_keys = keys // 2
unique_power2 = math.log2(unique_keys)
print("Total Possible Keys =", keys)
print("Approximate Power of 2 = 2^", round(power2, 2))
print("\nEffectively Unique Keys =", unique_keys)
print("Approximate Power of 2 = 2^", round(unique_power2, 2))