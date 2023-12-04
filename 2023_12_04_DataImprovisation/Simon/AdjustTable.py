import pandas as pd
import pycountry

# Load the .tsv file into a pandas DataFrame
df = pd.read_csv('2023_12_04_DataImprovisation/countries.txt', sep='\t')

# Dictionary to map specific country names to ISO-3 codes
country_name_to_iso3 = {
    "Bolivia": "BOL",
    "Cape Verde": "CPV",
    "Congo, Republic of the": "COG",
    "Czech Republic": "CZE",
    "Democratic People's Republic of Korea": "PRK",
    "Democratic Republic of the Congo": "COD",
    "Libyan Arab Jamahiriya": "LBY",
    "Moldova": "MDA",
    "Republic of Korea": "KOR",
    "Swaziland": "SWZ",
    "The former Yugoslav Republic of Macedonia": "MKD",
    "United Kingdom of Great Britain and Northern Ireland": "GBR",
    "United Republic of Tanzania": "TZA",
    "United States of America": "USA",
    "Vatican": "VAT"
}

# Function to convert country names to ISO-3 format
def convert_to_iso3(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except AttributeError:
        return country_name_to_iso3.get(country_name, 'Not found')

# Apply the function to the 'Name' column to create a new column with ISO-3 country codes
df['ISO-3'] = df['Name'].apply(convert_to_iso3)

# Add numeric values for colors
color_mapping = {"green": 0, "orange": 0.5, "red": 1}
df['Color_value'] = df['Code'].map(color_mapping)

# Text mapping
text_mapping = {"green": "OK", "orange": "Oh no ...", "red": "Fucked up!"}
df['Text'] = df['Code'].map(text_mapping)

# Save the DataFrame back to a .tsv file
df.to_csv('2023_12_04_DataImprovisation/Simon/countries_with_iso3.csv', index=False)