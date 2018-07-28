#-------------------------------------------------------------------------------
# Name:        ID-Password
# Purpose:
#
# Author:      SRCC
#
# Created:     13/06/2018
# Copyright:   (c) SRCC 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#user = {'gauransh':'loveyouto','kiran':'trythis','sharwan':'itisfun','hitesh':'open'}
from data import user
import sqlite3


id_inp = str(input("Enter the Input : "))
if id_inp in user:
    pass_inp = str(input("\nEnter password : "))
    if pass_inp == user[id_inp]:
        print('Welcome to program')

    else:
        print("Password don't match")

else:
    print("User doesn't exist")
    option = str(input("Do you want to register ? (y/n)"))
    if option == 'y':
        new_id = str(input('Enter the username : '))
        new_pass = str(input('Enter the Password : '))
        user.update({new_id:new_pass})
        print('Congratulations !!')

    else:
        exit(0)






