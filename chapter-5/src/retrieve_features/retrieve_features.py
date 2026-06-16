from feast import FeatureStore
import pandas as pd
from pathlib import Path
from feast.repo_config import FeastConfigError
from pydantic import ValidationError
import argparse
import os


def init_feature_store(
    file_name: str
) -> FeatureStore:
    # Download the content of the feature_store.yaml from the GCS bucket

    
    
    config_path = Path("./") / "feature_store.yaml"
    try:
        store = FeatureStore(repo_path=".", fs_yaml_file=config_path)
    except ValidationError as e:
        raise FeastConfigError(e, config_path)
    return store


def get_features(
    file_name: str,
    entity_df: str,
    feature_list: str,
    data_output: str,
):
    store = init_feature_store(file_name)
    print("Feature store initialized")
    feature_list = feature_list.split(",")
    print("Requested features:", feature_list)
    print(entity_df)
    entity_df = pd.read_parquet(entity_df)
    print("Entity DataFrame head:")
    print(entity_df.head())
    feature_df = store.get_historical_features(
        entity_df=entity_df,
        features=feature_list,
    ).to_df()
    print("Retrieved historical features:")
    print(feature_df.head())
    Path(data_output).parent.mkdir(parents=True, exist_ok=True)
    feature_df.to_parquet(data_output)


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Retrieve features from Feast")
    parser.add_argument("--minio_host", type=str, required=True, help="Minio host URL")

    parser.add_argument(
        "--file_name", type=str, required=True, help="File name to download"
    )
    parser.add_argument(
        "--entity_df", type=str, required=True, help="Input path for the Dataset"
    )
    parser.add_argument(
        "--feature_list", type=str, required=True, help="List of features to retrieve"
    )
    parser.add_argument(
        "--data_output", type=str, required=True, help="Output path for the Dataset"
    )
    args = parser.parse_args()

    # Call the get_features function with parsed arguments
    get_features(
        file_name=args.file_name,
        entity_df=args.entity_df,
        feature_list=args.feature_list,
        data_output=args.data_output,
    )


if __name__ == "__main__":
    main()