"""
Basic usage of RxPY
"""
import random
import re
import time

from colorama import init, Fore, Back, Style
from rx import of, operators as op, create


def basic_sample_1():
    """
    Basic usage of 'rx.create'
    :return:
    """

    def push_five_strings(observer, scheduler):
        print(scheduler)
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
        on_next=on_success,
        on_error=on_error,
        on_completed=on_complete,
    )


def basic_sample_2():
    """
    Simple form of an Observable using 'rx.of'
    :return:
    """
    source2 = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

    source2.subscribe(
        on_next=on_success,
        on_error=on_error,
        on_completed=on_complete,
    )


def basic_sample_3():
    """
    Use of operators
    :return:
    """

    def print_on_subscribe(word_len):
        on_success(word_len)

    of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        op.map(len),
        op.filter(lambda count: count >= 5)
    ).subscribe(print_on_subscribe)


def on_success(word):
    """
    :param word:
    :return:
    """
    return print(Fore.CYAN + "Received {0}".format(word))


def on_error(error):
    """
    :param error:
    :return:
    """
    return print(Fore.RED + "Error Occurred: {0}".format(error))


def on_complete():
    """
    :return:
    """
    return print(Fore.BLACK + Back.GREEN + Style.BRIGHT + "Done!")


if __name__ == '__main__':
    SELECTION = 'None'

    while not re.findall('[xX]', SELECTION):
        init(autoreset=True)
        SELECTION = input('Select sample to run [1,2,3] or Press X to exit: ')

        if SELECTION == '1':
            basic_sample_1()
            continue
        elif SELECTION == '2':
            basic_sample_2()
            continue
        elif SELECTION == '3':
            basic_sample_3()
            continue

    print('Bye!!')
