import pandas as pd

# Base sheet ID
sheet_id = "1eMfrkIEZgZ4lUwM6lMVY5Cy_YS3FIfmjmOatr5cWgtA"

# Export URLs for both sheets
csv_export_url_ru = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=888619976"  # usually the first sheet
csv_export_url_uz = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=998439754"

# Load both into DataFrames
df_ru = pd.read_csv(csv_export_url_ru)
df_uz = pd.read_csv(csv_export_url_uz)

# Save both locally
df_ru.to_csv("users_data_ru.csv", index=False)
df_uz.to_csv("users_data_uz.csv", index=False)

# # Print both
# print("🇷🇺 Russian Data:\n", df_ru.head())
# print("🇺🇿 Uzbek Data:\n", df_uz.head())

