import openai
import sqlite3

# Initialize OpenAI client with API key
client = openai.OpenAI(api_key='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')

# Function to generate response from the API
def get_code_suggestion(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Connect to a database (or create it)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user input if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY, request TEXT)''')

# Take input from the user (dynamic user input)
user_input = input("Ask me anything: ")

# Insert the user's input into the database
cursor.execute("INSERT INTO user_requests (request) VALUES (?)", (user_input,))

# Commit and close the connection to the database
conn.commit()
conn.close()

# Get the response from GPT based on the user's input
code_suggestion = get_code_suggestion(user_input)

# Output the response
print("Suggested Code:\n", code_suggestion)
