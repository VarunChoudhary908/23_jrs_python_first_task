a=input("Enter a number ")
f=int(1)
if a.isalpha():
    print("Not a valid input")
else:
    a=int(a)
    for b in range(1,a+1):
        f=f*b
    print(f"the factorial is {f}")

print("Varun Choudhary")