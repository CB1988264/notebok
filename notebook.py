import time


def open_notebook(notebook_file="notebook.txt", mode="r"):
    try:
        notebook = open(notebook_file, mode)
        return notebook
    except FileNotFoundError:
        if (notebook_file != "notebook.txt"):
            print("No notebook with that name detected, created one.")
            notebook = open(notebook_file, "w")
            return notebook
        else:
            print("No default notebook was found, created one.")
            notebook = open(notebook_file, "w")
            return notebook


def main():
    selection = 0
    notebook_file = "notebook.txt"
    open_notebook()
    while selection != 5:
        print("Now using file", notebook_file)
        print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit\n""")

        selection = int(input("Please select one: "))
        if selection == 1:
            notebook = open_notebook(notebook_file)
            content = notebook.read()
            notebook.close()
            print(content)
        elif selection == 2:
            note = input("Write a new note: ")
            notebook = open_notebook(notebook_file, "a")
            notebook.write(note + ":::" + time.strftime("%X %x") + "\n")
            notebook.close()
        elif selection == 3:
            notebook = open_notebook(notebook_file, "w")
            notebook.close()
            print("Notes deleted.")
        elif selection == 4:
            notebook_file = input("Give the name of the new file: ")
            notebook = open_notebook(notebook_file)
            notebook.close()
    print("Notebook shutting down, thank you.")


if __name__ == "__main__":
    main()