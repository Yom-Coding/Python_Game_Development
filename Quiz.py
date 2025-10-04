import pgzrun

TITLE = "QUIZ"
WIDTH = 600
HEIGHT = 600

questions = []

marquee = Rect (0,0 , WIDTH , 80)
question_box = Rect (0,120 , 400 , 120)
timer = Rect (440,120, 160, 120)
opt1 = Rect (0,280, 180, 100)
opt2 = Rect (440,280, 180, 100)
opt3 = Rect (0,120, 180, 100)
opt4 = Rect (440,120, 180, 100)


def draw():
    screen.fill("white")
    screen.draw.filled_rect(marquee, "blue" )
    screen.draw.filled_rect(question_box, "blue" )
    screen.draw.filled_rect(timer, "blue" )
    screen.draw.filled_rect(opt1, "blue" )



def read_question_file():
    global questions
    f=open("questions.txt", "r")
    questions=f.read().split("\n")
    f.close()
    

    
    





read_question_file()
print(questions)

pgzrun.go()
