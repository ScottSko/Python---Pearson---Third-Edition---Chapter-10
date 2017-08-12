class Question:

    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, correct_answer):

        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__correct_answer = correct_answer

    def get_question(self):
        return self.__question
    def get_answer_1(self):
        return self.__answer_1
    def get_answer_2(self):
        return self.__answer_2
    def get_answer_3(self):
        return self.__answer_3
    def get_answer_4(self):
        return self.__answer_4
    def get_correct_answer(self):
        return self.__correct_answer

    def set_question(self, question):
        self.__question = question
    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    def __str__(self):

        return self.__correct_answer

def main():

    total = 0

    questions = {}

    question_1 = Question("How old is Sam Harris?", "30", "40", "50", "60", "50")
    question_2 = Question("What is the capital of California?", "Los Angeles", "Sacramento", "Pasadena", "Hollywood",
                          "Sacramento")

    questions[0] = question_1
    questions[1] = question_2

    for x in questions:
        print(questions[x].get_question())
        print("Here are the possible answers: ")
        print("1.", questions[x].get_answer_1())
        print("2.", questions[x].get_answer_2())
        print("3.", questions[x].get_answer_3())
        print("4.", questions[x].get_answer_4())
        answer = input("Please enter the number of your answer: ")

        #print(questions[x].get_answer_3() == questions[x].get_correct_answer())

        while answer.isdigit() != True:
            answer = input("Please enter only the number: ")

        if answer == "1" and questions[x].get_answer_1() == questions[x].get_correct_answer():
            total += 1

        elif answer == "2" and questions[x].get_answer_2() == questions[x].get_correct_answer():
            total += 1

        elif answer == "3" and questions[x].get_answer_3() == questions[x].get_correct_answer():
            total += 1

        elif answer == "4" and questions[x].get_answer_4() == questions[x].get_correct_answer():
            total += 1


    print("The total number of correct answers is: ", total)

main()



################################################

#def main():

#    total = 0

#    questions = {1: "How old are you?"}
#    answers = {1: ["A: 12", "B: 13", "C: 14", "D: 15"]}
#    choices = {1: "A"}

#    for x in questions:
#        print(questions[x])
#        print(answers[x])
#        your_answer = input("Enter A, B, C or D: ").upper()
#        if your_answer == choices[x]:
#            total += 1

#    print("You got", total, "answers correct")

#main()

#elif answer == 4:
#    if questions[x].get_answer_4() == questions[x].get_correct_answer():
#    total += 1
