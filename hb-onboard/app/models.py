from app import db


class Onboard(db.Model):
    __tablename__ = 'onboards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    questions = db.relationship('Question', backref='survey', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    @property
    def has_questions(self):
        return self.questions.count() > 0

    @staticmethod
    def to_collection_dict(query):
        resources = query.all()
        data = {
            'items': [item.to_dict() for item in resources]
        }
        return data

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'questions': self.questions
        }
        return data


class Question(db.Model):
    __tablename__ = 'questions'

    TEXT = 'text'
    BOOLEAN = 'boolean'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    kind = db.Column(db.Enum(TEXT, BOOLEAN, name='question_kind'))
    onboard_id = db.Column(db.Integer, db.ForeignKey('onboards.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def __init__(self, content, kind=TEXT):
        self.content = content
        self.kind = kind

    def next(self):
        return self.survey.questions.filter(Question.id > self.id).order_by('id').first()

    @staticmethod
    def to_collection_dict(query):
        resources = query.all()
        data = {
            'items': [item.to_dict() for item in resources]
        }
        return data

    def to_dict(self):
        data = {
            'id': self.id,
            'content': self.content,
            'onboard_id': self.onboard_id,
            'answers': self.answers
        }
        return data


class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    session_id = db.Column(db.String, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    phone_no = db.Column(db.String(128), index=True)

    @classmethod
    def update_content(cls, session_id, question_id, content):
        existing_answer = cls.query.filter(Answer.session_id == session_id and
                                           Answer.question_id == question_id).first()
        existing_answer.content = content
        db.session.add(existing_answer)
        db.session.commit()

    def __init__(self, content, question, session_id):
        self.content = content
        self.question = question
        self.session_id = session_id

    @staticmethod
    def to_collection_dict(query):
        resources = query.all()
        data = {
            'items': [item.to_dict() for item in resources]
        }
        return data

    def to_dict(self):
        data = {
            'id': self.id,
            'content': self.content,
            'session_id': self.session_id,
            'question_id': self.question_id
        }
        return data
        

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    age = db.Column(db.Integer, index=True)
    phone_no = db.Column(db.String(13), index=True)
    group = db.Column(db.String(128), index=True)
    mentor = db.Column(db.Boolean(), index=True)

    @staticmethod
    def to_collection_dict(query):
        resources = query.all()
        data = {
            'items': [item.to_dict() for item in resources]
        }
        return data

    def from_dict(self, data):
        for field in data:
            setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone_no': self.phone_no,
            'group': self.group,
            'mentor': self.role
        }
        return data


