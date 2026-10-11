# Using the with keyword:
#If you are not using the with statement, you must write a close statement in order to close the file:

with open("D:\\Python Prc & Environment\\python\\File Handle\\dummy.txt") as f:
  print(f.read())