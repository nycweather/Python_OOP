import time

# Let's create a function that returns a list of cubes
def make_list(num: int) -> int:
    result = []
    for i in range(num):
        result.append(i**3)
    return len(result)

start_time = time.time()
result = make_list(9999999)
end_time = time.time()

execution_time = end_time - start_time
rounded_execution_time = round(execution_time, 4)

# print(f"Result: {result}")
print(f"Execution Time: {rounded_execution_time} seconds")

# Now, let's try it with a generator
def make_list_gen(num: int)-> int:
    for i in range(num):
        yield i**3

start_time_gen = time.time()
result_gen = make_list_gen(9999999)
end_time_gen = time.time()

execution_time_gen = end_time_gen - start_time_gen
rounded_execution_time_gen = round(execution_time_gen, 4)

print(f"Generator execution Time: {rounded_execution_time_gen} seconds")