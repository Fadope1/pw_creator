# tool for creating strong passwords
# Made by Fabian - Fadop3 08.12.2020

import argparse # for parsing the arguements in command line
import string # for getting all the characters and numbers/ special characters
import random # for randomizing the password - most used module

parser = argparse.ArgumentParser(description="A tool for generating safe passwords - Made by Fabian(fadop3)")
parser.add_argument("-p", "--password", default=None, help="A base password/ word, which will be modified")
parser.add_argument("-l", "--length", choices=range(13,101), metavar="[13-100]", default=16, type=int, help="Max length of the Password")
parser.add_argument("-c", "--count", type=int, default=10, help="How many passwords you wanna create?")
#parser.parse_args(["-p", None, "-l", "16"])

#print(parser.parse_args().length)

numbers = string.digits # 1-9
alphabet = string.ascii_letters # including upper and lowercase, not including special chars like äöü...
special_chars = string.punctuation

chars = [numbers, alphabet, special_chars]

# print(numbers, alphabet, special_chars, sep="\n\n")

def create_pw(base_pw=parser.parse_args().password):
    pw_length = random.choice(range(12, parser.parse_args().length))
    #print(pw_length)
    pw = ""
    if not base_pw:
        # if no base pw/word is given -> create complete random one
        for i in range(pw_length):
            pw += random.choice(random.choice(chars))
        return pw
    # else make the given word/ password safe
    pw = random.choice(special_chars) + base_pw
    for i in range(random.choice(range(3, parser.parse_args().length - len(base_pw)+1))):
        r = random.choice(random.choice(chars))
        pw += r
    return pw

for x in range(parser.parse_args().count):
    print(x+1, create_pw())
