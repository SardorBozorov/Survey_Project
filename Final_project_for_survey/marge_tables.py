import pandas as pd

# Read the first CSV file (RU) with the header
df_ru = pd.read_csv("users_data_ru.csv", header=None)

# Read the second CSV file (UZ) without headers (we assume it has the same structure as the first one)
df_uz = pd.read_csv("users_data_uz.csv")

# Set the column names of the second dataframe (UZ) to be the same as the first dataframe (RU)
df_ru.columns = df_uz.columns

# Append the second DataFrame (UZ) to the first (RU)
df_combined = pd.concat([df_uz, df_ru], ignore_index=True)

# Save the combined DataFrame to a new CSV file without additional headers
df_combined.to_csv("users_data_combined.csv", index=False)

print("✅ Combined data saved to users_data_combined.csv")
print(df_combined.head())
