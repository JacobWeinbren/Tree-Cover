import pandas as pd
import ujson

# Read the Excel files
tree_cover_df = pd.read_excel(
    "source/tree-cover.xlsx", sheet_name="neighbourhoods and tree cover "
)
deprivation_df = pd.read_excel("source/domains.xlsx", sheet_name="IoD2019 Domains")

# Rename columns for consistency in deprivation data
deprivation_df = deprivation_df.rename(
    columns={
        "LSOA code (2011)": "LSOA code",
        "Income Rank (where 1 is most deprived)": "Income Rank",
    }
)

# Merge the tree cover and deprivation data on LSOA code
combined_df = tree_cover_df[["LSOA code", "Tree_canopy_cover_%"]].merge(
    deprivation_df[["LSOA code", "Income Rank"]], on="LSOA code", how="inner"
)

# Load the GeoJSON file
with open("source/LSOAs.geojson", "r") as file:
    geojson_data = ujson.load(file)

# Update GeoJSON features with tree cover and Income Rank
for feature in geojson_data["features"]:
    lsoa_code = feature["properties"]["LSOA11CD"]
    row = combined_df[combined_df["LSOA code"] == lsoa_code]
    if not row.empty:
        cover_value = row["Tree_canopy_cover_%"].values[0]
        if cover_value != "No data":
            feature["properties"]["cover"] = float(cover_value)
        else:
            feature["properties"]["cover"] = None
        feature["properties"]["income"] = int(row["Income Rank"].values[0])

# Save the updated GeoJSON file
with open("output/LSOA_tree_IMD.geojson", "w") as file:
    ujson.dump(geojson_data, file, indent=4)
