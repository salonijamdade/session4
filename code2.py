password="saloni"
wrong_pass=True
while wrong_pass:
    user_input=input("enter password")
    if user_input==password:
        wrong_pass=False
    else:
        print("wrong password")

print("password correct")