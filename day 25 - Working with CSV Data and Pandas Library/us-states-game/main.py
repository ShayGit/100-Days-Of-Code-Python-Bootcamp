import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


names = turtle.Turtle()
names.penup()
names.color("black")
names.hideturtle()
turtle.shape(image)
states_guessed = []

data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()


while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 states correct", prompt="What's another state's name:").title()

    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in states_guessed]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in states_guessed:
        state_data = data[data.state == answer_state]
        coor = (float(state_data.x), float(state_data.y))
        names.goto(coor)
        names.write(answer_state)
        states_guessed.append(answer_state)




turtle.mainloop()
