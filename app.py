from flask import Flask, request, render_template, redirect, flash, jsonify
from surveys import satisfaction_survey 

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="catsarecool1234"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES =[]

@app.route('/')
def show_survey_title():
    """Shows user survey titles available to seleft"""
    return render_template("home.html", satisfaction_survey=satisfaction_survey)

@app.route("/begin", methods=["POST"])
def start_survey():    
    return redirect("/questions/0")


@app.route('/questions/0')
def show_questions():
    """Shows users survey questions to select"""
    
    return render_template("questions.html",question=satisfaction_survey.questions[0])

@app.route('/questions/1')
def show_questions1():
    """Shows users survey questions to select"""
    
    return render_template("questions.html",question=satisfaction_survey.questions[1])

@app.route('/questions/2')
def show_questions2():
    """Shows users survey questions to select"""
    
    return render_template("questions.html",question=satisfaction_survey.questions[2])

@app.route('/questions/3')
def show_questions3():
    """Shows users survey questions to select"""
    
    return render_template("questions.html",question=satisfaction_survey.questions[3])



@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    # get the response choice
    choice = request.form['answer']

    # add this response to the session
   
    RESPONSES.append(choice)   
    return redirect(f"/questions/{len(RESPONSES)}")

## ASK MENTOR FOR HELP WITH ADDING LOGIC TO REDIRECT TO thanks.html PAGE AFTER
##ALL SURVEY QUESTIONS HAVE BEEN ANSWERED

##ALSO, HOW CAN WE GET THE SAME RESULTS WITHOUT HARD CODING EACH QUESTION INDEX







