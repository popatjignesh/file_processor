# file_processor/main.py

import os
from utils.processor import FileProcessor

def get_folder_paths():
    """
    Construct the paths for the input and output folders relative to the location of this script.
    Returns a tuple containing the input and output folder paths.
    """
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the paths for input and output folders
    input_folder = os.path.join(base_dir, 'input')
    output_folder = os.path.join(base_dir, 'output')
    
    return input_folder, output_folder

if __name__ == "__main__":
    # Generate the input and output folder paths
    input_folder, output_folder = get_folder_paths()
    
    # Create the output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize the FileProcessor with the generated folder paths
    processor = FileProcessor(input_folder, output_folder)

    # Process the files
    processor.process_files()
