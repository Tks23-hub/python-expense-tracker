from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Expense {self.id}: {self.category} – {self.amount}>'
