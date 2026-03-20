import time
import random
import fastmath

def python_sum_squares(numbers):
    return sum(x*x for x in numbers)

# Генерируем 10 миллионов случайных чисел
data = [random.randint(1, 1000) for _ in range(10_000_000)]

# Rust
start = time.time()
rust_result = fastmath.sum_squares(data)
rust_time = time.time() - start

# Python
start = time.time()
python_result = python_sum_squares(data)
python_time = time.time() - start

print(f"Rust:    {rust_time:.4f} сек, результат = {rust_result}")
print(f"Python:  {python_time:.4f} сек, результат = {python_result}")
print(f"Ускорение: {python_time/rust_time:.2f}x")