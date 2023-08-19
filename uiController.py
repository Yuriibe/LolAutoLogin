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
    # Create a Frame widget with the desired background color
    frame = Frame(root, bg="#23283c")
    frame.place(x=100, y=100, width=800, height=400)

    # Create a Canvas widget with the desired background color
    canvas = Canvas(frame, bg="#23283c", bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    # Create a Treeview widget for the table
    tree = ttk.Treeview(canvas, columns=("Play", "Region", "Username", "IGN", "Rank", "Winrate"), show="headings")

    # Set the column headings
    tree.heading("Play", text="Play", anchor=W)
    tree.heading("Region", text="Region", anchor=W)
    tree.heading("Username", text="Username", anchor=W)
    tree.heading("IGN", text="IGN", anchor=W)
    tree.heading("Rank", text="Rank", anchor=W)
    tree.heading("Winrate", text="Winrate", anchor=W)

    # Set the column widths
    tree.column("Play", width=150, anchor=W)
    tree.column("Region", width=50, anchor=W)
    tree.column("Username", width=100, anchor=W)
    tree.column("IGN", width=150, anchor=W)
    tree.column("Rank", width=50, anchor=W)
    tree.column("Winrate", width=100, anchor=W)

    # Insert data into the table
    for i, account in enumerate(data):
        tree.insert("", i, values=(account["play"], account["region"], account["username"], account["ign"], "", ""),
                    tags=("play_button",))

    selected_index = None
    tree.tag_bind("play_button", "<ButtonRelease-1>", lambda event: assign_index(play_button_clicked(event)))
    # Position and pack the Treeview widget into the window
    canvas.create_window((0, 0), window=tree, anchor=NW)

    # Style the Treeview widget
    style = ttk.Style()
    style.configure("Treeview", background="#23283c", foreground="white", fieldbackground="#23283c", font=("Arial", 12))
    style.configure("Treeview.Heading", background="#23283c", foreground="white", fieldbackground="#23283c", font=("Arial", 14, "bold"))



def assign_index(index):
    global selected_index
    selected_index = index
    print(selected_index)


def open_modal():
    # Create a new Toplevel window
    addAcountModal = Toplevel(root)
    addAcountModal.title("Add new Account")
    addAcountModal.geometry("400x700")
    addAcountModal.transient(root)  # Make the modal a transient window of the root window
    addAcountModal.grab_set()  # Make the modal window modal

    # Add a label to the modal window
    label = Label(addAcountModal, text="This is a modal window.")
    label.pack(pady=20)

    # Add a button to close the modal window
    def close_modal():
        addAcountModal.destroy()

    close_button = Button(addAcountModal, text="Close", command=close_modal)
    close_button.pack(pady=20)
    createRegionSelection(addAcountModal)
    createUserDataInput(addAcountModal)
def updateAccountTable():
    # Clear the Treeview widget
    tree.delete(*tree.get_children())

    # Insert the updated data into the Treeview widget
    for i, account in enumerate(userData):
        tree.insert("", i, values=(account["play"], account["region"], account["username"], account["ign"], "", ""),
                    tags=("play_button",))
def createUserDataInput(addAcountModal):
    def gather_inputs():
        # Gather the input values
        username_value = usernameEntry.get()
        password_value = passwordEntry.get()
        summoner_value = summonerEntry.get()
        region_value = regionVariable.get()

        # Add the input values to a dictionary
        enteredUserData = {
            "play": "▶",
            "username": username_value,
            "password": password_value,
            "summoner": summoner_value,
            "region": region_value,
            "ign": "test",
         #   "rank": "iron V",
          #  "winrate": "0%"
        }

        userData.append(enteredUserData)
        dict_string = str(userData)
        # Write the string representation of the dictionary to a Python file
        with open("loginData.py", "w", encoding="utf-8") as file:
            file.write("userData = " + dict_string)
        updateAccountTable()
        addAcountModal.destroy()





    usernameLabel = StringVar()
    usernameLabel.set("Username:")
    labelUsername = Label(addAcountModal, textvariable=usernameLabel, height=4)
    labelUsername.pack()
    usernameEntry = Entry(addAcountModal, width=40)
    usernameEntry.focus_set()
    usernameEntry.pack()

    passwordLabel = StringVar()
    passwordLabel.set("Password:")
    labelPassword = Label(addAcountModal, textvariable=passwordLabel, height=4)
    labelPassword.pack()
    passwordEntry = Entry(addAcountModal, width=40)
    passwordEntry.focus_set()
    passwordEntry.pack()

    summonerLabel = StringVar()
    summonerLabel.set("Summoner name:")
    labelsummoner = Label(addAcountModal, textvariable=summonerLabel, height=4)
    labelsummoner.pack()
    summonerEntry = Entry(addAcountModal, width=40)
    summonerEntry.focus_set()
    summonerEntry.pack()

    # Create a Button to validate Entry Widget
    ttk.Button(addAcountModal, text="Okay", width=20, command=gather_inputs).pack(pady=20)

def createRegionSelection(addAcountModal):
    OPTIONS = [
        "EUW",
        "EUN",
        "NA",
        "LAN",
        "KR",
        "TR",
    ]  # etc

    global regionVariable
    regionVariable = StringVar(addAcountModal)
    regionVariable.set(OPTIONS[0])  # default value

    w = OptionMenu(addAcountModal, regionVariable, *OPTIONS)
    w.pack()

button = Button(root, text="Add Account!", command=open_modal)
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
