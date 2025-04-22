# 🏦 Python Expense Tracker

A simple Flask‑based personal finance app to **track** and **visualize** your expenses.

## What’s Done So Far

- **Project scaffold**

  - Created a Python virtual environment (`venv/`).
  - Added core dependencies in `requirements.txt`.

- **Configuration** (`config.py`)

  - Set up SQLite database (`expenses.db`) via SQLAlchemy.
  - Centralized settings in a `Config` class.

- **Data model** (`models.py`)

  - Defined an `Expense` model with `id`, `amount`, `category`, `description`, and `date`.

- **Flask app** (`app.py`)

  - Initialized Flask, SQLAlchemy, and Flask‑Migrate.
  - Routes:
    - `/` → Dashboard (lists expenses + Chart.js bar chart).
    - `/add` → Form to add a new expense.
    - `/data` → JSON endpoint for chart data.

- **Templates** (`templates/`)

  - `base.html` – common layout with Bootstrap & navbar.
  - `index.html` – dashboard view, Jinja loops, Chart.js.
  - `add_expense.html` – form to submit expenses.

- **Database**
  - Ran migrations (`flask db init`, `migrate`, `upgrade`) to create `expenses` table in `expenses.db`.

## How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/<your‑username>/python-expense-tracker.git
cd python-expense-tracker

# 2. Create & activate venv
py -3 -m venv venv
.\venv\Scripts\Activate.ps1  # (or `source venv/bin/activate` on macOS/Linux)

# 3. Install deps
pip install -r requirements.txt

# 4. Run migrations
$Env:FLASK_APP = "app.py"
python -m flask db upgrade

# 5. Start the server
python -m flask run
```
