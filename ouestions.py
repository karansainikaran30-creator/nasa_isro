# a program to input 2 numbers & print their sum

# a=int(input("enter a"))
# b=int(input("enter b"))

# print("sum :", (a+b) )

# WAP to input side of a square & print its area

# side = int(input("enter your side"))
# print(side**2)


#WAP to input 2 floating point numbers & print their average

# a=float(input("enter your first num."))
# b=float(input("enter your second num."))
# print("ave.:", (a+b)/2)


#WAP to input 2 int numbers a and b print true if a is gerater than or b if not print false

# a = int(input("enter a"))
# b = int(input("enter b"))
# print(a>=b)


#WAP to input user first name & print its length.

# str = input("enter string value")
# print(len(str))

#WAP to find the occurrence of '$' in a sting.

# str = "string"
# print(str.count("$"))

# name= input("enter")
# print(name.count("a"))


#WAP to ask the user to enter names of their 3 favorite movies & store than in a list
#1st
# list = input("enter your favorite 3 movies" )
# print(list)

#2nd
# movies = []
# mov1= input("enter your 1st mov.")
# mov2 = input("enter your 2nd movie")
# mov3 = input("enter your 3rd movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#WAP to chack if a list contains a palindrom of elements 

# list1 = [1,2,1]
# list2= [9,8,7]
# copylist1= list1.copy()
# copylist1.reverse()
# if(copylist1==list):
#   print("palindrom")
# else:
#     print("not palindron")
   
   
   
   
#WAP to count the number of students with the "A" grade in the following tuple.
#["c","D","A","B","B","A"]
# tup = ("c","D","A","B","B","A")
# count= tup.count("C")
# print(count)


#store the above values in a list& sort them from "A" to "D"

# list=["C","D","A","B","B","A"]
# sort=list.sort()
# print(sort)
# print(list)

# store following world meanings in a python dictionary 
    # table : "a piece of furniture","list of facts & figures"
    # cat : "a small animal"
# dict = {
#     "table" :["a piece of furniture","list of facts & figures" ],
#     "cat": "a small animal",
# }
# print(dict)

# you are given a list of subjects for students . assume one classroom is required for 1 subject. how mny classrooms are needed by all students.
   # "python","java","c++","python","javascript","java","python","java","c++","c"
# set={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
#     }
# print(set)
# print(len(set))

#print numbers from 1 to 100.
# i = 1
# while i<=100:
#     print(i)
#     i+=1
#print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i-=1
#print the multiplication table of a number n.
# i =1
# while i<=10:
#     print(i*3)
#     i+=1
# n = int(input("enter your number"))
# i =1
# while i<=10:
#  print(n*i)
#  i+=1
#print the elements of the following list using a loop
# nums = [ 1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

#search for a number x in this tuple using loop.
# nums = [ 1,4,9,16,25,36,49,64,81,100]
# nums = [ 1,4,9,16,25,36,49,64,81,100]
# x = 36
# indx = 0

# while indx < len(nums):
#     if(nums[indx] == x):
#         print("True",indx)
#     indx+=1

# nums = [ 1,4,9,16,25,36,49,64,81,100]
# x = 36
# indx = 0

# while indx < len(nums):
#     if(nums[indx] == x):
#         print("True",indx)
#     else:
#         print("false")
#     indx+=1

#for loop
# print the elements of the following list using a loop
# int = [ 1,4,9,16,25,36,49,64,81,100]
# for el in int:
#     print(el)

# search for a number x in this tuple using loop.
# nu = [ 1,4,9,16,25,36,49,64,81,100]
# x =49
# idx=0
# for el in nu:
#     if(el==x):
#         print("found",idx)
          
#     idx +=1
    










#functions

#WAF to print the length of a list (list is the parameter)
# heros = ["Superheroes","Mythological"," heroes","Movie" ,  "heroes"]
# coun = [2,3,4,5,6,7,8,9]
# tup = (9,8,7,6,5,4,3,2,1)
# def print_len(list):
#    print(len(list))
   
# print_len(coun)

##WAF to print the elements of a list in a single line (list is a perameter)
# heros = ["Superheroes","Mythological"," heroes","Movie" ,  "heroes"]
# coun = [2,3,4,5,6,7,8,9]
# tup = (9,8,7,6,5,4,3,2,1)
# def print_len(list):
    
#     print(len(list))
# def print_len(list):
#     for item in list:
#         print(item,end="")
   
# print_len(coun)


# heros = ["Superheroes","Mythological"," heroes","Movie" ,  "heroes"]
# coun = [2,3,4,5,6,7,8,9]
# tup = (9,8,7,6,5,4,3,2,1)
# def print_len(list):
    
#     print(len(list))
# def print_len(list):
#     for item in list:
#         print(item,end=" ")
   
# print_len(coun)


# heros = ["Superheroes","Mythological"," heroes","Movie" ,  "heroes"]
# coun = [2,3,4,5,6,7,8,9]
# tup = (9,8,7,6,5,4,3,2,1)
# def print_len(list):
    
#     print(len(list))
# def print_len(list):
#     for item in list:
#         print(item,end="\n")
   
# print_len(coun)

#WAF for calculate the factoriyal
# def clcu_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#       fact *=i
#     print(fact)
# clcu_fact(6)

#WAF to convert USD to INR
# def con_usd(n):
#     inr=83
    
#     print(inr*n)
# con_usd(78)
              
#               #or
# def con_usd(usd):
#     inr=usd*83
#     print(usd,"USD =",inr,"INR")
# con_usd()


#HW
def even_odd():
    ev = int(input("enter your number"))
    if ev %2==0:
        return "even"
    else:
        return "odd"
result = even_odd()
print(result)
