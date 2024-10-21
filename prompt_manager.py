
def genarate_prompts(table_schema, user_i):
    prompt = (
        f"Given the following table schema created using SQLite3 in a Python environment:\n\n"
        f"{table_schema}\n\n"
        f"Your task is to generate the appropriate SQL queries based on the user's input.\n"
        f"Ensure that the query follows the SQLite3 syntax and correctly references the provided table structure.\n\n"
        f"Here is the user's input: {user_i}\n\n"
        f"Examples:\n"
        f"1. If the user asks 'retrieve all items from the TEST table', you should return: SELECT * FROM TEST;\n"
        f"2. If the user asks 'find the total sales for each product', you should return a query that uses GROUP BY.\n"
        f"3. If the user asks for information on orders, include joins based on foreign key relationships.\n\n"
        f"Please provide an SQL query that matches the user’s request.\n"
        f"if user tell you to create SQLite3 qry to create table to store data please remember to not to use table names "
        f"that already in the provided schema otherwise this will make error in the system"
    )
    return prompt

def genarate_prompts_c(re_data):
    prompt_c = (
        f"Here is the dataset: {re_data}. "
        f"The necessary modules (pandas, matplotlib, and seaborn) are already imported. "
        f"Please generate a Pandas DataFrame from this data using an appropriate format based on the dataset.\n"
        f"Use the column names from the dataset to create the DataFrame, for example:\n"
        f"df = pd.DataFrame(data, columns=['CUSTOMER_NAME', 'Product_name', 'Amount_Bought'])\n"
        f"or if the dataset includes sales, use:\n"
        f"df = pd.DataFrame(data, columns=['Product_name', 'Total_Sales']) REMEMBER LAWAYS TRY TO INCLUDE ALL DATA YOU CAN CREATE SUBPLOT'S\n"
        f"Feel free to use more advanced visualizations like count plots, box plots, scatter plots, or even subplots if necessary.\n"
        f"Consider using scatter plots if there's a correlation between variables, count plots for frequency distributions, etc. "
        f"Generate subplots if the data can be split into multiple visualizations for better clarity.\n"
        f"Do not include redundant imports. Also, provide an explanation for why you chose this chart type and how it represents the data.\n"
        f"Put your explanation in a block like this: ```Explanation<your Explanation>```"
        f"if user tell you to create SQLite3 qry to create table to store data please remember to not to use table names "
        f"that already in the provided schema otherwise this will make error in the system"
    )
    return prompt_c
def genarate_prompts_w(table_schema,user_i):
    prompt=(f"Given the following table schema created using SQLite3 in a Python environment:\n\n"
            f"{table_schema}\n\n"
            f"user may ask question from this or he might ask question about other data bse related problems\n"
            f"if user ask question to create pandas dataframe and create seaborn plots please inform them to give you"
            f"the command to retrieve necessary  data from database like: example 'retrieve all items from the TEST table'\n"
            f" inform them after giving this command you can proceed with other tasks like creating table or inserting the "
            f"database\n"
            f"and here is the user input: {user_i}\n"
            f"if user request is of like getting or creating query fallow this examples:\n"
            f"1. If the user asks 'retrieve all items from the TEST table', you should return: SELECT * FROM TEST;\n"
            f"2. If the user asks 'find the total sales for each product', you should return a query that uses GROUP BY.\n"
            f"3. If the user asks for information on orders, include joins based on foreign key relationships.\n\n"
            f"Please provide an SQL query that matches the user’s request."
            f"if user tell you to create SQLite3 qry to create table to store data please remember to not to use table names "
            f"that already in the provided schema otherwise this will make error in the system"
            )
    return prompt
def genarate_prompt_s():
    prompt=(f"if you face this sinario that means user ask you to make some changes to original database (create table delete some data)\n\n"
            f"ask them if they like to make any other changes to the database or check the existing data(like pandas plot request)"
            f"if user tell you to create SQLite3 qry to create table to store data please remember to not to use table names "
            f"that already in the provided schema otherwise this will make error in the system"
            )
    return prompt
