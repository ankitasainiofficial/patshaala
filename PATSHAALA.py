'''
SOFTWARE NAME: PATSHAALA
VERSION: 1.0.1
DESCRIPTION: A tiny program to illustrate patterns in python.
DEVELOPER: Ankita Saini
LAST UPDATED: 15 Sept 2023
LICENSE: MIT Licence
LOCATION: Jammu, J&K, India

Copyright 2023 -  Ankita Saini

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

def sq(*a):
    print("Welcome to square pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguements
    if(count==0):
        for i in range(10):
            print()
            for j in range(10):
                print('*',end=" ")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val):
                print()
                for j in range(val):
                    print('*',end=" ")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10):
                print()
                for j in range(10):
                    print(val,end=" ")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1):
                print()
                for j in range(val1):
                    print(val2,end=" ")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2):
                    print(val1,end=" ")
        # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(val1):
                    print(val2,end=val3)
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2):
                    print(val1,end=val3)
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(val3):
                    print(val1,end=val2)
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    # when there are more than 3 arguements.
    else:
        print('Error: Invalid number of arguments, only 3 arguments are acceptabe at most.')

# sq()
# sq(23)
# sq('@')
# sq(23,23)
# sq(23,'#')
# sq('^',12)
# sq('sam','dam')
# sq(23,'sam','jam')
# sq(2,7,0)
# sq('sam',22,'dam')
# sq('sam','dam',15)
# sq('sam','cam','dam')
#sq(2,'dam','cam',33)

def rect(*a):
    print("Welcome to rectangle pattern function")
    count=0
    for i in a:
        count= count+1
    print(count)

    #default case without any arguements
    if(count==0):
        for i in range(20):
            print()
            for j in range(10):
                print('*',end=" ")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val):
                print()
                for j in range(val):
                    print('*',end=" ")
        # if it's not numeric it prints default pattern
        else:
            for i in range(20):
                print()
                for j in range(10):
                    print(val,end=" ")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            val1=int(val1)
            val2=int(val2)
            for i in range(val1):
                print()
                for j in range(val2):
                    print('*',end=" ")
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1):
                print()
                for j in range(val1):
                    print(val2,end=" ")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2):
                    print(val1,end=" ")
        # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
         # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only 2 argument can be numeric')
        # when 1 & 2 are numerics.
        elif(val1.isnumeric() and val2.isnumeric() and not(val3.isnumeric())):
            val1=int(val1)
            val2=int(val2)
            for i in range(val1):
                print()
                for j in range(val2):
                    print(val3,end=' ')
        # when 2 & 3 are numeric
        elif(not(val1.isnumeric()) and val2.isnumeric() and val3.isnumeric()):
            val2=int(val2)
            val3=int(val3)
            for i in range(val2):
                print()
                for j in range(val3):
                    print(val1,end=' ')   
        # when 3 & 1 are numeric
        elif(val1.isnumeric() and not (val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            val1=int(val1)
            for i in range(val3):
                print()
                for j in range(val1):
                    print(val2,end=' ')  
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 2 numeric and 1 string arguments are allowed')
    # case with 4 arguemnets
    elif(count==4):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        val4=str(a[3])
        # when all 4 arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric()):
            print('Error: Invalid Input. Only 2 argument can be numeric')
        # when 1&2 arguments are numeric.
        elif(val1.isnumeric() and val2.isnumeric() and not (val3.isnumeric()) and not (val4.isnumeric())):
            val1=int(val1)
            val2=int(val2)
            for i in range(val1):
                print()
                for j in range(val2):
                    print(val3,end=val4)
        # when 2&3 argumnets are numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric() and  val3.isnumeric() and not (val4.isnumeric())):
            val2=int(val2)
            val3=int(val3)
            for i in range(val2):
                print()
                for j in range(val3):
                    print(val4,end=val1)
        # when 3&4 argumnets are numeric.
        elif(not(val1.isnumeric()) and  not (val2.isnumeric()) and  val3.isnumeric() and val4.isnumeric()):
            val3=int(val3)
            val4=int(val4)
            for i in range(val3):
                print()
                for j in range(val4):
                            print(val1,end=val2)
        # when 4&1 argumnets are numeric.
        elif(val1.isnumeric() and not(val2.isnumeric()) and not (val3.isnumeric()) and val4.isnumeric()):
            val4=int(val4)
            val1=int(val1)
            for i in range(val4):
                print()
                for j in range(val1):
                    print(val2,end=val3)
        # when all 4 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 2 numeric and 2 string arguments are allowed')
    # when there are more than 4 arguements.
    else:
        print('Error: Invalid number of arguments, only 4 arguments are acceptabe at most.')
                       
#rect()
#rect(3)
#rect('sam')
#rect(5,10)
#rect(4,'sam')
#rect('sam',2)
#rect('sam','dam')
#rect(3,12,0)
#rect(2,5,'%')
#rect('$',2,9)
#rect(13,'^',3)
#rect('sam','dam','cam')
#rect(2,4,6,12)
#rect(10,1,'sam','dam')
#rect('sam',2,12,'dam')
#rect("sam","dam",2,6)
#rect(3,'*','dam',2)
#rect(3,12,6,7,6)

def tri(*a):
    print("Welcome to right angle triangle pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10):
            print()
            for j in range(i+1):
                print('*',end=" ")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val):
                print()
                for j in range(i+1):
                    print('*',end=" ")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10):
                print()
                for j in range(i+1):
                    print(val,end=" ")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1):
                print()
                for j in range(i+1):
                    print(val2,end=" ")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(i+1):
                    print(val1,end=" ")
        # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
#case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(i+1):
                    print(val2,end=val3)
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(i+1):
                    print(val1,end=val3)
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    # when there are more than 3 arguements.
    else:
        print('Error: Invalid number of arguments, only 3 arguments are acceptabe at most.')


#tri()
#tri(5)
#tri("sam")
#tri(5,2)
#tri(5,'sam')
#tri('sam',5)
#tri('sam','dam')
#tri(3,7,3)
#tri(5,"*","%")
#tri('sam',6,'sam')
#tri('sam','dam',8)
#tri("sam",'dam','cam')
#tri(3,4,5,2)

def rtri(*a):
    print("Welcome to reverse right angle triangle pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10,0,-1):
            print()
            for j in range(i):
                print('*',end=" ")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val,0,-1):
                print()
                for j in range(i):
                    print('*',end=" ")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10,0,-1):
                print()
                for j in range(i):
                    print(val,end=" ")
        # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1,0,-1):
                print()
                for j in range(i):
                    print(val2,end=" ")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2,0,-1):
                print()
                for j in range(i):
                    print(val1,end=" ")
        # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1,0,-1):
                print()
                for j in range(i):
                    print(val2,end=val3)
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2,0,-1):
                print()
                for j in range(i):
                    print(val1,end=val3)
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3,0,-1):
                print()
                for j in range(i):
                    print(val1,end=val2)
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    # when there are more than 3 arguements.
    else:
        print('Error: Invalid number of arguments, only 3 arguments are acceptabe at most.')

#rtri()
#rtri(4)
#rtri('sam')
#rtri(3,4)
#rtri(4,'sam')
#rtri('dam',6)
#rtri('sam','dam')
#rtri(5,6,2)
#rtri(3,'*','sam')
#rtri('*',7,'dam')
#rtri('%','cam',2)
#rtri('sam','dam','cam')
#rtri(5,12,4,6)

def arr(*a):
    print("Welcome to arrow pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10+1):
            print()
            for j in range(i+1):
                print('*',end=" ")
        for a in range(10,0,-1):
            print()
            for b in range(a):
                print('*',end=" ")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val+1):
                print()
                for j in range(i+1):
                    print('*',end=" ")
            for a in range(val,0,-1):
                print()
                for b in range(a):
                    print('*',end=" ")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10+1):
                print()
                for j in range(i+1):
                    print(val1,end=" ")
            for a in range(10,0,-1):
                print()
                for b in range(a):
                    print(val1,end=" ")
     # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1+1):
                print()
                for j in range(i+1):
                    print(val2,end=" ")
            for a in range(val1,0,-1):
                print()
                for b in range(a):
                    print(val2,end=" ")
         # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2+1):
                print()
                for j in range(i+1):
                    print(val1,end=" ")
            for a in range(val2,0,-1):
                print()
                for b in range(a):
                    print(val1,end=" ")
        # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)  
            for i in range(val1+1):
                print()
                for j in range(i+1):
                    print(val2,end=val3)
            for a in range(val1,0,-1):
                print()
                for b in range(a):
                    print('*',end=" ")  
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2+1):
                print()
                for j in range(i+1):
                    print(val1,end=val3)
            for a in range(val2,0,-1):
                print()
                for b in range(a):
                    print("*",end=" ")
        #when arguement 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val3,0,-1):
                print()
                for b in range(a):
                    print("*",end=" ")
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 3 string arguments are allowed')
    #case with 4 arguements
    elif(count==4):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        val4=str(a[3])
        # when all 4 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 3 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())and not (val4.isnumeric())):
            val1=int(val1)
            for i in range(val1+1):
                print()
                for j in range(i+1):
                    print(val2,end=val3)
            for a in range(val1,0,-1):
                print()
                for b in range(a):
                    print(val4,end=" ")
        # when argument 2 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())and not (val4.isnumeric())):
            val2=int(val2)
            for i in range(val2+1):
                print()
                for j in range(i+1):
                    print(val1,end=val3)
            for a in range(val2,0,-1):
                print()
                for b in range(a):
                    print(val4,end=" ")
        #when arguement 3 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and val3.isnumeric() and not (val4.isnumeric())):
            val3=int(val3)
            for i in range(val3+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val3,0,-1):
                print()
                for b in range(a):
                    print(val4,end=" ")
        #when arguement 4 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and val4.isnumeric()):
            val4=int(val4)
            for i in range(val4+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val4,0,-1):
                print()
                for b in range(a):
                    print(val3,end=" ")
        # when all 4 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 3 string arguments are allowed')
    #case with 5 arguements
    elif(count==5):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        val4=str(a[3])
        val5=str(a[4])
        # when all 5 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric() and val5.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 4 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())and not (val4.isnumeric())and not (val5.isnumeric())):
            val1=int(val1)
            for i in range(val1+1):
                print()
                for j in range(i+1):
                    print(val2,end=val3)
            for a in range(val1,0,-1):
                print()
                for b in range(a):
                    print(val4,end=val5)
        # when argument 2 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())and not (val4.isnumeric()) and not (val5.isnumeric())):
            val2=int(val2)
            for i in range(val2+1):
                print()
                for j in range(i+1):
                    print(val1,end=val3)
            for a in range(val2,0,-1):
                print()
                for b in range(a):
                    print(val4,end=val5)
        #when arguement 3 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and val3.isnumeric() and not (val4.isnumeric()) and not (val5.isnumeric())):
            val3=int(val3)
            for i in range(val3+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val3,0,-1):
                print()
                for b in range(a):
                    print(val4,end=val5)
        #when arguement 4 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and val4.isnumeric() and not (val5.isnumeric())):
            val4=int(val4)
            for i in range(val4+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val4,0,-1):
                print()
                for b in range(a):
                    print(val3,end=val5)
        #when arguement 5 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and not (val4.isnumeric()) and val5.isnumeric()):
            val5=int(val5)
            for i in range(val5+1):
                print()
                for j in range(i+1):
                    print(val1,end=val2)
            for a in range(val5,0,-1):
                print()
                for b in range(a):
                    print(val3,end=val4)
        # when all 4 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 4 string arguments are allowed')

    # when there are more than 5 arguements.
    else:
        print('Error: Invalid number of arguments, only 5 arguments are acceptabe at most.')

#arr()
#arr(12)
#arr('sam')
#arr(5,2)
#arr(5,'sam')
#arr('sam',5)
#arr('sam','dam')
#arr(3,7,3)
#arr(5,"*","%")
#arr('sam',6,'sam')
#arr('sam','dam',8)
#arr("sam",'dam','cam')
#arr(12,3,4,6)
#arr(6,"*",'sam',"%")
#arr('dam',12,'*','#')
#arr("sam",'dam',6,"*")
#arr("sam",'dam','cam',8)
#arr('sam','dam','cam','pam')
#arr(12,3,4,6,5)
#arr(6,"*",'sam',"%",'pam')
#arr('dam',12,'*','#','pam')
#arr("sam",'dam',6,"*",'pam')
#arr("sam",'dam','cam',8,'pam')
#arr('sam','dam','cam','pam','pam')
#arr(3,4,5,2,12,2)

def etri(*a):
    print("Welcome to equilateral triangle pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10):
            print()
            for j in range(10,0,-1):
                if(i>=j):
                    print('*',end=" ")
                else:
                    print(" ",end="")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val):
                print()
                for j in range(val,0,-1):
                    if(i>=j):
                        print('*',end=" ")
                    else:
                        print(" ",end="")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10):
                print()
                for j in range(10,0,-1):
                    if(i>=j):
                        print(val,end=" ")
                    else:
                        print(" ",end="")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=" ")
                    else:
                        print(" ",end="")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=" ")
                    else:
                        print(" ",end="")
            # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val1,end=val2)
                    else:
                        print(" ",end="")
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    # when there are more than 3 arguements.
    else:
        print('Error: Invalid number of arguments, only 3 arguments are acceptabe at most.')

#etri()
#etri(5)
#etri("sam")
#etri(5,2)
#etri(5,'sam')
#etri('sam',5)
#etri('sam','dam')
#etri(3,7,3)
#etri(5,"*","%")
#etri('sam',6,'sam')
#etri('sam','dam',8)
#etri("sam",'dam','cam')
#etri(3,4,5,2)

def ertri(*a):
    print("Welcome to equilateral reverse triangle pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10,0,-1):
            print()
            for j in range(10,0,-1):
                if(i>=j):
                    print('*',end=" ")
                else:
                    print(" ",end="")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val,0,-1):
                print()
                for j in range(val,0,-1):
                    if(i>=j):
                        print('*',end=" ")
                    else:
                        print(" ",end="")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10,0,-1):
                print()
                for j in range(10,0,-1):
                    if(i>=j):
                        print(val,end=" ")
                    else:
                        print(" ",end="")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=" ")
                    else:
                        print(" ",end="")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=" ")
                    else:
                        print(" ",end="")
            # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3,0,-1):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val1,end=val2)
                    else:
                        print(" ",end="")
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    # when there are more than 3 arguements.
    else:
        print('Error: Invalid number of arguments, only 3 arguments are acceptabe at most.')

#ertri()
#ertri(5)
#ertri("sam")
#ertri(5,2)
#ertri(5,'sam')
#ertri('sam',5)
#ertri('sam','dam')
#ertri(3,7,3)
#ertri(5,"*","%")
#ertri('sam',6,'sam')
#ertri('sam','dam',8)
#ertri("sam",'dam','cam')
#ertri(3,4,5,2)

def di(*a):
    print("Welcome to diamond pattern function")
    count=0
    for i in a:
        count = count+1
    print(count)

    # default case without any arguments
    if(count==0):
        for i in range(10):
            print()
            for j in range(10,0,-1):
                if(i>=j):
                    print('*',end=" ")
                else:
                    print(" ",end="")
        for i in range(10,0,-1):
            print()
            for j in range(10,0,-1):
                if(i>=j):
                    print('*',end=" ")
                else:
                    print(" ",end="")
    # case with only one arguement
    elif(count==1):
        val = str(a[0])
        # when the arguement given is numeric
        if(val.isnumeric()):
            val=int(val)
            for i in range(val):
                print()
                for j in range(val,0,-1):
                    if(i>=j):
                        print('*',end=" ")
                    else:
                        print(" ",end="")
            for i in range(val,0,-1):
                print()
                for j in range(val,0,-1):
                    if(i>=j):
                        print('*',end=" ")
                    else:
                        print(" ",end="")
        # if it's not numeric it prints default pattern
        else:
            for i in range(10):
                print()
                for j in range(10,0,-1):
                    if(i>=j):
                        print(val,end=" ")
                    else:
                        print(" ",end="")
            for i in range(10,0,-1):
                print()
                for j in range(10,0,-1):
                    if(i>=j):
                        print(val,end=" ")
                    else:
                        print(" ",end="")
    # case with 2 arguements
    elif(count==2):
        val1=str(a[0])
        val2=str(a[1])
        # when both the arguments are numeric
        if(val1.isnumeric() and val2.isnumeric()):
            print('Error: both arguments cant be numeric, only one numeric argument is allowed')
        # when argument 1 is numeric & argument 2 is not
        elif(val1.isnumeric() and not(val2.isnumeric())):
            val1 = int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=" ")
                    else:
                        print(" ",end="")
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=" ")
                    else:
                        print(" ",end="")
        # when argument 1 is non-numeric & argument2 is numeric.
        elif(not(val1.isnumeric()) and val2.isnumeric()):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=" ")
                    else:
                        print(" ",end="")
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=" ")
                    else:
                        print(" ",end="")
            # when both the arguments are non-numeric
        else:
            print('Error: invalid argument types')
    #case with 3 arguements
    elif(count==3):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        # when all 3 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 2 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
        # when argument 2 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
        # when argument 3 is numeric and other 2 are not
        elif(not(val1.isnumeric()) and not(val2.isnumeric()) and val3.isnumeric()):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val1,end=val2)
                    else:
                        print(" ",end="")
            for i in range(val3,0,-1):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val1,end=val2)
                    else:
                        print(" ",end="")
        # when all 3 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 2 string arguments are allowed')
    #case with 4 arguements
    elif(count==4):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        val4=str(a[3])
        # when all 4 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 3 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())and not (val4.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val4,end=" ")
                    else:
                        print(" ",end="")
        # when argument 2 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())and not (val4.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val4,end=" ")
                    else:
                        print(" ",end="")
        #when arguement 3 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and val3.isnumeric() and not (val4.isnumeric())):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val2,end=val1)
                    else:
                        print(" ",end="")
            for i in range(val3,0,-1):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val4,end=" ")
                    else:
                        print(" ",end="")
        #when arguement 4 is numeric and other 3 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and val4.isnumeric()):
            val4=int(val4)
            for i in range(val1):
                print()
                for j in range(val4,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val4,0,-1):
                print()
                for j in range(val4,0,-1):
                    if(i>=j):
                        print(val1,end=" ")
                    else:
                        print(" ",end="")
        # when all 4 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 3 string arguments are allowed')
    #case with 5 arguements
    elif(count==5):
        val1=str(a[0])
        val2=str(a[1])
        val3=str(a[2])
        val4=str(a[3])
        val5=str(a[4])
        # when all 5 of arguments are numeric
        if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric() and val5.isnumeric()):
            print('Error: Invalid Input. Only one argument can be numeric')
        # when argument1 is numeric and other 4 are not
        elif(val1.isnumeric() and not(val2.isnumeric()) and not(val3.isnumeric())and not (val4.isnumeric())and not (val5.isnumeric())):
            val1=int(val1)
            for i in range(val1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val1,0,-1):
                print()
                for j in range(val1,0,-1):
                    if(i>=j):
                        print(val4,end=val5)
                    else:
                        print(" ",end="")
        # when argument 2 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and val2.isnumeric() and not(val3.isnumeric())and not (val4.isnumeric()) and not (val5.isnumeric())):
            val2=int(val2)
            for i in range(val2):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val1,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val2,0,-1):
                print()
                for j in range(val2,0,-1):
                    if(i>=j):
                        print(val4,end=val5)
                    else:
                        print(" ",end="")
        #when arguement 3 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and val3.isnumeric() and not (val4.isnumeric()) and not (val5.isnumeric())):
            val3=int(val3)
            for i in range(val3):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val2,end=val1)
                    else:
                        print(" ",end="")
            for i in range(val3,0,-1):
                print()
                for j in range(val3,0,-1):
                    if(i>=j):
                        print(val4,end=val5)
                    else:
                        print(" ",end="")
        #when arguement 4 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and val4.isnumeric() and not (val5.isnumeric())):
            val4=int(val4)
            for i in range(val4):
                print()
                for j in range(val4,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val4,0,-1):
                print()
                for j in range(val4,0,-1):
                    if(i>=j):
                        print(val1,end=val5)
                    else:
                        print(" ",end="")
        #when arguement 5 is numeric and other 4 are not
        elif(not(val1.isnumeric()) and not (val2.isnumeric()) and not  (val3.isnumeric()) and not (val4.isnumeric()) and val5.isnumeric()):
            val5=int(val5)
            for i in range(val5):
                print()
                for j in range(val5,0,-1):
                    if(i>=j):
                        print(val2,end=val3)
                    else:
                        print(" ",end="")
            for i in range(val5,0,-1):
                print()
                for j in range(val5,0,-1):
                    if(i>=j):
                        print(val4,end=val1)
                    else:
                        print(" ",end="")
        # when all 4 arguements are non-numeric
        else:
            print('Error: invaid argument types. atmost 1 numeric and 4 string arguments are allowed')
    # when there are more than 5 arguements.
    else:
        print('Error: Invalid number of arguments, only 5 arguments are acceptabe at most.')
                
#di()
#di(12)
#di('sam')
#di(5,2)
#di(5,'sam')
#di('sam',5)
#di('sam','dam')
#di(3,7,3)
#di(5,"*","%")
#di('sam',6,'sam')
#di('sam','dam',8)
#di("sam",'dam','cam')
#di(12,3,4,6)
#di(6,"*",'sam',"%")
#di('dam',12,'*','#')
#di("sam",'dam',6,"*")
#di("sam",'dam','cam',8)
#di('sam','dam','cam','pam')
#di(12,3,4,6,5)
#di(6,"*",'sam',"%",'pam')
#di('dam',12,'*','#','pam')
#di("sam",'dam',6,"*",'pam')
#di("sam",'dam','cam',8,'pam')
#di('sam','dam','cam','pam','pam')
#di(3,4,5,2,12,2)


def help():
    print("welcome to help function")
    a = input("Enter a choice:\n1 for Square Patern help\n2 for Rectangle Pattern help\n3 for Right Angle Triangle Pattern help\n4 for Reverse Right Angle Triangle help\n5 for Arrow Pattern help\n6 for Equivlateral Triangle Pattern help\n7 for Reverse Equivlateral Triangle Pattern help\n8 for Diamond Pattern help\n0 to exit\n-->\t")

    if(a=='0'):
        print('thanks for using help menu of patterns module')
    elif(a=='1'):
        print('\n\nWelcome to square pattern help section ***\n\n')
        print('Defaut option gives a 10x10 square pattern\nCalling function with custome size will print a custom pattern\n calling function with custom size and symbol gives us a custom square pattern\n calling function with custom size, symbol and ending gives us a custom square pattern\n')
    elif(a=='2'):
        print('\n\nWelcome to rectangle pattern help section ***\n\n')
        print('Defaut option gives a 20x10 rectangle pattern\nCalling function with custome size will print a custom pattern\n calling function with custom length and breadth will print a custom rectangle pattern\n calling function with custom size, length and breadth and symbol gives us a custom rectangle pattern\n calling function with custom size,length and breadth, symbol and ending gives us a custom rectangle pattern\n')
    elif(a=='3'):
        print('\n\nWelcome to right angle triangle pattern help section ***\n\n')
        print('Defaut option gives a 10 right angle triangle pattern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom right angle triangle pattern\n calling function with custom size, symbol and ending gives us a custom right angle triangle pattern\n')
    elif(a=='4'):
        print('\n\nWelcome to reverse right angle triangle pattern help section ***\n\n')
        print('Defaut option gives a 10 reverse right angle triangle pattern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom reverse right angle triangle pattern\n calling function with custom size, symbol and ending gives us a custom reverse right angle triangle pattern\n')
    elif(a=='5'):
        print('\n\nWelcome to arrow pattern help section ***\n\n')
        print('Defaut option gives a 10 size arrow pattern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom arrow pattern\n calling function with custom size, symbol and ending gives us a custom arrow pattern\n calling function with custom size, symbol, ending and symbol gives us a custom arrow pattern\n calling function with custom size, symbol, ending, symbol and ending gives us a custom arrow pattern\n')
    elif(a=='6'):
        print('\n\nWelcome to equilateral triangle pattern help section ***\n\n')
        print('Defaut option gives a 10 size equilateral triangle pattern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom equilateral triangle pattern\n calling function with custom size, symbol and ending gives us a custom equilateral triangle pattern\n') 
    elif(a=='7'):
        print('\n\nWelcome to reverse equilateral triangle pattern help section ***\n\n')
        print('Defaut option gives a 10 size reverse equilateral triangle patstern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom reverse equilateral triangle pattern\n calling function with custom size, symbol and ending gives us a custom reverse equilateral triangle pattern\n') 
    elif(a=='8'):
        print('\n\nWelcome to diamond pattern help section ***\n\n')
        print('Defaut option gives a 10 size diamond pattern\nCalling function with custom size will print a custom pattern\n calling function with custom size and symbol gives us a custom diamond pattern\n calling function with custom size, symbol and ending gives us a custom daimond pattern\n calling function with custom size, symbol, ending and symbol gives us a custom diamond pattern\n calling function with custom size, symbol, ending, symbol and ending gives us a custom diamond pattern\n')    


mainmenuchoice = '1'

while(mainmenuchoice!='0'):
    
    mainmenuchoice = input("Enter a choice for main menu:\n1 for Square Patern\n2 for Rectangle Pattern\n3 for Right Angle Triangle Pattern\n4 for Reverse Right Angle Triangle\n5 for Arrow Pattern\n6 for Equivlateral Triangle Pattern\n7 for Reverse Equivlateral Triangle Pattern\n8 for Diamond Pattern\nhelp for help menu\n0 to exit\n-->\t")
    
    if(mainmenuchoice=='1'):
        print("Welcome to Square pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10x10 pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")

        if(submenuchoice == '1'):
            sq()
        elif(submenuchoice == '2'):

            size = input('Enter size of square pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                sq(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of square pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of square pattern:\t')
                sq(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of square pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of square pattern:\t')
                ending = input('Enter ending of square pattern:\t')
                sq(size,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='help'):
            help()
        else:
            print('error:invalid choice')
    

    elif(mainmenuchoice=='2'):
        print("Welcome to rectangle pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 20x10 pattern\n2 for custom sized length of the pattern \n3 for custom sized lenhth and breadth of pattern\n4 for custom size, length , breadth  and symbol\n5 for custom size length, breadth ,symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            rect()
        elif(submenuchoice == '2'):

            size = input('Enter size of rectangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                rect(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            l = input('Enter the length for rectangle pattern:\t')
            if(l.isnumeric()):
                l=int(l)
            b = input('enter the breadth for rectangle pattern:\t')
            if(b.isnumeric()):
                b=int(b)
                rect(l,b)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='4'):
            l = input('Enter the length for rectangle pattern:\t')
            if(l.isnumeric()):
                l=int(l)
            b = input('enter the breadth for rectangle pattern:\t')
            if(b.isnumeric()):
                b=int(b)
                symbol = input('Enter symbol of rectangle pattern:\t')
                rect(l,b,symbol)
        elif(submenuchoice== '5'):
            l = input('Enter the length for rectangle pattern:\t')
            if(l.isnumeric()):
                l=int(l)
            b = input('enter the breadth for rectangle pattern:\t')
            if(b.isnumeric()):
                b=int(b)            
                symbol = input('Enter symbol of recatngle pattern:\t')
                ending = input('Enter ending of rectangle pattern:\t')
                rect(l,b,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        else:
            print('error:invalid choice')


    elif(mainmenuchoice=='3'):
        print("Welcome to right angle triangle pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            tri()
        elif(submenuchoice == '2'):

            size = input('Enter size of right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                tri(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of right angle triangle pattern:\t')
                tri(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of right angle triangle pattern:\t')
                ending = input('Enter ending of right angle triangle pattern:\t')
                tri(size,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='help'):
            help()
        else:
            print('error:invalid choice')

    elif(mainmenuchoice=='4'):
        print("Welcome to reverse right angle triangle pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            rtri()
        elif(submenuchoice == '2'):
            size = input('Enter size of reverse right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                rtri(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of reverse right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of reverse right angle triangle pattern:\t')
                rtri(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of reverse right angle triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of reverse right angle triangle pattern:\t')
                ending = input('Enter ending of reverse right angle triangle pattern:\t')
                rtri(size,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        else:
            print('error:invalid choice')

    elif(mainmenuchoice=='5'):
        print("Welcome to arrow pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\n5 for custom size, symbol ,ending symbol and symbol\n6 for custom size,symbol, ending symbol, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            arr()
        elif(submenuchoice == '2'):
            size = input('Enter size of arrow pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                arr(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of arrow pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of arrow pattern:\t')
                arr(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of arrow pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of arrow pattern:\t')
                ending = input('Enter ending of arrow pattern:\t')
                arr(size,symbol,ending)
        elif(submenuchoice== '5'):
            size = input('Enter size of arrow pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of arrow pattern:\t')
                ending = input('Enter ending of arrow pattern:\t')
                symbol2 = input('Enter symbol of arrow pattern:\t')
                arr(size,symbol,ending,symbol2)
        elif(submenuchoice== '6'):
            size = input('Enter size of arrow pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of arrow pattern:\t')
                ending = input('Enter ending of  arrow pattern:\t')
                symbol2 = input('Enter symbol 2 of arrow pattern:\t')
                ending2 = input('Enter ending 2 of  arrow pattern:\t')
                arr(size,symbol,ending,symbol2,ending2)
            else:
                print('Error: invalid size input, only numeric value allowd')
        else:
            print('error:invalid choice')

    elif(mainmenuchoice=='6'):
        print("Welcome to equivalent triangle pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):    
            etri()
        elif(submenuchoice == '2'):

            size = input('Enter size of equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                etri(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of right angle triangle pattern:\t')
                etri(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of equivalent triangle pattern:\t')
                ending = input('Enter ending of equivalent triangle pattern:\t')
                etri(size,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        else:
            print('error:invalid choice')

    elif(mainmenuchoice=='7'):
        print("Welcome to reverse equivalent triangle pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            ertri()
        elif(submenuchoice == '2'):
            size = input('Enter size of reverse equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                ertri(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of reverse equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of reverse equivalent triangle pattern:\t')
                ertri(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of reverse equivalent triangle pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of reverse equivalent triangle pattern:\t')
                ending = input('Enter ending of reverse equivalent triangle pattern:\t')
                ertri(size,symbol,ending)
            else:
                print('Error: invalid size input, only numeric value allowd')
        else:
            print('error:invalid choice')


    elif(mainmenuchoice=='8'):
        print("Welcome to diamond pattern menu -->\n\n")
        submenuchoice = input("Enter a choice:\n1 for default 10 size pattern\n2 for custom sized pattern\n3 for custom size and symbol\n4 for custom size, symbol and ending symbol\n5 for custom size, symbol ,ending symbol and symbol\n6 for custom size,symbol, ending symbol, symbol and ending symbol\nhelp for help\n0 to back menu\nexit to exit program:\n-->\t")


        if(submenuchoice == '1'):
            di()
        elif(submenuchoice == '2'):
            size = input('Enter size of diamond pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                di(size)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice=='3'):
            size = input('Enter size of diamond pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of diamond pattern:\t')
                di(size,symbol)
            else:
                print('Error: invalid size input, only numeric value allowd')
        elif(submenuchoice== '4'):
            size = input('Enter size of diamond pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of diamond pattern:\t')
                ending = input('Enter ending of diamond pattern:\t')
                di(size,symbol,ending)
        elif(submenuchoice== '5'):
            size = input('Enter size of diamond pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of diamond pattern:\t')
                ending = input('Enter ending of diamond pattern:\t')
                symbol2 = input('Enter symbol of diamond pattern:\t')
                di(size,symbol,ending,symbol2)
        elif(submenuchoice== '6'):
            size = input('Enter size of diamond pattern:\t')
            if(size.isnumeric()):
                size=int(size)
                symbol = input('Enter symbol of diamond pattern:\t')
                ending = input('Enter ending of  diamond pattern:\t')
                symbol2 = input('Enter symbol of diamond pattern:\t')
                ending2 = input('Enter ending of  diamond pattern:\t')
                di(size,symbol,ending,symbol2,ending2)
            else:
                print('Error: invalid size input, only numeric value allowd')

        else:
            print('Error: Invalid Choice for Sub Menu')
    
    elif(mainmenuchoice=='help'):
        help()
    elif(mainmenuchoice=='0'):
        print('Thanks for using Pattern Module for Python.\n\nCopyright 2023 - Ankita')
    else:
        print('error:invalid choice')