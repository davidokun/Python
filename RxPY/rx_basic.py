"""
Basic usage of RxPY
"""
import random
import time

from colorama import Fore, init
from rx import of, operators as op, create


# Example 1
def push_five_strings(observer, scheduler):
    observer.on_next("Alpha")
    time.sleep(random.randint(5, 20) * 0.1)
    observer.on_next("Beta")
    time.sleep(random.randint(5, 20) * 0.1)
    observer.on_next("Gamma")
    time.sleep(random.randint(5, 20) * 0.1)
    observer.on_next("Delta")
    time.sleep(random.randint(5, 20) * 0.1)
    observer.on_next("Epsilon")
    time.sleep(random.randint(5, 20) * 0.1)
    observer.on_completed()


source1 = create(push_five_strings)

source1.subscribe(
    on_next=lambda i: print(Fore.YELLOW + "Received {0}".format(i)),
    on_error=lambda e: print(Fore.RED + "Error Occurred: {0}".format(e)),
    on_completed=lambda: print(Fore.GREEN + "Done!"),
)

init(autoreset=True)

# Example 2
source2 = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

source2.subscribe(
    on_next=lambda i: print("Received {0}".format(i)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!"),
)


# Example 3
def print_sucker(s):
    print(f'Received {s} sucker!!!')


of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    op.map(lambda word: len(word)),
    op.filter(lambda count: count >= 5)
).subscribe(print_sucker)
