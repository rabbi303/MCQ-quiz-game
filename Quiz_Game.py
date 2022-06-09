print("Wellcome to Quiz Game!")

#a variable for store score
score=0

#user input for initial staritng
playing= input("Do you want to play? ")

if playing.lower() != 'yes':
    quit() 
print("Okay! Lets play...\n")

#input answer from user
question = input("Who is the father of Computers?\na) James Gosling\nb) Charles Babbage\nc) Dennis Ritchie\nWrite your choice : ")

#Comparing answer
if question.lower() == 'b':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'b) Charles Babbage'\n")


#input answer from user
question = input("What is the full form of CPU?\na) Computer Processing Unit\nb) Computer Principle Unit\nc) Central Processing Unit\nWrite your choice : ")

#Comparing answer
if question.lower() == 'c':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'c) Central Processing Unit'\n")



#input answer from user
question = input("Which language is written in binary codes only?\na) pascal\nb) machine language\nc) C\nWrite your choice : ")

#Comparing answer
if question.lower() == 'b':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'b) machine language'\n")



#input answer from user
question = input("Which is the brain of the computer?\na) CPU\nb) RAM\nc) ALU\nWrite your choice : ")

#Comparing answer
if question.lower() == 'a':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'a) CPU'\n")


#input answer from user
question = input("Which is the smallest unit of data in a computer?\na) Bit\nb) Byte\nc) Nibble\nWrite your choice : ")

#Comparing answer
if question.lower() == 'a':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'a) Bit'\n")


#input answer from user
question = input("Which can access the server?\na) Web Client\nb) User\nc) Web Browser\nWrite your choice : ")

#Comparing answer
if question.lower() == 'a':
    print("Correct!\n")
    score+=1
else:
    print("Incorrect!")
    print("Correct answer is 'a) Web Client'\n ")


print("your score is: " + str(score) + " out of 6" ) 