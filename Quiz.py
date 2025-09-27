import pgzrun

TITLE = "QUIZ"
WIDTH = 600
HEIGHT = 600

questions = []

def draw():
    screen.fill("white")


def read_question_file():
    global questions
    f=open("questions.txt", "r")
    questions=f.read()
    f.close()
    

    
    





read_question_file()
print(questions)

pgzrun.go()
