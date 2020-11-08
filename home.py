from flask import Flask, render_template, request, session
import random 

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'




def computer_choice():
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0,2)]


# def num_game():
#     guess_number = random.randrange(0,101)
#     if "guess" not in session:
#         session["guess"] = guess_number
#     return render_template("number_game.html")


def winner1(player_choice, computer_choice):
    
    winner = "computer"
    session['Lossess'] += 1

    if player_choice == computer_choice:
        winner = "tie"
        session['tie'] += 1
        session['Lossess'] -= 1

    if player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
        session['Wins'] += 1
        session['Lossess'] -= 1

    if player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
        session['Wins'] += 1
        session['Lossess'] -= 1

    if player_choice == "paper" and computer_choice == "rock":
        winner = "player"
        session['Wins'] += 1
        session['Lossess'] -= 1

    return winner



@app.route('/')
def index():
    
    if session == 0:
        session['Wins'] = 0
        session['Lossess'] =0
        session['tie'] =0 

    
    
    return render_template("home.html")



@app.route('/results', methods=['POST'])
def result():

    player= request.form['choice']
    computer =  computer_choice()
    winner = winner1(player, computer)

    return render_template("winner.html", winner=winner, player_choice=player, computer_choice=computer, wins = session['Wins'], Lossess = session['Lossess'], Ties=session['tie']  )
    
if __name__=="__main__":    
    app.run(debug=True)