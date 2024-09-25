# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and open the file in write mode
        with open('my_file.txt', 'w') as file:
            # Write three lines of text (including numbers)
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 42.\n")
            file.write("And this is the third line, with some more text.\n")
        print("File 'my_file.txt' created and written successfully.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Write operation completed.")

def read_and_display_file():
    try:
        # Open the file in read mode
        with open('my_file.txt', 'r') as file:
            # Read and display file contents
            content = file.read()
            print("\nReading 'my_file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Read operation completed.")

def append_to_file():
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append three more lines of text
            file.write("Appending a fourth line.\n")
            file.write("Adding a fifth line with a number: 99.\n")
            file.write("And here's the sixth line, appended to the file.\n")
        print("File 'my_file.txt' appended successfully.")
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Append operation completed.")

# Execute the functions in order
create_and_write_file()     # Task 1: Create and write to file
read_and_display_file()     # Task 2: Read and display file contents
append_to_file()            # Task 3: Append to file
read_and_display_file()     # Task 4: Read and display after appending
