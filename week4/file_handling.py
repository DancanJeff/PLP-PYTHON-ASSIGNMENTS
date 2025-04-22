def process_file():
    try:
        # Get input filename from user
        input_filename = input("Enter the name of the input file: ")
        
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Process the content (convert to uppercase)
        modified_content = content.upper()
        
        # Get output filename from user
        output_filename = input("Enter the name of the output file: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully processed {input_filename} and saved to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    process_file()