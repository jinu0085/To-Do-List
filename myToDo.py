import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To Do List")
root.geometry('500x500')

TaskList = []  #List for Task
checkbox_vars = []

#Label for user instruction
labelText = tk.Label(root, text="Enter Your Task", font=("Arial", 14))
labelText.place(x=180, y=15)

#Text box for user input
user_InputS = tk.Text(root, height=5, width=30)
user_InputS.place(x=130, y=50)

def showTask():
    labelShowTask = tk.Label(root, text="Your Tasks", font=("Arial", 14))
    labelShowTask.place(x=30, y=220)
    y_Position = 255
    for task in TaskList:
        var = tk.BooleanVar()
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(root, text=task, variable=var, font=("Arial", 12, "bold"), background="White")
        checkbox.place(x=30, y=y_Position)
        y_Position += 30
    SCREEN_SCROLL()

def TaskCheck():  #Func. to check Task box activity
    checkInput = user_InputS.get("1.0", "end-1c").strip()
    if not checkInput:
        messagebox.showerror("Error", "Please enter Task!")
    else:
        TaskList.append(checkInput)
        user_InputS.delete("1.0", "end")
        y_Position = 255
        for task in TaskList:
            var = tk.BooleanVar()
            checkbox_vars.append(var)
            checkbox = tk.Checkbutton(root, text=task, variable=var, font=("Arial", 12, "bold"), background="White")
            checkbox.place(x=30, y=y_Position)
            y_Position += 30
        messagebox.showinfo("Information", "Task Added")
        print(TaskList)

#def SCREEN_SCROLL():
 #   root.bind("<MouseWheel>")




#Buttons
AddButton = tk.Button(root, text="Add Task", command=TaskCheck, font=("Arial", 12 ))
AddButton.place(x=100, y=160)

ShowTask = tk.Button(root, text="Show My Task", command=showTask, font=("Arial", 12 ))
ShowTask.place(x=200, y=160)






root.mainloop()
