import psutil
import tkinter as tk

def show_open_files():
    # Get all running processes
    processes = psutil.process_iter(['pid', 'name'])

    # Create a dictionary to store open files for each process
    open_files = {}

    # Loop through each process
    for process in processes:
        try:
            # Get a list of open files for the process
            files = process.open_files()

            # Add the list of open files to the dictionary
            open_files[process.pid] = files
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Create a Tkinter window to display the results
    root = tk.Tk()
    root.title('Open Files')

    # Create a text widget to display the results
    text = tk.Text(root)
    text.pack()

    # Loop through each process and its open files
    for pid, files in open_files.items():
        # Add the process name to the text widget
        text.insert(tk.END, f'Process: {psutil.Process(pid).name()}\n')

        # Loop through each file and add it to the text widget
        for file in files:
            text.insert(tk.END, f'  {file.path}\n')

        # Add a blank line between processes
        text.insert(tk.END, '\n')

    # Start the Tkinter event loop
    root.mainloop()

show_open_files()