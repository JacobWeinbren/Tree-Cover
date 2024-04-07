import pandas as pd

# Read the tree cover data
tree_cover_df = pd.read_excel(
    "source/tree-cover.xlsx", sheet_name="neighbourhoods and tree cover "
)

# Read the deprivation data
deprivation_df = pd.read_excel(
    "source/domains.xlsx",
    sheet_name="IoD2019 Domains",
)

# Rename columns for consistency
deprivation_df.rename(
    columns={
        "LSOA code (2011)": "LSOA code",
        "Income Rank (where 1 is most deprived)": "IMD rank",
    },
    inplace=True,
)
tree_cover_df.rename(columns={"Tree_canopy_cover_%": "tree cover"}, inplace=True)

print(tree_cover_df.columns)
print(deprivation_df.columns)

# Merge the dataframes on LSOA code
combined_df = pd.merge(
    tree_cover_df[["LSOA code", "tree cover"]],
    deprivation_df,
    on="LSOA code",
    how="inner",
)

# Save the combined data to a new CSV file
combined_df.to_csv("output/combined_data.csv", index=False)
