# Azaan Dawson Amdg 10/7/20

x = input("How many wins for Ethiopia")

y = input("How many ties for Ethiopia")

w = input("How many wins for France")

z = input("How many ties for France")

total_score_1 = (3 * int(x)) + int(y)

total_score_2 = (3 * int(w)) + int(z)

if total_score_1 < total_score_2 :
  print("France won")
else:
  print("Ethiopia won") 
