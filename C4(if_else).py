#conditional statement

marks=int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
elif marks < 33:
    print("Fail")
else:
    print("c")

# If not
rain= False
if not rain:
    print("Go out side the home ")