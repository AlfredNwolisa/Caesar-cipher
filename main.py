#import clear
#def greet():
    ##print(" T baby rocks")
    ##print(" tbaby alife")

#greet()

#funtions that allows for input

#def greet_with_name(name):
    ##print(f"yes {name}")
    ##print(f" T baby rocks, yes {name}")
    ##print(f" tbaby {name}")

#greet_with_name("ALFRED")
  
#def greet_with(name, location):
    #print(f"Hello {name}")
    #print(f"What is it like in {location}?")

#greet_with("jack bauer","nowhere")

#greet_with(location="nowhere",name="jack bauer")


#Write your code below this line 👇

#def paint_calc(height, width, cover):
    #numb_cans = round((height*width),-1) / cover
    #print(f"you'll need {int(numb_cans)} pain cans")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
#test_h = int(input("Height of wall: "))
#test_w = int(input("Width of wall: "))
#coverage = 5
#paint_calc(height=test_h, width=test_w, cover=coverage)
#print("hihii")
#clear

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True

    for i in range (2, number):
        if number % i == 0:
         is_prime = False
         break

    if is_prime:
        print("its a prime number")
    else:
        print("its not a prime number")


    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


