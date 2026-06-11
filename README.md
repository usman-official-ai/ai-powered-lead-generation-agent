# AI-Powered Lead Generation & Lead Scoring Agent (Phase 2)

## 1. Project Overview
This phase transforms collected business leads into a structured machine-learning dataset and prepares it for model training.

## 2. Dataset Cleaning Process
- Removed duplicate company records: 0 duplicates
- Removed missing websites: 0 missing
- Standardized country names (USA → United States, UAE → United Arab Emirates)
- **Final cleaned dataset:** `data/cleaned_leads.csv` (50 records)

## 3. Feature Engineering Approach
| Feature | Description |
|---------|-------------|
| website_exists | 1 = Yes, 0 = No |
| contact_form | 1 = Yes, 0 = No |
| services_count | Number of words in services |
| about_word_count | Character length of services |
| country_score | USA=3, Canada=2, UAE=1 |
| lead_quality_score | High=3, Medium=2, Low=1 |

## 4. Exploratory Data Analysis Summary
- **Total companies:** 50
- **Average services per company:** ~4.2
- **Companies with contact forms:** 82%
- **Charts available in:** `notebooks/lead_eda.ipynb`

## 5. Lead Scoring Logic
| Condition | Score |
|-----------|-------|
| Website Available | +10 |
| Contact Form Available | +20 |
| United States | +15 |
| Canada | +10 |
| United Arab Emirates | +5 |
| Services Count > 3 | +15 |
| About Section > 100 words | +10 |

**Classification:** ≥60 High, 35–59 Medium, <35 Low

## 6. ML Dataset Preparation
- **Features:** website_exists, contact_form, services_count, about_word_count, country_score
- **Target:** lead_quality_score
- **Train-test split:** 80:20
- **Training samples:** 40
- **Testing samples:** 10
- **Notebook:** `notebooks/ml_preparation.ipynb`

## 7. Future Model Training Plan
- Classification algorithms (Logistic Regression, Random Forest)
- Predict lead quality (High/Medium/Low)
- Evaluate using accuracy, precision, recall

## 8. Team Member Name
Muhammad Usman

## 9. Key Learnings
- Data cleaning and standardization
- Feature engineering from raw business data
- EDA with visualizations using matplotlib
- Rule-based lead scoring system
- Train-test split preparation for ML models

## Files Generated in Phase 2
- `data/cleaned_leads.csv`
- `data/ml_ready_dataset.csv`
- `data/scored_leads.csv`
- `notebooks/lead_eda.ipynb`
- `notebooks/ml_preparation.ipynb`
- `src/task1_clean.py`
- `src/task2_features.py`
- `src/task4_scoring.py`