number = input("enter a five digit number: ")
num = ""
if number.isdigit():
    if len(number) == 5:
        for count in number:
            num = count + num
        else:
            if num == number:
                print(num)
                print("it is a palindrome")
            else:
                print(num)
                print("not a palindrome")
    else:
        print("integer not five digit long")

else:
    print("not an integer")
