from .models import Onboard, Question
import json


def onboard_from_json(onboard_json_string):
    onboard_dict = json.loads(onboard_json_string)
    onboard = Onboard(title=onboard_dict['title'])
    onboard.questions = questions_from_json(onboard_json_string)
    return onboard


def questions_from_json(onboard_json_string):
    questions = []
    questions_dicts = json.loads(onboard_json_string).get('questions')
    for question_dict in questions_dicts:
        body = question_dict['body']
        kind = question_dict['type']
        questions.append(Question(content=body, kind=kind))
    return questions
