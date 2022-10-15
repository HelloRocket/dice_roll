from flask import Flask, render_template, request
import random

#The script rolls a die for you from 1 to 6 and then lets you guess the number.

die_sides = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def roll_die():

    rand_roll=random.choice(die_sides)
    return render_template('form.html', roll=rand_roll)

@app.route('/result', methods=['GET', 'POST'])
def result():
    guess = int(request.form['say'])-1
    roll = request.form['roll']
    if die_sides[guess]==roll:
        backNumber= "Yes"
    else:
        backNumber= "No"

    return render_template('answer.html', 
    confirm=backNumber, 
    answer=request.form['roll'])       

    
if __name__ == "__main__":
    app.run()
