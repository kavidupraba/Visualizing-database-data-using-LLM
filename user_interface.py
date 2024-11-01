import tkinter as tk
from tkinter import scrolledtext
from call_handler import create_fist_prompt,sending_chart_request,showing_the_charts,getting_information,prompt_without_sql_request
from gemini import __chat__
from checking_user_input_and_response import classify_user_input

root=tk.Tk()
root.title("SQL chart generator")
root.geometry("600x600")
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

conversation_box=scrolledtext.ScrolledText(root,width=60,height=20,wrap=tk.WORD)
conversation_box.grid(row=0,column=0,padx=10,pady=10,columnspan=2,sticky="nsew")
conversation_box.insert(tk.END,"Welcome! Ask me anything about SQL or chart generation.\n")
conversation_box.tag_config("you",foreground="blue")
conversation_box.tag_config("system",foreground="green")

def handler():
    #n=1
    #m=2
    #result=n+m
    #conversation_box.delete(1.0,'end')
    #conversation_box.insert(1.0,f'{result}')
    user_input=user_entry.get()
    ch=classify_user_input(user_input)
    match ch:
        case "sql":
            conversation_box.insert(tk.END,f"\nyou: {user_input}","you")
            first_prompt=create_fist_prompt(user_input)
            response_s=__chat__(first_prompt)
            user_entry.delete(0,'end')


            #conversation_box.insert(tk.END,f"system: {response_s}")


            prompt_c,re_data=sending_chart_request(response_s)
            if re_data!=None:
                conversation_box.insert(tk.END,f"\nsystem retrieved data: {re_data}\n","system")
            response_c=__chat__(prompt_c)
            Explanation = getting_information(response_c)
            conversation_box.insert(tk.END, f"\nsystem: {Explanation}\n\n","system")
            showing_the_charts(response_c)
        case "normal":
            conversation_box.insert(tk.END,f"\nyou: {user_input}","you")
            prompt_n=prompt_without_sql_request(user_input)
            response_w=__chat__(prompt_n)
            conversation_box.insert(tk.END,f"\nsystem: {response_w}\n\n","system")







user_entry=tk.Entry(root,width=50,)
user_entry.grid(row=1,column=0,padx=10,pady=10,sticky="ew")
submit_button=tk.Button(root,text="Enter",command=lambda:handler(),font=('Arial,14'))
submit_button.grid(row=1,column=1,padx=10,pady=10)
root.bind('<Return>', lambda event: submit_button.invoke())
root.mainloop()