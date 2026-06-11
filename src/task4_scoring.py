import pandas as pd

# Load the feature-engineered dataset
df = pd.read_csv("data/ml_ready_dataset.csv")

# Calculate score based on rules
score = 0
score += df["website_exists"] * 10      # Website available: +10
score += df["contact_form"] * 20         # Contact form: +20

# Country score: USA=15, Canada=10, UAE=5
country_points = df["country_score"].map({3: 15, 2: 10, 1: 5}).fillna(5)
score += country_points

# Services count > 3: +15
score += (df["services_count"] > 3).astype(int) * 15

# About word count > 100: +10
score += (df["about_word_count"] > 100).astype(int) * 10

df["Lead Score"] = score

# Classify leads
def classify(score):
    if score >= 60:
        return "High"
    elif score >= 35:
        return "Medium"
    else:
        return "Low"

df["Predicted Lead Class"] = df["Lead Score"].apply(classify)

# Save to data folder
df.to_csv("data/scored_leads.csv", index=False)

print(" scored_leads.csv saved in data/ folder")
print("\nFirst 5 scored leads:")
print(df[["Company Name", "Lead Score", "Predicted Lead Class"]].head())
print(f"\nTotal companies scored: {len(df)}")