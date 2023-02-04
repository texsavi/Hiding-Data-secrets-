
import os
admin=os.environ["adminUser"]
adPass=os.environ["adminPass"]
guest=os.environ["normUser"]
guPass=os.environ["guest"]
s=""
print(f"{s:^18}\033[34m🇰🇪My Server🇰🇪")
print()
while True:
  user=input("Username>> ")
  print()
  wpass=input("Password>> ")
  if user==admin and wpass==adPass:
    print("Hello Admin😊! Welcome🤗")
    break
  elif user==guest and wpass==guPass:
    print("Hello guest🤗. Welcome☺️!")
    break
  else:
    print("We could not identify you😢")
    continue