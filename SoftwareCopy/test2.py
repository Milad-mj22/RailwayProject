import os

def create_folder_structure(base_path):
    try:
        # Define the nested folder structure
        folder_structure = os.path.join(base_path, "folder1", "folder2", "folder3")
        
        # Create the folder structure
        os.makedirs(folder_structure)
        
        print(f"Folder structure '{folder_structure}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the base path where you want to create the folder structure
base_path = "asd"

# Create the folder structure
create_folder_structure(base_path)
