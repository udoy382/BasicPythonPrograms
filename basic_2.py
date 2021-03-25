# Python Program To Check Whether A Nomber Is A Palindrome Or Not

# Take Input

number = int(input("Enter The number: "))
# print(type(number))

temp = number
reverse = 0
while(number>0):
    dig = number%10
    reverse = reverse*10 + dig
    number = number//10

if temp==reverse:
    print("Number is a Palindrone!")
else:
    print("Nomber is not a Palindrone!")