# program 1
# hi github

def checkSum(a,b,c):
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  c = int(input("Enter a number: "))
  d = a+b+c

  if (d%3 == 0):
    print("Its divisible by 6. ")
  else:
    print("It's not divisible by 6. ")

checkSum(3,4,5)
print("**************************")
#program2
def water(temperature):
  temperature = int(input("Enter a number to be temperature"))
  if (temperature >= 100):
    print("gas")
  if (temperature <= 0):
    print("solid")
  if (temperature > 0) and (temperature<100):
    print("liquid")
water(30)
print("**************************")
#program3
def greatest(aa,bb):
  if (aa>bb):
    return aa
  else :
    return bb
def greatestOfThree(num1,num2,num3):
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a number: "))
  num3 = int(input("Enter a number: "))
  num12= greatest(num1,num2)  
  num4 = greatest(num12,num3)
  print(num4+"Is the greatest number.")
greatestOfThree(1,2,3)
print("**************************")
