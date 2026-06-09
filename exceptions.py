try:
   raise Exception('an errror!')
except Exception as error:
   print(error)