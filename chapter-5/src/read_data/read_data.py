import pandas as pd
import os
import argparse
from pathlib import Path

def get_data(file_name:str, data_output_path:str):
    """
    Reads a DataFrame and saves it as Parquet file. 
    
    Args: 
        file_name (str): The name of the file to read.
        data_output_path (str): The path where the Parquet file will be saved.
    """
    
    local_temp_file = os.path.join("./temp", file_name)
    
    
    # Load the Parquet file into a DataFrame
    print(f"Reading the downloaded file {local_temp_file}...")
    df = pd.read_parquet(local_temp_file)

    # Save the DataFrame as a parquet file in the specified output path
    print(f"Saving the processed data to {data_output_path}...")
    Path(data_output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(data_output_path)
    
    print("Data saved successfully.")
    

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Download data and save as a Dataset."
    )
    parser.add_argument(
        "--file_name", type=str, required=True, help="File name to download"
    )
    parser.add_argument(
        "--data_output_path",
        type=str,
        required=True,
        help="Output path for the Dataset",
    )

    args = parser.parse_args()

    # Call the get_data function with parsed arguments
    get_data(
        file_name=args.file_name,
        data_output_path=args.data_output_path,
    )


if __name__ == "__main__":
    main()