import pgzrun

TITLE = "QUIZ"
WIDTH = 600
HEIGHT = 550

questions = []

current_question = 0



remaining_time = 10

total_question = 0

score = 0

game_over = False

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
    if not game_over:
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
        screen.draw.textbox(str(remaining_time), timer, color='white')
        screen.draw.textbox("Welcome to the Quiz Master. This is Q" +str(current_question) + " out of " + str(total_question) + ".", marquee, color='white')
    else:
        screen.draw.text("The Game Is Over. Your Score was " + str(score) + " Out of " + str(total_question), center = (WIDTH // 2, HEIGHT // 2), color = 'black')



def on_mouse_down(pos):
    global question, score
    if skip.collidepoint(pos):
        question = read_a_question()

    for option in options:
        if option.collidepoint(pos):
            if options.index(option) == int(question[5]) - 1:
                print("correct")
                score = score + 1
            question = read_a_question()
            


def read_a_question():
    global current_question, game_over, remaining_time
    if len(questions) >0 :
        current_question = current_question + 1
        remaining_time = 10
        return questions.pop(0).split("|")
    else:
        game_over = True


def read_question_file():
    global questions, total_question
    f=open("questions.txt", "r")
    questions=f.read().split("\n")
    f.close()
    total_question = len(questions)
    

    
def update_time():
    global remaining_time, question
    if remaining_time >0:
        remaining_time = remaining_time - 1
    else:
        question = read_a_question()






read_question_file()
print(questions)
question = read_a_question()
print(question)


clock.schedule_interval(update_time, 1)

pgzrun.go()
