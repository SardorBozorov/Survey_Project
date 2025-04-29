import pandas as pd
import re

df = pd.read_csv(
    r"users_data_combined_cleaned.csv",
    keep_default_na=False,
    encoding='utf-8',
    dtype={'☎️ Tel. raqamingiz:': str}  # Replace with your actual column name
)


def clean_name(name):
    name = str(name).strip()

    # Check for numbers or invalid characters
    if re.search(r"[^a-zA-Zа-яА-ЯёЁқҚўЎғҒ\s'-]", name):
        return "Invalid Name"


    # Capitalize each word
    return ' '.join(word.capitalize() for word in name.split())

# Apply the function to your name column (replace with your actual column name)
df['👤 Ism-familiyangiz:'] = df['👤 Ism-familiyangiz:'].apply(clean_name)

# Save the cleaned DataFrame back
df.to_csv("users_data_names_cleaned.csv", index=False)

print("✅ Name column cleaned and saved.")


