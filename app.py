from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey 

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="catsarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES =[]

@app.route('/')
def show_survey_title():
    """Shows user survey titles available to seleft"""
    return render_template("home.html", satisfaction_survey=satisfaction_survey)


# @app.route('/questions/0')
# def show_questions():
#     """Shows users survey questions to select"""
    
#     return render_template("questions.html",question=satisfaction_survey.questions[0])

@app.route('/questions/<int:question_id>')
def show_questions (question_id):
    """Shows users survey questions to select"""
    if (len(RESPONSES) != question_id):
        # Trying to access questions out of order.
        flash("Please answer questions in order.")
        return redirect(f"/questions/{len(RESPONSES)}")
    if (len(RESPONSES) == len(satisfaction_survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")
    else:
        return render_template("questions.html",question=satisfaction_survey.questions[question_id])





@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    # get the response choice
    choice = request.form['answer']

    # add this response to the session
   
    RESPONSES.append(choice)   
    return redirect(f"/questions/{len(RESPONSES)}")


@app.route("/complete")
def show_completed():
    return render_template("thanks.html")

## Review adding methods=["POST"] to the /answer route









