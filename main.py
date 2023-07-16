from account import *
import os

def main():
    name = input('Please enter your name:   ')
    account_number = input('Please enter your account number:   ')

    filename =  'C:/Users/Kevin/Documents/GitHub/user_account/output.txt'
    text_file = TextFile(filename)
    text_file.create_file()
    text_file.write_text(name,account_number)
    text_file.close_file()

if __name__ == '__main__':
    main()