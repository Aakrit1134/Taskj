import tkinter as tk
def addtask():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def removetask():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
# Create the main window
root = tk.Tk()
root.title("To-Do List")
# Create widgets
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=addtask)
remove_button = tk.Button(root, text="Remove Task", command=removetask)
task_list = tk.Listbox(root)
# Place widgets in the window
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
task_list.pack()
# Start the main loop
root.mainloop()
