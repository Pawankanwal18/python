#function is a block of code which is used to perform a specific task and it can be reused multiple times in a program
#def hello(name,age):
  #  print("hello " + name +" you are " + str(age)+' years old')

#hello("pawan",22)
def hello(name,):
    if not name:
        return
    print("hello "+ name + '!')

hello("pawan") 
#if we declear a fuction outside the function that is called global variable
#and if we declear a variable inside the function that is called local variable
 #age=8
#3  print(age)

#print(age)
#test()

#a function innside a function is called nested function 
def outer_function():
    def inner_function():
        print("hello from inner function")
    inner_function()
    print("hello from outer function")
outer_function()

#we can return multiple values from a function using tuple
def calculate(a,b):
    sum=a+b
    diff=a-b 
    return sum,diff
result1,result2=calculate(5,3)
print("sum:",result1)
print("difference:",result2)
#it is also possible to return a function from another function