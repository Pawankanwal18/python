#try:
 #   l=[1,2,4,5]
  #  i = int(input("enter  the index:"))
   # print(l[i])
#except:
 #  print("some error occured")

#finally:
 #   print("this block is always executed")

def fun1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("this block is always executed")

x = fun1()
print(x)
