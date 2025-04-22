from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from datetime import datetime

from config import Config
from models import db, Expense

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    
    q = Expense.query
    start = request.args.get('start_date')
    end   = request.args.get('end_date')
    cat   = request.args.get('category')
    if start:
        q = q.filter(Expense.date >= start)
    if end:
        q = q.filter(Expense.date <= end)
    if cat:
        q = q.filter(Expense.category == cat)

    expenses = q.order_by(Expense.date.desc()).all()
    categories = [c[0] for c in db.session.query(Expense.category).distinct().all()]
    return render_template(
        'index.html',
        expenses=expenses,
        categories=categories,
        start_date=start,
        end_date=end,
        selected_category=cat
    )
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amt  = float(request.form['amount'])
        cat  = request.form['category']
        desc = request.form.get('description', '')
        dt   = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        new  = Expense(amount=amt, category=cat, description=desc, date=dt)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/data')
def data():
    
    q = Expense.query
    start = request.args.get('start_date')
    end   = request.args.get('end_date')
    cat   = request.args.get('category')

    if start:
        q = q.filter(Expense.date >= start)
    if end:
        q = q.filter(Expense.date <= end)
    if cat:
        q = q.filter(Expense.category == cat)

    results = q.with_entities(
        Expense.category,
        db.func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    categories = [r[0] for r in results]
    totals     = [r[1] for r in results]
    return jsonify(categories=categories, totals=totals)

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    exp = Expense.query.get_or_404(expense_id)
    db.session.delete(exp)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    exp = Expense.query.get_or_404(expense_id)
    if request.method == 'POST':
        exp.amount      = float(request.form['amount'])
        exp.category    = request.form['category']
        exp.description = request.form.get('description', '')
        exp.date        = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_expense.html', expense=exp)



if __name__ == '__main__':
    app.run(debug=True)
