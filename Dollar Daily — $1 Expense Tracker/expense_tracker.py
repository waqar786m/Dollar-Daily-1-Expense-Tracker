import streamlit as st

# Class to represent an expense
class Expense:
    def __init__(self, description: str, amount: float):
        # Initialize expense with description and amount
        self.description = description
        self.amount = amount

    def __str__(self):
        # String representation of an expense (e.g. "Coffee: $1.00")
        return f"{self.description}: ${self.amount:.2f}"

# Class to manage expenses and daily limit
class ExpenseTracker:
    def __init__(self):
        # Initialize expenses and daily limit in session state
        if "expenses" not in st.session_state:
            st.session_state["expenses"] = []
        if "daily_limit" not in st.session_state:
            st.session_state["daily_limit"] = 1.0  # default limit set to $1.0
        self.__expenses = st.session_state["expenses"]

    def set_limit(self, limit: float):
        # Set the daily limit
        st.session_state["daily_limit"] = limit
        st.success(f"Daily limit set to: ${limit:.2f}")

    def add_expense(self, description: str, amount: float):
        # Check if adding this expense will exceed the limit
        if self.get_total_expense() + amount > st.session_state["daily_limit"]:
            st.warning("Warning: Adding this expense exceeds your limit!")
            return  # Exit the function without adding the expense
        
        # If the limit is not exceeded, add the expense
        expense = Expense(description, amount)
        self.__expenses.append(expense)
        st.session_state["expenses"] = self.__expenses  # Update session state with the new expense
        st.success(f"Added: {expense}")

    def get_total_expense(self):
        # Calculate and return the total expenses added so far
        return sum(exp.amount for exp in self.__expenses)

    def get_remaining_balance(self):
        # Calculate and return the remaining balance
        return st.session_state["daily_limit"] - self.get_total_expense()

    def list_expenses(self):
        # List all added expenses
        if not self.__expenses:
            st.write("No expenses added yet.")
        for exp in self.__expenses:
            st.write(exp)

    def reset_expenses(self):
        # Reset all expenses for a new day
        self.__expenses = []
        st.session_state["expenses"] = []  # Clear the session state expenses
        st.success("Expenses have been reset.")

# Main user interface
def main():
    st.title("Dollar Daily — $1 Expense Tracker")

    tracker = ExpenseTracker()  # Create ExpenseTracker instance

    st.markdown("### Set your daily spending limit before adding expenses.")
    # Input for setting daily limit
    new_limit = st.number_input("Set daily limit ($):", min_value=0.01, step=0.01, value=st.session_state["daily_limit"])
    if st.button("Update Limit"):
        tracker.set_limit(new_limit)

    # Sidebar for navigation between different options
    option = st.sidebar.selectbox(
        "Choose an option:",
        ["Add Expense", "View Total Spent", "View Remaining Balance", "List All Expenses", "Reset for New Day"]
    )

    if option == "Add Expense":
        description = st.text_input("Enter expense description:")
        amount = st.number_input("Enter amount:", min_value=0.0, max_value=st.session_state["daily_limit"], step=0.01)
        if st.button("Add Expense"):
            tracker.add_expense(description, amount)  # Add expense if button clicked

    elif option == "View Total Spent":
        # Display total spent so far
        st.write(f"Total Spent: ${tracker.get_total_expense():.2f}")

    elif option == "View Remaining Balance":
        # Display remaining balance
        st.write(f"Remaining Balance: ${tracker.get_remaining_balance():.2f}")

    elif option == "List All Expenses":
        # List all expenses added so far
        tracker.list_expenses()

    elif option == "Reset for New Day":
        if st.button("Reset Expenses"):
            tracker.reset_expenses()  # Reset all expenses for the new day

# Run the app
if __name__ == "__main__":
    main()
