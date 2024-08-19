print("                   Kaun Banega Crorepati!            ")
question = ["What is the capital of France?", 
            "Who is the current president of United States of America?",
            "In which year did India achieve Independence?",
            "Who was the actor that played Spider-man in the movie The Amazing Spider-man?"
            ]
answers = ["1.Nice\n2.Paris\n3.Rennes\n4.Toulouse",
            "1.Donald Trump\n2.Hilary Clinton\n3.Joe Biden\n4.Barack Obama",
            "1. 1945\n2. 1948\n3. 1950\n4. 1947",
            "1. Tobey Maguire\n2. Tom Holland\n3. Chris Evans\n4. Andrew Garfield"
            ]
correct_answer = [2,3,4,4]
for i in range(len(question)):
    print(question[i])
    print(answers[i])
    user_answer = int(input("Please choose one of the options: "))
    if user_answer == correct_answer[i]:
        print("Congratulations! You have got the right answer.")
        print() 
    else:
        print("Wrong answer! You have lost the game.")
        break
print("          CONGRATULATIONS YOU ARE A CROREPATI NOW    ")


