import os
import ujson as json

input_directory = "output/split"
output_file = "output/simplified_buildings.geojson"

print("Listing simplified GeoJSON files...")
simplified_files = [
    file
    for file in os.listdir(input_directory)
    if file.startswith("simplified_part") and file.endswith(".geojson")
]

merged_features = []

print("Processing files...")
for file in simplified_files:
    file_path = os.path.join(input_directory, file)
    print(f"Reading {file}...")
    with open(file_path, "r") as f:
        geojson_data = json.load(f)

    for feature in geojson_data["features"]:
        for key in ["fid", "id", "feature_code"]:
            feature["properties"].pop(key, None)
        if (
            "cover" in feature["properties"]
            and feature["properties"]["cover"] is not None
        ):
            feature["properties"]["cover"] = round(feature["properties"]["cover"], 2)

    merged_features.extend(geojson_data["features"])

merged_geojson = {"type": "FeatureCollection", "features": merged_features}

print("Writing merged GeoJSON...")
with open(output_file, "w") as f:
    json.dump(merged_geojson, f)

print(f"Merged GeoJSON file saved as {output_file}")
