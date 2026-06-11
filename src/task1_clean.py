import pandas as pd

# Load original file from data folder
df = pd.read_excel("data/business_leads_50_complete.xlsx")

original_count = len(df)
print(f"Original rows: {original_count}")

# Remove duplicates
df = df.drop_duplicates(subset=["Company Name"])
print(f"After removing duplicates: {len(df)}")

# Remove missing websites
df = df.dropna(subset=["Website"])
print(f"After removing missing websites: {len(df)}")

# Standardize country names
country_map = {
    "USA": "United States",
    "Canada": "Canada",
    "UAE": "United Arab Emirates"
}
df["Country"] = df["Country"].replace(country_map)

# Ensure Contact Page values are Yes/No
df["Contact Page"] = df["Contact Page"].apply(lambda x: "Yes" if str(x).lower() == "yes" else "No")

# Standardize Lead Quality
quality_map = {"high": "High", "medium": "Medium", "low": "Low"}
df["Lead Quality"] = df["Lead Quality"].apply(lambda x: quality_map.get(str(x).lower(), "Medium"))

# Save cleaned dataset in data folder
df.to_csv("data/cleaned_leads.csv", index=False)

print(f"\n✅ cleaned_leads.csv saved in data/ folder")
print(f"Final records: {len(df)}")
print(f"Records removed: {original_count - len(df)}")