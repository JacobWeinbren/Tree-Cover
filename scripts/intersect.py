import geopandas as gpd


def filter_lsoa_geojson(input_file, output_file):
    print(f"Loading GeoJSON file: {input_file}")
    gdf = gpd.read_file(input_file)

    # Filter features with 'cover' and 'income' properties
    filtered_gdf = gdf[gdf.columns.intersection(["cover", "income", "geometry"])]

    # Save the filtered GeoJSON file
    filtered_gdf.to_file(output_file, driver="GeoJSON", decimal=6)
    print(f"Filtered GeoJSON saved to: {output_file}")


def intersect_buildings(lsoa_file, buildings_file, output_file):
    print(f"Loading GeoJSON files: {lsoa_file} and {buildings_file}")
    lsoa_gdf = gpd.read_file(lsoa_file)
    buildings_gdf = gpd.read_file(buildings_file)

    # Perform the intersection
    print("Performing intersection...")
    intersection = gpd.overlay(buildings_gdf, lsoa_gdf, how="intersection")

    # Save the intersected buildings to a new GeoJSON file
    intersection.to_file(output_file, driver="GeoJSON", decimal=6)
    print(f"Intersected buildings saved to: {output_file}")


if __name__ == "__main__":
    input_file = "output/LSOA_tree_IMD.geojson"
    filtered_output_file = "output/filtered_LSOA.geojson"
    buildings_file = "source/buildings.geojson"
    intersected_output_file = "output/intersected_buildings.geojson"

    # Filter LSOA_tree_IMD.geojson
    filter_lsoa_geojson(input_file, filtered_output_file)

    # Intersect buildings with filtered LSOA_tree_IMD.geojson
    intersect_buildings(filtered_output_file, buildings_file, intersected_output_file)
