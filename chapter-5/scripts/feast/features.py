from feast import FileSource, FeatureView, Field
from feast.data_format import ParquetFormat
from feast.types import String
from entity import user
from datetime import timedelta

demo_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="./data/demographic_features.parquet"
)

relationship_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="./data/relationship_features.parquet",
)

occupational_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="./data/occupational_features.parquet",
)

demo_features = FeatureView(
    name="demographic", 
    entities=[user], 
    schema=[
        Field(name="Native_country", dtype=String), 
        Field(name="Sex", dtype=String), 
        Field(name="Race", dtype=String),
    ],
    ttl=timedelta(days=365), 
    source=demo_features_parquet_file_source, 
    tags={
        "authors": "Alice, Bob, Charlie", 
        "description": "User Demographics",
        "used_by": "Income_Calculation_Team"
    }
)

relationship_features = FeatureView(
    name="relationship",
    entities=[user],
    schema=[
        Field(name="Relationship", dtype=String),
        Field(name="Marital-Status", dtype=String),
    ],
    ttl=timedelta(days=365),
    source=relationship_features_parquet_file_source,
    tags={
        "authors": "Alice",
        "description": "User Relationship Info",
        "used_by": "Income_Calculation_Team",
    },
)

occupational_features = FeatureView(
    name="occupation",
    entities=[user],
    schema=[
        Field(name="Workclass", dtype=String),
        Field(name="Education", dtype=String),
        Field(name="Occupation", dtype=String),
    ],
    ttl=timedelta(days=365),
    source=occupational_features_parquet_file_source,
    tags={
        "authors": "Bob",
        "description": "User Occupation Information",
        "used_by": "Income_Calculation_Team",
    },
)