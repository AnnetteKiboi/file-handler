# File Read & Write with Error Handling

def modify_content(content):
    """
    A simple function to modify file content.
    For example, convert all text to uppercase.
    """
    return content.upper()


def process_file():
    try:
        # Ask user for the filename
        input_filename = input("Enter the name of the file to read: ")

        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content
        modified_content = modify_content(content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don`t have access to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
process_file()
