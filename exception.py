def main():
    try:
        # Ask the user for the input file name
        input_file_name = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the input file
        with open(input_file_name, 'r') as input_file:
            content = input_file.readlines()
        
        # Modify the content (example: convert to uppercase)
        modified_content = [line.upper() for line in content]
        
        # Ask the user for the output file name
        output_file_name = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the output file
        with open(output_file_name, 'w') as output_file:
            output_file.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file_name}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")

if __name__ == "__main__":
    main()