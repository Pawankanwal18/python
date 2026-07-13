#list are the simple way to select the data is used in python
age=input("what is your age")
print("your age is " +age) 
dogs=["roger", 1,"syd", True]
#print("roger" in dogs)
print(dogs[1])
dogs[1]="buddy"
dogs.append("max")
print(dogs[-1])
print(dogs[0:3])
dogs.remove("syd")
print(dogs)
