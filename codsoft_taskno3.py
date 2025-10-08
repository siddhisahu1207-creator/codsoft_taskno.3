print("\033c",end="")
while True:
 heading=("PASSWORD GENERATOR")
 print(heading.center(500))
 import random
 lower="abcdefghijklmnopqrstuvwxyz"
 upper="ABCDEFGFIJKLMNOPQRUSTUVWXYZ"
 number="0123456789"
 symbol="~!@#$%^&*()_+-=[]\<>/?|}{"
 complexity=int(input("Select the complexity you want for your password:-\n \t1-Easy \n \t2-Strong \n \t3-Very Strong\n")) 
 char=""
 if complexity==1:
     char=lower+upper
 elif complexity==2:
     char=lower+upper+number
 else:
     char=lower+upper+number+symbol 
 length=int(input("Enter the length of password you want: "))
 password="".join(random.sample(char,length))
 print("Generated Password:",password)
 program=input("Do you want to check again(y/n):")
 if program=="n":
    break
 
print("Thankyou!")