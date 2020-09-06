// File: DSC510 Assignment 10.pdf
// Name: Michael Gonzalez
// Date: 2/14/2019
// Course: DSC 510 - Introduction to Programming
// Desc: This program will connect via a get request of a chuck norris joke APi until they don't want to see anymore jokes. 
// Usage: This program will connect via a get request of a chuck norris joke APi until they don't want to see anymore jokes. 

import requests


welcome = input("Welcome to the C. N. Joke Program")

# requesting the joke and displaying the joke in pretty output 
def jokes():
    url = 'https://api.chucknorris.io/jokes/random'
    json_data = requests.get(url).json()
    formatted_data = json_data['value']
    print(formatted_data)

    question = input('Want to do another joke? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Good Bye!")
        exit()

# defining main function with while loop code to run the program
def main():
    while True:
        answer = input("Would you like to hear a joke? Please type y or n: ")
        if answer == 'y':
            try:
                jokes()
            except Exception:
                print("Sorry. The joke program is not working.")

        if answer == 'n':
            print("See you later!")
            exit()

main()