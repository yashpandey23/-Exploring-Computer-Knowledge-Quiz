print("Welcome to my computer quiz! ")

print("-------THIS QUIZ IS FOR SEE HOW MUCH YOU KNOW ABOUT THE COMPUTER IN THE LAST YOU CAN SEE YOUR SCORE AND THE PERCENTAGE YOU GO-------")

playing = input("Do you want tp play? ")


if playing != "yes":
    quit()

print("Okay ! Let's play :) ") 

# answer = input("What does CPU Stand for? ")

# if answer =="Cental processing unit":
#     print("Correct!")

# else:
#     print("Incorrect!")

# So,i am using the fuction so that i can reuse the code and reduce the code repetation
count=0
def ask_question(question, correct_answer):
    global count
  
    user_answer = input(question)

    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        count = count+1

    else:
        print("Incorrect!")

# Example usage
ask_question("1) What does CPU stand for? ", "Central Processing Unit")
ask_question("2) What is the full form of RAM? ", "Random Access Memory")
ask_question("3) What does HTML stand for? ", "HyperText Markup Language")
ask_question("4) Name three programming languages? ", "Python, Java, C++")
ask_question("5) What is the full form of URL? ", " Uniform Resource Locator")
ask_question("6) What does HTTP stand for? ", "HyperText Transfer Protocol")
ask_question("7) What is the full form of CSS? ", "Cascading Style Sheets")
ask_question("8) What does PHP stand for? ", " Hypertext Preprocessor")
ask_question("9) What is the full form of SQL? ", "Structured Query Language")
ask_question("10) What is the full form of PDF?", " Portable Document Format")



print("The number of point you scored is: "+str(count))
print ("The percentage you got is : "+str((count/10)*100)+"%")