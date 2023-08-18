import tkinter
from tkinter import *
from tkinter import ttk
from loginData import userData

root = Tk()
root.configure(bg='#23283c')
windowWidth = 1000
windowHeight = 600
root.geometry(f"{windowWidth}x{windowHeight}")
# Remove the default title bar
root.overrideredirect(True)
icon = None

def close_window():
    root.destroy()

def minimize_window():
    root.withdraw()
    taskbar_window.iconify()

def restore_window(event=None):
    root.deiconify()
    taskbar_window.withdraw()

def createCustomTitlebar():
    global icon  # Use the global icon variable
    # Create a custom title bar
    titleBar = Frame(root, bg='#23283c')
    titleBar.place(x=0, y=0, width=windowWidth, height=40)

    icon = PhotoImage(file="images/titlebarIcon.png")
    icon = icon.subsample(3)

    iconLabel = Label(titleBar, image=icon, bg='#23283c')
    iconLabel.pack(side=LEFT, padx=10)

    # Add a label to the title bar
    titleLabel = Label(titleBar, text='LoL Account Manager 1.0.0', bg='#23283c', fg='white')
    titleLabel.pack(side=LEFT)

    # Add a close button to the title bar
    close_button = Button(titleBar, text='X', bg='#282e48', fg='white', command=close_window)
    close_button.pack(side=RIGHT, padx=10)

    # Add a minimize button to the title bar
    minimize_button = Button(titleBar, text='-', bg='#282e48', fg='white', command=minimize_window)
    minimize_button.pack(side=RIGHT)

    titleBar.bind('<Button-1>', on_click)
    titleBar.bind('<B1-Motion>', on_drag)

# Bind the mouse events for dragging the window
def on_click(event):
    root._offset_x = event.x_root - root.winfo_x()
    root._offset_y = event.y_root - root.winfo_y()

def on_drag(event):
    x, y = event.x_root - root._offset_x, event.y_root - root._offset_y
    root.geometry(f"+{x}+{y}")

def play_button_clicked(event):
    global tree  # Add this line
    item = tree.selection()[0]
    index = tree.index(item)
    print(f"Play button clicked for item: {tree.item(item)['values']} ")
    return index

def createAccountTable(data):
    global tree  # Add this line
    # Create a Treeview widget for the table
    tree = ttk.Treeview(root, columns=("Play", "Region", "Username", "IGN", "Rank", "Winrate"), show="headings")

    # Set the column headings
    tree.heading("Play", text="Play")
    tree.heading("Region", text="Region")
    tree.heading("Username", text="Username")
    tree.heading("IGN", text="IGN")
    tree.heading("Rank", text="Rank")
    tree.heading("Winrate", text="Winrate")

    # Set the column widths
    tree.column("Play", width=150)
    tree.column("Region", width=50)
    tree.column("Username", width=100)
    tree.column("IGN", width=150)
    tree.column("Rank", width=50)
    tree.column("Winrate", width=100)

    # Insert data into the table
    for i, account in enumerate(data):
        tree.insert("", i, values=("", account["region"], account["username"], account["ign"], "", ""), tags=("play_button",))

    selected_index = None
    tree.tag_bind("play_button", "<ButtonRelease-1>", lambda event: assign_index(play_button_clicked(event)))
    # Position and pack the Treeview widget into the window
    tree.place(x=100, y=100, width=800, height=400)

def assign_index(index):
    global selected_index
    selected_index = index
    print(selected_index)

def open_modal():
    # Create a new Toplevel window
    modal = Toplevel(root)
    modal.title("Modal Window")
    modal.geometry("300x200")
    modal.transient(root)  # Make the modal a transient window of the root window
    modal.grab_set()  # Make the modal window modal

    # Add a label to the modal window
    label = Label(modal, text="This is a modal window.")
    label.pack(pady=20)

    # Add a button to close the modal window
    def close_modal():
        modal.destroy()

    close_button = Button(modal, text="Close", command=close_modal)
    close_button.pack(pady=20)


button = Button(root, text="Click me!", command=open_modal)
button.place(x=450, y=510)


# Create a secondary window for the taskbar
taskbar_window = Toplevel(root)
taskbar_window.geometry('1x1+0+0')
taskbar_window.withdraw()
taskbar_window.title('Account Manager')
taskbar_window.protocol('WM_DELETE_WINDOW', restore_window)
taskbar_window.bind('<Map>', restore_window)
taskbar_window.iconbitmap('images/titlebar.ico')

createAccountTable(userData)
createCustomTitlebar()

root.mainloop()
