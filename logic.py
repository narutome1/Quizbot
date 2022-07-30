import random
import json

f = open('qna.json')
data = json.load(f)

i = 0
quest_asked = 0
correct_ans = 0

def Quiz():
    global i, usr_answer, correct_ans, quest_asked

    ques_no = random.randint(0,1)
    # ques_no = 0
    question = data[ques_no]['question']
    i += 1
    print(f"Question no.{i}: ", question)
    quest_asked += 1

    for j in range(0,4):
        print([data[ques_no]['answers'][j]['answer']])
    
    usr_input = str(input("Enter your response as A, B, C or D: "))
    usr_answer = ord(usr_input.lower()) - 97

    if data[ques_no]['answers'][usr_answer]["is_correct"] == True:
        print("Correct Answer")
        correct_ans += 1 
    else:
        print("Wrong Answer")
    print(f"Correct answers till now: {correct_ans}/{quest_asked}" )
    input("Press enter for the next question.")
    Quiz()
    


Quiz()





