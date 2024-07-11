# FinanceApp

FinanceApp is a simple web application that allows users to manage their financial data, including insurance, pension, bank balance, loan, and credit card information. 

Users can register, log in, view their financial data, and add new financial data entries.

## Project Structure

```angular2html
FinanceApp/
│
├── financeapp/
│   ├── __init__.py
│   ├── views.py
│   ├── db.py
│   └── templates/
│       ├── index.html
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── add_data.html
│       └── view_data.html
│
├── run.py
├── financial_data.db
├── requirements.txt
├── .gitignore
├── README.md
└── venv/
```

**Clone the repository:**
```bash
git clone https://github.com/MIKIHERSHCOVITZ/FinanceApp.git
cd FinanceApp
```

**Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```


**Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**Initialize the database:**
```bash
python -c 'from financeapp.db import init_db; init_db()'
```

**Run the application:**
```bash
python run.py
```


**Open your web browser and go to:**
```bash
http://127.0.0.1:5000
```


## Functionality of the Project

1. Register: Users can register by providing a username and password. 
2. Login: Users can log in using their registered username and password. 
3. Dashboard: After logging in, users are taken to the dashboard where they can add new financial data. 
4. Add Data: Users can add financial data such as insurance, pension, bank balance, loan, and credit card information. 
5. View Data: Users can view their financial data in a list format. 
6. Logout: Users can log out from their session.


## Example to Run
1. Register:

    Go to http://127.0.0.1:5000/register

    Enter a username and password, then click "Register".


2. Login:

    Go to http://127.0.0.1:5000/login

    Enter the registered username and password, then click "Login".


3. Add Data:

    After logging in, click "Add Data" on the dashboard to add new financial data.


4. View Data:

    Click "View Data" to see the list of financial data entries.

## Expected Output

After registering and logging in:

    You should be redirected to the dashboard.
    The dashboard will have options to add data and view data.

After adding data:

    The data will be added to the database and will be available to view under the "View Data" section.

Viewing data:

    You will see a list of financial data entries with details like ID, insurance, pension, bank balance, loan, and credit card information.

## Additional Information

1. Templates: HTML templates are stored in the templates directory.
2. Database: SQLite database file financial_data.db is used to store user and financial data.
3. Session Management: Flask session management is used to handle user sessions.



