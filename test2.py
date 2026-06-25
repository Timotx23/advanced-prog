# NB1_11.py
from threading import Thread
from queue import Queue
from math import sqrt
import random 
import sys


class NotPrimeError(Exception):
    def __init__(self):
        # CHANGED: removed sys.exit()
        # WHY: an error class should only describe the error.
        # The game loop should decide whether to continue or exit.
        super().__init__("Number entered is not a prime number")


class UserWonError(Exception):
    def __init__(self, reason):
        # CHANGED: removed sys.exit()
        # WHY: this exception may happen inside a thread.
        # sys.exit() inside a thread only exits that thread, not the full game cleanly.
        super().__init__(f"User won due to bot having the issue: {reason}")


class GameEndedError(Exception):
    def __init__(self):
        # CHANGED: removed sys.exit()
        # WHY: the exception should signal the game ended.
        # Cleanup should happen in game_builder().
        super().__init__("user ended the game")


START = "start"
END = "end"


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


### Exercise 5 ###############################

def user_input(queue, inputs):

    i = int(inputs)

    if is_prime(i) == True:
        queue.put(i)
    else:
        raise NotPrimeError()


def bot_input(x):
    if x >= 1000:
        raise UserWonError("User number is too large for the bot range")

    for _ in range(5):
        random_number = random.randint(x, 1000)
        if is_prime(random_number) == True:
            return random_number


    raise UserWonError("Robot had too many attempts to produce a valid prime number")


def producer_worker(player_queue, system_queue):
    while True:
        getter = player_queue.get()

        if getter == END:
            system_queue.put(END)
            break

        try:
            bot_output = bot_input(getter)
            system_queue.put(bot_output)
        except UserWonError as error:
            system_queue.put(error)
            break

def game_builder():
    """
    This needs to get the user input and pass it to the consumer -> then it needs to pass that to the producer 
    create the Queue/ threads
    End said threads
    """

    ui = input("Enter the Commands: ")

    while ui != START:
        ui = input("Enter the Commands: ")

    input_Queue = Queue()
    system_queue = Queue()
    game_manager = Thread(target=producer_worker, args=(input_Queue, system_queue))
    game_manager.start()

    try:
        while True:
            inputs = input("Enter a prime number: ")
            if inputs == END:
                input_Queue.put(END)
                raise GameEndedError()
            try:
                user_input(input_Queue, inputs)
            except ValueError:
                print("Please enter a number or type 'end'.")
                continue

            except NotPrimeError as error:
                print(error)
                continue
            getter = system_queue.get()
            if getter == END:
                print("Game ended")
                break
            if isinstance(getter, UserWonError):
                print(getter)
                break
            print(f"Current bot number is: {getter}, enter a larger number")
    except GameEndedError as error:
        print(error)
    except KeyboardInterrupt:
        
        print("Ended game due to players action")
        input_Queue.put(END)
    finally:
        game_manager.join()


game_builder()
##############################################