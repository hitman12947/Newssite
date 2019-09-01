from newsweb import db

class NewsDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text,nullable=False)
    link = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"News for: {self.title}"
