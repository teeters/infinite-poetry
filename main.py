from poetry import *
from word_processing import *
from time import sleep
import os

def say(msg, delay=.02):
    for c in msg:
        print(c, end="", flush=True)
        sleep(delay)
    print()

def intro():
    say("Hello! Wecome to the free infinite poetry generator.")

def get_seeds():
    say("Enter a space-separated list of words to use as seeds. Choose up to 6.")
    words = input()
    print()
    return words.split()[:7]

def get_advice():
    say("Enter any other advice for the poetry generator, on one line:")
    advice = input()
    print()
    return advice

def get_forced():
    return os.environ.get('FORCED_IMAGE')

def free_associate(seeds, p=True):
    word_cloud = ""
    for word in seeds:
        new_line = ", ".join(word_assoc(word))
        if p:
            say(new_line)
        word_cloud += new_line + '\n'
    print()
    return word_cloud

def should_break():
    acceptable_yes = ['yes', 'Yes', 'y', '']
    acceptable_no = ['no', 'No', 'n']
    say("Do you wish to continue?")
    answer = input()
    while (answer not in acceptable_yes) and (answer not in acceptable_no):
        say(f"Do you wish to continue? (Y/n)")
        answer = input()
    return (answer in acceptable_no)

def decay(poem, forced, age):
    return ablate_words(poem, forced, int(2*age))
    
def main():
    intro()
    age = 0

    while True:
        seeds = get_seeds()
        advice = get_advice()
        forced = get_forced()
        
        say("Free associating...\n")
        words = free_associate(seeds)

        say("Writing poem...\n")
        poem = get_poem(words, advice, forced)
        poem = decay(poem, forced, age)
        say(poem)
        print()

        if should_break():
            break
        else:
            print()
            age += 1
            continue
        
if __name__ == '__main__':
    main()
