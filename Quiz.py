import pgzrun

TITLE = "QUIZ"
WIDTH = 600
HEIGHT = 550

questions = []

marquee = Rect (0,0 , WIDTH , 80)
question_box = Rect (0,120 , 400 , 120)
timer = Rect (440,120, 160, 120)
opt1 = Rect (0,280, 180, 100)
opt2 = Rect (220,280, 180, 100)
opt3 = Rect (0,420, 180, 100)
opt4 = Rect (220,420, 180, 100)
skip = Rect (440,280, 160, 240)

options = [opt1, opt2, opt3, opt4]

def draw():
    screen.fill("white")
    screen.draw.filled_rect(marquee, "black" )
    screen.draw.filled_rect(question_box, "black" )
    screen.draw.filled_rect(timer, "black" )
    for option in options:
        screen.draw.filled_rect(option, "black" )

    screen.draw.filled_rect(skip, "black" )

    screen.draw.textbox(question[0].strip(), question_box, color='white')
    screen.draw.textbox(question[1].strip(), opt1, color='white')
    screen.draw.textbox(question[2].strip(), opt2, color='white')
    screen.draw.textbox(question[3].strip(), opt3, color='white')
    screen.draw.textbox(question[4].strip(), opt4, color='white')
    screen.draw.textbox("Skip", skip, color='white', angle=-90)

def on_mouse_down(pos):
    print("HELLO")
    global question
    if skip.collidepoint(pos):
        print("SKIP")
        question = read_a_question()


def read_a_question():
    print("READ")
    if len(questions) >0 :
        return questions.pop(0).split("|")


def read_question_file():
    global questions
    f=open("questions.txt", "r")
    questions=f.read().split("\n")
    f.close()
    

    
    





read_question_file()
print(questions)
question = read_a_question()
print(question)




pgzrun.go()
