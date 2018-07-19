from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    age = db.Column(db.Integer)
    phone_no = db.Column(db.Integer, index=True)

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
            'phone_no': self.phone_no
        }
        return data
