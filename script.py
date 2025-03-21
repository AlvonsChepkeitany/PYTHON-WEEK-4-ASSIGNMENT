# Function for reading and modifying the contents of a file
def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (this example adds a line to the content)
        modified_content = content + "\n\n-- File processed successfully!"

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been processed and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function for error handling when asking the user for a filename
def get_filename():
    filename = input("Please enter the filename you want to open: ")

    try:
        # Attempt to open the file for reading
        with open(filename, 'r') as file:
            print(f"File '{filename}' opened successfully.")
            content = file.read()
            print(f"File contents:\n{content}")
            return filename  # If the file is opened successfully, return the filename
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Main program execution
if __name__ == "__main__":
    print("Welcome to the File Handling and Exception Handling Lab!")

    # Asking for a file and handling errors
    filename = get_filename()

    if filename:
        # Process the file and write the modified content to a new file
        new_filename = "modified_" + filename
        modify_file(filename, new_filename)
