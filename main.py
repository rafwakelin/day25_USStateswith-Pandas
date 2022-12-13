import turtle
import pandas

guesses = []
states_to_learn = []

# Setting the screen
screen = turtle.Screen()
screen.title("Guess the State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading CSV file with pandas library
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()

while len(guesses) < 50:
    user_answer = screen.textinput(title=f"{len(guesses)}/50", prompt="Type the U.S. state name")
    formatted_answer = user_answer.title()

    # Exits thr game if user type exit and creates a csv file with the states user didn't guess
    if formatted_answer == "Exit":
        for state in states_list:
            if state not in guesses:
                states_to_learn.append(state)
        data_frame = pandas.DataFrame(states_to_learn)
        data_frame.to_csv("States_to_Learn.csv")
        break

    # Writes the name of the state in the map and adds the guesses to a list
    for state in states_list:
        if formatted_answer == state and state not in guesses:
            guesses.append(state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_location = states_data[states_data.state == formatted_answer]
            t.goto(float(state_location.x), float(state_location.y))
            t.write(formatted_answer)

screen.exitonclick()
