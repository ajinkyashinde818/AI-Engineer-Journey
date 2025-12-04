a=int(input("Enter the Number 1:"))
b=int(input("Enter the Number 2:"))


choice=input("What are you Perform like (+,-,*,/):").strip()


if choice == "+":
    print("The Addition is:",a+b)
elif choice== "-":
    print("The Substraction is:",a-b)
elif choice== "*":
    print("The Multiplication is:",a*b)
elif choice== "/":
    if b==0:
        print("Division By 0")
    else:
        print("The Division is:",a/b)
else:
    print("Invalid Choice")