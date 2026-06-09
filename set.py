#sets are muteable and unordered colections of uniue elements so we cant change them
#set1 ={"pawan","ram"}
#set2={"ram"}

#intersect= set1 &set2
#print(intersect)
#union =set1|set2
#print(union)
#mod=set1-set2
#print(mod)
#set cannot have duplicate elements

#order is not preserved in sets
#set ={1,2,3,4,5}
cities ={"delhi","mumbai","chennai","kolkata"}
cities2 ={"delhi","mumbai","banglore","hyderabad"}
cities3 = cities.union(cities2)
print(cities3)
cities ={"delhi","mumbai","chennai","kolkata"}
cities2 ={"delhi","mumbai","banglore","hyderabad"}
cities3 = cities.intersection(cities2)
print(cities3)
cities ={"delhi","mumbai","chennai","kolkata"}
cities2 ={"delhi","mumbai","banglore","hyderabad"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities ={"tokyo ","osaka"}
cities.add("kyoto")
print(cities)
cities ={"tokyo ","osaka"}
cities.discard("kyoto")
print(cities)