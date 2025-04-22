
# Dollar Daily — $1 Expense Tracker

## Overview

Dollar Daily is a simple and user-friendly expense tracker built using **Streamlit**. This app helps users track their daily expenses, ensuring they stay within a set daily spending limit. By default, the app assumes a $1 limit, but users can adjust it to any value they desire.

With features like adding expenses, viewing total spending, and tracking remaining balance, this app makes it easy for users to manage their finances efficiently.

## Features

- **Set Daily Limit**: Users can set their own daily spending limit to control their expenses.
- **Add Expenses**: Users can add expenses with a description and amount.
- **View Total Spent**: Displays the total amount spent so far within the set daily limit.
- **View Remaining Balance**: Shows how much money is left within the set daily limit after expenses.
- **List All Expenses**: Displays all the expenses added by the user for the day.
- **Reset for New Day**: Allows users to reset all expenses for a new day, starting fresh.

## Project Setup

### Prerequisites

Before running the application, make sure you have the following:

- Python 3.x installed.
- Streamlit installed. If not, you can install it using pip.


3. **Install Dependencies**

   The project uses `Streamlit`. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**

   Once the dependencies are installed, you can start the app with the following command:

   ```bash
   streamlit run expense_tracker.py
   ```

5. **Access the App**

   After running the command, the app will be available in your web browser at `http://localhost:8501`.

## How to Use

### Set Daily Spending Limit

- On the home page, you can set your daily limit. The default is $1, but you can adjust this to any value that fits your needs.
- After setting the limit, click the "Update Limit" button.

### Add Expenses

- Select the "Add Expense" option from the sidebar.
- Enter a description for the expense (e.g., "Lunch", "Transport").
- Enter the amount of the expense. The maximum amount you can add is equal to your daily limit.
- Click the "Add Expense" button to record your expense.

### View Total Spent

- Under the "View Total Spent" option, the app will show the total amount you’ve spent so far.

### View Remaining Balance

- Select the "View Remaining Balance" option to see how much is left from your daily limit after subtracting the total spent.

### List All Expenses

- Select the "List All Expenses" option to view all the expenses you've added for the day.

### Reset for New Day

- At the end of the day, or whenever you want to start fresh, click the "Reset for New Day" button to reset all expenses and start the next day with a clean slate.

## Example Use Case

1. Set the daily limit to $5.
2. Add expenses such as:
   - $1.50 for breakfast.
   - $2.00 for transportation.
3. The app will display:
   - Total spent: $3.50
   - Remaining balance: $1.50


### Technologies Used:

- **Streamlit**: For building the web interface and making the app interactive.
- **Python**: The programming language used for the backend logic of the app.

---