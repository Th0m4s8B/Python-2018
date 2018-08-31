import random

name = str(input("What is your name?: "))
while True:
    loop = input("Do you have a question?(Y/N): ")
    if loop.strip() == "Y":
        quest = input("What is your question?: ")
        shaken = input("Are you ready to have your question answered?(Y/N)?: ")
        fortunes = ["No","Yes","Unlikely","Probable","Try Again"]
        print("Your answer is... %s." %str(random.choice(fortunes)))
    else:
        break
              
print("Have a nice day, %s."%name)
