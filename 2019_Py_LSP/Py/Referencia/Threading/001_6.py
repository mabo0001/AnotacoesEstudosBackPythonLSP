# %%
from time import perf_counter, sleep
from random import randint
from concurrent.futures import ThreadPoolExecutor, as_completed
# %%


def do_something(x):
    print(f'Sleeping {x} second...', end='')
    sleep(x)
    return f'end well in {x}...'


# %%

start = perf_counter()

with ThreadPoolExecutor() as executer:
    r = [randint(1, 9) for _ in range(10)]
    results = executer.map(do_something, r)

    for result in results:
        print(result)

finish = perf_counter()

print(f'Finishes in {round(finish - start, 2):0.2f} seconds...')
