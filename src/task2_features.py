import pandas as pd

df = pd.read_csv("data/cleaned_leads.csv")

# website_exists: 1 for all
df["website_exists"] = 1

# contact_form: Yes -> 1, No -> 0
df["contact_form"] = df["Contact Form"].apply(lambda x: 1 if str(x).lower() == "yes" else 0)

# services_count: number of words in Company Services
df["services_count"] = df["Company Services"].apply(lambda x: len(str(x).split()) if pd.notna(x) else 1)

# about_word_count: length of Company Services as proxy
df["about_word_count"] = df["Company Services"].apply(lambda x: len(str(x)) if pd.notna(x) else 50)

# country_score: USA=3, Canada=2, UAE=1
country_score_map = {"United States": 3, "Canada": 2, "United Arab Emirates": 1}
df["country_score"] = df["Country"].map(country_score_map).fillna(1)

# lead_quality_score: High=3, Medium=2, Low=1
quality_score_map = {"High": 3, "Medium": 2, "Low": 1}
df["lead_quality_score"] = df["Lead Quality"].map(quality_score_map).fillna(2)

# Save
df.to_csv("data/ml_ready_dataset.csv", index=False)

print("✅ ml_ready_dataset.csv saved in data/ folder")
print(f"New features added. Total columns: {len(df.columns)}")
print(df[["website_exists", "contact_form", "services_count", "about_word_count", "country_score", "lead_quality_score"]].head())