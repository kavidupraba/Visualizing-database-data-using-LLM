
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
        f"Please provide an SQL query that matches the user’s request."
    )
    return prompt

def genarate_prompts_c(re_data):
    prompt_c = (
        f"Here is the dataset: {re_data}. "
        f"The necessary modules (pandas, matplotlib, and seaborn) are already imported. "
        f"Please generate a Pandas DataFrame from this data using the following format:\n"
        f"df = pd.DataFrame(data, columns=['Product_name', 'Total_Sales'])\n"
        f"Create a Seaborn bar chart from the DataFrame (sns.barplot), set the x-axis as 'Product_name' and y-axis as 'Total_Sales'. "
        f"Make sure to label the chart appropriately with titles and axis labels, and finally display the chart using plt.show(). "
        f"Do not include redundant imports"
    )
    return prompt_c
