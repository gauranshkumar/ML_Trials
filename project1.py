user = {'gauransh':9205768854,'sharwan':9868958402,'kiran':9968251108,           #User Database using dictionary
'hitesh':9013825255}
crdentials = {'gauransh':{'email':'gauranshk21@gmail.com','age':'16','phone':
    '9205768854'}
,'sharwan':{'email':'sharwank2001@gmail.com','age':'50','phone':'9868958402'},
'kiran':{'email':'kb.kiranbharti74@gmail.com','age':'43','phone':'9968251108'},  #User Database using dictionary
'hitesh':{'email':'hit.jag.2012@gmail.com','age':'22','phone':'9013825255'}}

inp = str(input('Enter Username : '))                                            #username input
if inp in user:                                                                  #checking wether user exist
    password_inp = int(input('Enter Password : '))                               #password input
    if password_inp == user[inp]:                                                #matching password with database
        print('Welcome to My Program ' + inp)
        print('Your Credentials are here : ')
        print('\nEmail : '+crdentials[inp]['email'])                             #prints emial from databse dictionary
        print('Age : '+crdentials[inp]['age'])                                   #prints age from databse dictionary
        print('Phone: '+crdentials[inp]['phone'])                                #prints phone from databse dictionary
    else:
        print('Password don\'t match')                                           #message if password entered is incorrect
        exit()                                                                   #exiting program after cheking

else:
    print('User doesn\'t exist')                                                 #message if user is not in database
