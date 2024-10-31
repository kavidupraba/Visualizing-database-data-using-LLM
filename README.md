# Visualizing-database-data-using-LLM
The goal of this project is to create a system that generates SQL queries and displays results as charts using a Large Language Model (LLM). The solution allows users to interact easily without requiring Priore programming skills, which makes database queries easier.

#System Overview
The system includes the following components
User interface (UI): A simple GUI interface was created using Tkinter, where users can enter their requests.
LLM (Gemini-1.5-flash): response with generated queries, plot codes with explanation.
System: Database, decision making

#Workflow
Step 1: User Request
The user enters a request or question related to data that stored in database.
The system classifies the input as SQL-related or general.
Step 2: LLM query generation
For SQL-related query generation system prompts the LLM with a schma (stored in a JSON file).
The LLM generates SQL code and, if necessary, Python code for visualization.
Step 3: Executing SQL Queries
The system executes SQL queries on the database.
If the query is related to retrieving data, it is passed for chart creation. If it modifies data,the system returns a confirmation to the user.
Step 4: Data Visualization
The Retrieved data is sent back to the LLM for chart generation.
The LLM generates a Python Seaborn chart, which the system executes and displays.
Step 5:Response and Recovery
If the system encounters errors (e.g. incorrect queries), it returns an explanation to the user.
It updates the schema in the JSON file when the database structure changes.
4.Key functionalities
SQL Querying: The system can generate and execute SQL queries for various operations, such as data retrieval and modification.
Data Visualization: Seaborn is used to create visualization example bar plot, scatter plot…etc with explanations from the LLM about why a certain chart type is suitable.
Error handling: Basic error detection is implemented for handling incorrect queries and database errors.
Handling Failures.
Potential Issues.
LLM will might not visualize whole data we retrieve from the database (no subplots).
User Intent Misunderstanding: The system uses a basic classification ( decide the request is about sql related or not using few key word like. [“create”, “retrieve”…etc] in here we try to use NLP natural language processing model like spacy so it can detect at least small changes like retrieve, retrieving but it did not provide that much support.
When modifications LLM model might not provide a “DONE! Message sometimes” even it already completed the task.


#Future Work
Improvements:
•	Advanced NLP features include developing, with libraries such as Hugging Face Transformers or Rasa NLU, more sophisticated intent detection that does not have to rely as heavily on keywords and phrases.
•	Upload through CSV: Upload facility for CSV and it should be able to automatically create normalized tables in the database.
•	More Powerful Visualizations: Expand the range of chart types and increase the size of the datasets handled in visualizations.
•	Comparison with other LLMs: Compare similar models like ChatGPT-3.5 and even newer ones that boast better performance and quality of interaction.
Conclusion
This project allows users who don’t have prior knowledge about data visualization and coding to interact with databases and make changes.and it simplifies complex SQL tasks. Future improvements aim to enhance flexibility, error handling, and data visualization capabilities.
