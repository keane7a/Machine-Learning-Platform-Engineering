import pandas as pd  # Updated imports for KFP v2
import argparse


def write_data(
    file_name: str,
    input_data_path: str,  # Updated type hint for KFP v2
):
    # Load input data from the artifact path
    input_data = pd.read_parquet(
        input_data_path
    )  # KFP v2 uses `.path` for artifact inputs
    input_data.to_parquet(file_name, index=False)

    # Upload the file
    


def main():
    parser = argparse.ArgumentParser(description="Upload data to MinIO.")
    parser.add_argument("--file_name", type=str, help="Name of the file to upload")
    parser.add_argument("--input_data_path", type=str, help="Path to the input data")

    args = parser.parse_args()

    write_data(
        file_name=args.file_name,
        input_data_path=args.input_data_path,
    )


if __name__ == "__main__":
    main()