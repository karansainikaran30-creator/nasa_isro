# print("hello world")
# print("my name is karan saini \n i am from jaipur")
# print("my name is karan saini \t i am from jaipur")
# # variables
# name = "karan"
# age = 23
# price=67.7
# print(name)
# print(age)
# print("name")
# print(price)
# print("my name is :",name, "my age is :",age)
# name2=name
# print(name2)
# print(type(name)) #string
# print(type(age)) #int
# print(type(price)) #float

# #deta types
# #integyers,strint,float,boolean,none

# age=19
# old=False
# a= None
# print(type(old))
# print(a)
# print(type(a))
#  # python is a case sensitive language
 
#  # print sum
 
 
# a=2
# b= 34
# sum=a+b
# print(sum)
 
#  #operators
#     # 1. arithmetic operators
# a=2
# b= 34
# sum=a+b
# c=a+b
# print(sum)
# print(c)
# a=2
# b= 34
# c=a-b
# print(c)
# a=2
# b= 34
# c=a*b
# print(c)
# a=2
# b= 34
# c=a/b
# print(c)
# a=2
# b= 34
# c=a%b
# print(c)
# a=34

# b= 2
# c=a**b
# print(c)
 
#  # relational operaters
#   # ==,!=,>,<,>=,<=
  
# a=30
# b=20
# print(a==b) # False
# a=30
# b=20
# print(a!=b) #true
# a=30
# b=20
# print(a<b) #false
# a=30
# b=20
# print(a>b) #true
# a=30
# b=20
# print(a>=b)#true
# a=30
# b=20
# print(a<=b) #false

# #assigment operators
#   # =,+=,-=,/=,*=,**=
# a=23
# print(a)
# num=10
# num+=10
# print(num) #20
# num=10
# num-=10
# print(num) #0
# num=10
# num/=10
# print(num) #1
# num=10
# num*=10
# print(num) #100
# num=10
# num**=10
# print(num) #10000000000
# #logical operaters
#   #   and, or ,not
  
# print(not False)
# print(not True)

# a=50
# b=40
# print(not (a>b)) #false
# print(not (a<b)) #true
# a=True
# b=True
# print(a and b) #true
# a=True
# b=False
# print(a and b) #false

# a=True
# b=True
# print(a or b)

# a=True
# b=False
# print(a or b)

# a = 40
# b= 50
# print(a==b and a<b) #false

# a = 40
# b= 50
# print(a==b or a<b) #true

# a = 40
# b= 50
# print( not a<b) #false


# #type casting

# a = int("2")
# b = 4
# print(a+b)
# a = float(2)
# b = (3.3)
# print(type(a))
# print(type(b))
# print(a+b)
# a = float(2)
# b = int(3.3)
# print(type(a))
# print(type(b))
# print(a+b)
# a = float("45")
# b = (3.3)
# print(type(a))
# print(type(b))
# print(a+b)


# #input in python
# #1
# input("enter your name")
# #2
# name = input("enter your name")
# print(name)
# #3

# name = input("enter your name")
# age = input ("enter your age")
# marks = input ("eter your marks")
# print("welcome",name,age,marks)

# #4

# name = input("enter your name")
# age = int(input ("enter your age"))
# marks = int(input ("eter your marks"))
# print("welcome",name,age,marks)


# #strings 

# str1 = "this is a string."
# str2 = 'this is a string.'
# str3 = """" this is a string."""
#   # concatenation
# str1 = "this is a string."
# str2 = 'this is a string.'
# str3 = """" this is a string."""
# print(str1+str2+str3)

# str1 = "this is a string."
# str2 = 'this is a string.'
# str3 = """" this is a string."""
# final_str = str1+str2+str3
# print(final_str)
 
#  #length of str.
# str1 = " a string."
# str2 = 'this is.'
# str3 = """" this is a string."""
# #1
# print(len(str1))
#  #2
# len2 = len(str2)
# print(len2)

# print(len(str1+""+str2+str3))

# #indexing
# #1
# str = "karan saini"
# ch = str[2]
# print(ch) #r
# #2
# print(str[3])


# #slicing
# str = 'karan saini'
# print(str[1:4])
# str = 'karan saini'
# print(str[0:5])
# 2
# print(str[0:len(str)])
# #nagative index
# print(str[-5:-1])

# string functions
# str = "i am a student"
# #1st function
# print(str.endswith("ent")) #true
# print(str.endswith("abc")) #false
# #2nd
# print(str.capitalize()) #changes only new string not orignal
# print(str)

# str= str.capitalize() #changes orignal string
# print(str)
#  #3rd
# print(str.replace("a","ox"))
# print(str.replace("student","boy"))

# #4th
# print(str.find("student")) #7
# print(str.find("a")) #2
# print(str.find("x")) #-1 / not exist

# #5
# print(str.count("a")) #2
# print(str.count("student")) #1

# ## conditional statement

# age = 89

# if(age>18):
#   print("true")
# elif(age<18):
#   print("false")
# else:
#   print("end of code")
  
  
  
  
  
# age = 12

# if(age==18):
#   print("yes")
# if(age==16):
#   print("yes")
# if(age==19):
#   print("yes")
# elif(age==13):
#   print("no")
  
  
  
  
# light = "red"
  
# if(light=="green"):
#   print("go")  
# elif(light=="red"):
#   print("stop")
    

#  =input("enter light colour")
# light= a
  
# if(light=="green"):
#   print("go")  
# elif(light=="red"):
#   print("stop")
#     
    
    
# a =2
# if():
#   print()  
# elif():
#   print()
# else:
#   print()
  
  
  
  
# marks= 89

# if(marks>=90):
#     print("gread 'A'")
# elif(marks>=80):
#     print("gread 'B'")
# elif(marks>=70):
#     print("c")
# elif(marks<70):
#     print("d")

  
  
  
# marks= 89

# if(marks>=90 and marks < 100):
#     print("gread 'A'")
# elif(marks>=80 and marks < 90):
#     print("gread 'B'")
# elif(marks>=70 and marks < 80):
#     print("c")
# elif(marks<70):
#     print("d")
# else:
#     print("...........")
    
    
    
    
    
  
# marks= 89

# if(marks>=90 and marks < 100):
#     grade = "a"
# elif(marks>=80 and marks < 90):
#     grade ="B"
# elif(marks>=70 and marks < 80):
#     grade = "c"
# elif(marks<70):
#     grade = "d"
# else:
#     gread = "fail"
    
# print("your gread", grade)
    
    
    
    
    
    
# mmarks= int(input("enter your marks"))

# if marks>=90 and marks < 100:
#     grade = "a"
# elif marks>=80 and marks < 90:
#     grade ="B"
# elif marks>=70 and marks < 80:
#     grade = "c"
# elif marks<70:
#     grade = "d"
# else:
#     gread = "fail"
    
# print("your gread", grade)





# #list and tuples
#     #list in python

# marks1 = 97.78
# marks2 =89.90
# marks3 =78.90
# marks4 =90.00
# marks5 =89.87
    
    
# marks = [97.78,89.90,78.90,90.00,89.87]
# print(marks)
# print(type(marks))
# print(marks[3])
# marks[3] = 45.90
# print(marks[3])

# student = ["karan",19,98.90,"peepla"]
# print(student)
# print(type(student))
# print(student[0])
# student[3]="jaipur"
# print(student[3])

    
# #list slicing
# marks= [97.78,89.90,78.90,90.00,89.87]
# print(marks[1:3])
# print(marks[:3])
# print(marks[1:])
# print(marks[-4:-1])
# print(len(marks))


# #list methods
# list = [2,1,4,3]
# list.append(9)
# print(list)
# list.sort()
# print(list)
# print(list.append(9))
# print(list.sort())
# list.sort(reverse=True)
# print(list)


# fruts=["apple","banana","mango","lichi"]
# print(fruts)
# print(type(fruts))
# print(len(fruts))
# fruts.append("orange")
# print(fruts.append("orange"))
# print(fruts)
# fruts.sort()
# print(fruts.sort())
# fruts.sort(reverse=True)
# print(fruts)
# fruts.reverse()
# print(fruts)
# fruts.insert(1,"papaya")
# print(fruts)
# fruts.remove("apple")
# print(fruts)
# fruts.pop(2)
# print(fruts)



#tuples in python

# tup = (2,3,4,5,6,7,)
# print(tup)
# print(type(tup))
# print(tup[0])
# print(tup[2])

# tup2=("hello",)
# print(tup2)
# print(type(tup2))

# #slicing
# print(tup[2:5]) 


#tuple methods
# tup = (1,2,3,4,5,5,6,)
# index =tup.index(5)
# print(index)
# count = tup.count(5)
# print(count)



# #dictionary & set in python

# dict={
#     "name" : "karan",
#     "age" : 18,
#     "add.":"jaipur",
#     "sub.":["python","java","c"],
#     "topics":("dict","set"),
    
# }

# print(dict)
# print(type(dict))
# print(len(dict))
# print(dict["name"])
# print(dict["age"])
# print(dict["topics"])
# dict["name"]="ramkaran"
# print(dict)
# dict["name"] = "ram"
# print(dict)
# dict["nick name"] = "karan saini"  
# print(dict)

# null_dict = {}
# print(null_dict)

# #nested dict.

# student = {
#     "name" : "karan",
#     "subjects":{
#         "phy":89,
#         "chem": 90,
#         "mat." : 98,
#     }
# }
# print(student["subjects"]["chem"]) #90
#  #methods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))
# student.update({"city":"jaipur"})
# print(student)

# #set in python

# nums = {1,2,3,4,5}
# print(nums)
# print(type(nums))
# num = {9,3,4,5,"karan","jaipur","jaipur"}
# print(num)
# print(len(num))
# empty =set()
# print(empty)

# #methods
# # num.add(1)
# # num.remove(1)
# # num.remove(7) #error
# # num.clear() #empty
# # num.pop()
# # num.pop()
# # num.union(nums)
# num.intersection(nums)
# print(num)


#loops in python
# count = 1
# while count <= 5:
#     print("hello karan")
#     count +=1   
#     print(count)
# # i = 1
# while i<=1000:
#     print("karan",i)
#     i+=1
# i = 5
# while i>=1:
#     print(i)
#     i-=1

#key word 1st break and 2nd continue

# count = 1
# while count <= 5:
#     if(count == 3):
#         break
#     print(count)
    
#     count +=1   
    
# count = 0
# while count <= 10:
#     if(count == 4):
#         count +=1
#         continue
#     print(count)
#     count +=1   

# count = 0
# while count <= 10:
#     if(count%2== 0 ): #for odd numbers
#         count +=1
#         continue
#     print(count)
#     count +=1 
   
   
# count = 0
# while count <= 10:
#     if(count%2!= 0 ): #for even numbers
#         count +=1
#         continue
#     print(count)
#     count +=1 
   
   
#for loop
# list = [1,2,3,4,5,6,7]
# for el in list:
#     print(el)
    
# list = (1,2,3,4,5,6)
# for tu in list:
#     print(tu)



# str = "karansaini"
# for name in str:
#       if(name == 'n'):
#          print("n found")
#          break
#       print(name)
# else:
#     print("end")


#range()
# seq = range(10) #range(stop)
# for num in seq:
#     print(num)

# seq = range(2,10) #range(start,stop)
# for num in seq:
#     print(num)
    
    

# seq = range(2,10,2) #range(start,stop,stap)
# for num in seq:
#     print(num)

#pass statement
# for i in range(89):
#     pass
# print()
    


# function & recursion
# def calc_aver(a,b,c):
#     sum = a +b+c
#     averg=sum/3
#     print(averg)
#     return(averg)
# calc_aver(1,2,3)

# def vel(a,b,c,d):
#     sum=a+b+c+d
#     ave=sum/4
#     div=ave/2
#     print(sum)
#     print(ave)
#     print(div)
#     return sum 
# vel(2,3,4,5)

# types of function















# opps in python
# class car:
#     colour = "blue"
    
# car1 = car()
# print(car1.colour)

# class Student:
#     #default constructores
#     def __init__(self):
#          pass
#      #parameterized constructors
         
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
# s1 = Student("karan",97)
# print(s1.name,s1.marks)

# s2 = Student("arjun",89)
# print(s2.name, s2.marks)

#class & instance attributes
# class Student:
#     collage_name = "gyan vihar"
    
    
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
# s1 = Student("karan",97)
# print(s1.name,s1.marks,s1.collage_name)

# s2 = Student("arjun",89)
# print(s2.name, s2.marks)
# print(s2.collage_name)
# print(Student.collage_name)

#methods
# class Student:
#    collage_name = "gyan vihar"
    
    
#    def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
        
#    def welcome(self):
#     print("welcome students")
        
# s1 = Student("karan",97)


    
# s1.welcome()
    



# class Student:
#    collage_name = "gyan vihar"
    
    
#    def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
        
#    def get_avg(self):
#      sum = 0
#      for val in self.marks:
#          sum +=val
#      print("hi",self.name,"your avg score is:",sum/3)
        
# s1 = Student("karan",[97,87,90])
# s1.get_avg()

#static methods


#del key world
class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student("karan")
print(s1.name)
del s1.name
print(s1.name)