import random
import time
import memory_profiler as mp

print(f"Memory usage before: {round(mp.memory_usage()[0], 2)} MiB")

name = ["fiza", "iqra", "mehak", "nandni"]
majors = ["CS", "SE", "IT", "AI"]

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(name),
            "major": random.choice(majors)
        }
        result.append(person)

    return result

def people_generator(num_people):
   
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(name),
            "major": random.choice(majors)
        }
        yield person

   
# time1 = time.time()
# people = people_list(100000)
# time2 = time.time()

time1 = time.time()
people = people_generator(100000)
time2 = time.time()

print(f"Memory usage after list: {round(mp.memory_usage()[0], 2)} MiB")
print(f"time took {time2-time1:.4f} sec")

# def square(num):
#     """
#     Generators are Python's way of producing a sequence of values lazily — one at a time, on demand — instead of building the whole thing in memory upfront.
#     """
#     for i in num:
#         yield (i*i)

# gen = square([1,2,3,4,5])

# for i in gen:
#     print(next(gen))