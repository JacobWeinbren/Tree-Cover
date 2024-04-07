import json

input_file = "output/intersected_buildings.geojson"
output_prefix = "output/split/part"
max_features_per_file = 2000000

with open(input_file, "r") as file:
    geojson = json.load(file)

features = geojson["features"]
total_features = len(features)
num_files = (total_features + max_features_per_file - 1) // max_features_per_file

for i in range(num_files):
    start_index = i * max_features_per_file
    end_index = min((i + 1) * max_features_per_file, total_features)

    output_file = f"{output_prefix}{i+1:02d}.geojson"

    with open(output_file, "w") as file:
        json.dump(
            {"type": "FeatureCollection", "features": features[start_index:end_index]},
            file,
        )
