import sqlite3

# Mocking the OpenAI API call for testing purposes
def get_code_suggestion(prompt):
    # This function simulates a response as if it came from GPT-3.5
    return f"This is a simulated response for the prompt: '{prompt}'"

# Connect to a database (or create it)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user input if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY, request TEXT)''')

# Take input from the user
user_input = input("Ask me anything: ")

# Insert the user's input into the database
cursor.execute("INSERT INTO user_requests (request) VALUES (?)", (user_input,))

# Commit the transaction to save the input
conn.commit()

# Close the database connection
conn.close()

# Get the simulated response (instead of calling the real API)
code_suggestion = get_code_suggestion(user_input)

# Output the simulated response
print("Suggested Answer:\n", code_suggestion)
