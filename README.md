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
    - `/` → Dashboard (lists & filters expenses + Chart.js bar chart).
    - `/add` → Form to add a new expense.
    - `/edit/<id>` → Edit an existing expense by ID.
    - `/delete/<id>` → Delete an expense by ID.
    - `/data` → JSON endpoint for (filtered) chart data.

- **Styling & Interactivity**
  - Swapped Bootstrap for **Tailwind CSS** (utility‑first styling).
  - Added **AOS** for smooth scroll animations (`data-aos` attributes).
  - Integrated **SweetAlert2** for modern modal confirmations.
  - Used **Alpine.js** for in‑page interactivity and deletion handling (`x-data`, `x-ref`).
  - Updated templates (`base.html`, `index.html`, `add_expense.html`, `edit_expense.html`) with:
    - Colored backgrounds, borders, and focus states on inputs.
    - Gradient buttons and cards with shadows and rounded corners.
    - Animated reveals and hover effects.

## How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/Tks23-hub/python-expense-tracker.git
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

Open your browser at `http://127.0.0.1:5000/`, then:

1. **Filter** by date range and/or category
2. **Add**, **edit**, or **delete** expenses
3. Watch your table and chart update in real‑time.
