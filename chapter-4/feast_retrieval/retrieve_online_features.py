from feast import FeatureStore

store = FeatureStore(repo_path="../feast", fs_yaml_file="../feast/feature_store.yaml")
online_features = store.get_online_features(
    features=[
        "demographic:Sex",
    ],
    entity_rows=[
        {"user_id": "9f2ac416-06e1-44a0-87bd-d4787c85bf66"},
    ]
)
print(online_features.to_df())