import getpass
import os
import time
from os import path

class Information:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def timercount(self, number):
        while number:
            timer = '{:01d}'.format(number) 
            print(timer, end="\n") 
            time.sleep(1) 
            number -= 1
        os.system('cls||clear')

    def done(self, temporary):
        print("Done!")
        doagain = input("Do you want to continue? (y/n): ")
        if doagain == "y":
            print("Restarting...")
            f.timercount(3)
            f.mainfunction("temp")
        else:
            exit

    def check(self, searchtext):
        with open("database.db", "r") as readobj:
            for line in readobj:
                if searchtext in line:
                    return True
        return False

    def store(self, username, password):
        storeInfo.write(username + "\n" + password + "\n\n")
        storeInfo.close()
        f.done("temp")

    def login(self, username, password):
        username = input("Please put the username: ")
        password = getpass.getpass("Please put the password: ")
        userchecker = f.check(username)
        passchecker = f.check(password)
        if userchecker == True and passchecker == True:
            print("Logged in.")
            storeInfo.close()
            f.done("temp")
        else:
            print("You have entered wrong username or password.")
            print("Please try again.\n")
            f.login("temp", "temp")

    def mainfunction(self, placeholder):
        loopfunc = False
        while loopfunc == False:
            print("PYTHON LOGIN FORM")
            check = input("Register or Login? ")
            basedata = bool(path.exists("database.db"))
            if check == "register":
                if basedata == False:
                    loopfunc = True
                    storeInfo = open("database.db", "x")
                    f.store(input("Please put the username: "), getpass.getpass("Please put the password: "))
                elif basedata == True:
                    loopfunc = True
                    storeInfo = open("database.db", "a")
                    f.store(input("Please put the username: "), getpass.getpass("Please put the password: "))
            elif check == "login":
                loopfunc = True
                storeInfo = open("database.db", "r")
                f.login("temp", "temp")
            else:
                loopfunc = False
                print(check + " is not a valid command.")
                print("Restarting...")
                f.timercount(3)

storeInfo = "temp"
f = Information("temp", "temp")
f.mainfunction("temp")