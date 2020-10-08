# Azaan Dawson Amdg 10/8/20

x = input("Give  number")

if int(x) % 30 == 0: 
  print("x is a multiple of 2,3,and 5")
elif int(x) % 15 == 0:
  print("x is a multiple of 3 and 5")
elif int(x) % 6 == 0 :
  print("x is a multiple of 2 and 3")
elif int(x) % 2 == 0:
  print("X is a multiple of two")
elif int(x) % 3 == 0 :
  print("x is a multiple of three")
elif int(x) % 5 == 0 :
  print("x is a multiple of 5")  
else :
  print("x is not a multiple of 2,3, or 5")
