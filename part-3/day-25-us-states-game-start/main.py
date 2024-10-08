import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="whats another states name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

#states_to_learn.csv
#compare guessed_states to all_states
#any that arent in guessed_states get saved into the csv file and display when the program exit

#if answer_states is on eo fth estates in the states of the 50_states.csv
    #if they got it right:
        #create a turtle to write the name of the state at the states (x,y) cordinates
        #add 1 to the score out of 50
    #if they got it wrong:
        #display the answer box again


