from . import app
from .models import Onboard
from flask import url_for, session, jsonify
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/message', methods=['POST'])
def sms_onboard():
    response = MessagingResponse()

    onboard = Onboard.query.first()

    if 'question_id' in session:
        response.redirect(url_for('answer', question_id=session['question_id']))
    else:
        welcome_user(onboard, response.message)
        redirect_to_first_question(response, onboard)
    return str(response)


def redirect_to_first_question(response, onboard):
    first_question = onboard.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
    welcome_text = 'Welcome to Health-Buddy'
    send_function(welcome_text)

