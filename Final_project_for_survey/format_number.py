import pandas as pd

# Read the combined CSV file
df = pd.read_csv("users_data_combined.csv")

# Print the current phone numbers in the column
print("Before cleaning:")
print(df['☎️ Tel. raqamingiz:'])

# Function to clean and format phone numbers
def format_phone_number(phone_number):
    # Convert to string to ensure all are treated as strings
    phone_number = str(phone_number)
    
    # Remove non-numeric characters (spaces, hyphens, parentheses, etc.)
    phone_number = ''.join(filter(str.isdigit, phone_number))
    
    # If the number has fewer than 9 digits, replace it with an empty string
    if len(phone_number) < 9:
        phone_number = ''
    else:
        # Cut the last 9 digits and prepend '+998'
        phone_number = '+998' + phone_number[-9:]
    
    return phone_number

# Apply the function to the '☎️ Tel. raqamingiz:' column
df['☎️ Tel. raqamingiz:'] = df['☎️ Tel. raqamingiz:'].apply(format_phone_number)

# Print the cleaned phone numbers
print("After cleaning:")
print(df['☎️ Tel. raqamingiz:'])

# Save the cleaned data back to a CSV file
df.to_csv("users_data_combined_cleaned.csv", index=False)

print("✅ Cleaned data saved to users_data_combined_cleaned.csv")
