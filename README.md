# AI-Powered Lead Generation & Lead Scoring Agent

## Project Overview
This project builds an intelligent system that discovers business leads from public sources, collects company information, analyzes websites, prepares ML-ready datasets, trains machine learning models, and develops a recommendation agent for sales prioritization.

---

## Phase 1: Lead Collection & Website Analysis

### Objective
Collect 50 business leads from USA-based companies and analyze their websites for services and contact information.

### Data Collection
- **Sources**: Google Maps, Clutch.co, business directories
- **Countries**: USA
- **Industries**: AI Development, SaaS, Web Development, Mobile App Development

### Dataset Structure (50 leads)
| Column | Description |
|--------|-------------|
| Company Name | Name of the business |
| Website | Company URL |
| Country | United States |
| Industry | AI/SaaS/Web/Mobile App Development |
| Contact Page | Yes/No |
| Company Services | Services offered by the company |
| Contact Form | Yes/No |
| Lead Quality | High/Medium/Low (rule-based) |

### Deliverables
- `business_leads_50_complete.xlsx` - Raw collected data
- `lead_analysis.ipynb` - Initial data analysis
- Flowchart in `docs/` folder

---

## Phase 2: Data Cleaning, Feature Engineering & ML Preparation

### Dataset Cleaning
- Removed duplicate records: 0 duplicates
- Removed missing websites: 0 missing
- Standardized country names (USA → United States, UAE → United Arab Emirates)
- **Final cleaned dataset**: `cleaned_leads.csv` (50 records)

### Feature Engineering
| Feature | Description |
|---------|-------------|
| website_exists | 1 = Yes, 0 = No |
| contact_form | 1 = Yes, 0 = No |
| services_count | Number of words in services |
| about_word_count | Character length of services |
| country_score | USA=3, Canada=2, UAE=1 |
| lead_quality_score | High=3, Medium=2, Low=1 |

### Exploratory Data Analysis (EDA)
- **Total companies**: 50
- **Average services per company**: 4.2
- **Companies with contact forms**: 82%
- Charts available in `lead_eda.ipynb`

### Lead Scoring Engine (Rule-Based)
| Condition | Score |
|-----------|-------|
| Website Available | +10 |
| Contact Form Available | +20 |
| United States | +15 |
| Canada | +10 |
| United Arab Emirates | +5 |
| Services Count > 3 | +15 |
| About Section > 100 words | +10 |

**Classification**: ≥60 High, 35-59 Medium, <35 Low

### ML Dataset Preparation
- **Features**: website_exists, contact_form, services_count, about_word_count, country_score
- **Target**: lead_quality_score
- **Train-test split**: 80:20 (40 training, 10 testing)

### Deliverables
- `cleaned_leads.csv` - Cleaned dataset
- `ml_ready_dataset.csv` - Feature engineered dataset
- `scored_leads.csv` - Rule-based scoring results
- `lead_eda.ipynb` - EDA with visualizations
- `ml_preparation.ipynb` - Train-test split

---

## Phase 3: ML Model Training & Recommendation Agent

### Model Training
**Algorithms Evaluated**:
- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression

**Features Used**:
- website_exists
- contact_form
- services_count
- about_word_count
- country_score

**Target Variable**: Predicted Lead Class (High/Medium/Low)

**Results**:
| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Decision Tree | 100% | 100% | 100% | 100% |
| Random Forest | 100% | 100% | 100% | 100% |
| Logistic Regression | 100% | 100% | 100% | 100% |

**Note**: 100% accuracy is due to small dataset (50 records). Overfitting is expected. For production, 500+ leads recommended.

### Lead Recommendation Agent

**Agent Name**: `LeadRecommendationAgent`

**Functionality**:
- Loads trained model from `best_lead_model.pkl`
- Accepts lead features as input
- Predicts lead quality (High/Medium/Low)
- Returns actionable recommendation

**Recommendation Messages**:
| Prediction | Recommendation |
|------------|----------------|
| 🔴 High | Priority Lead - Contact within 24 hours |
| 🟡 Medium | Potential Opportunity - Add to nurture campaign |
| 🟢 Low | Low Priority - Monitor for future engagement |

### Model Artifacts
- `best_lead_model.pkl` - Serialized model using joblib

### Agent Testing Results
Tested on 10 sample leads:
| Prediction | Count |
|------------|-------|
| High | 7 |
| Medium | 2 |
| Low | 1 |

### Deliverables
- `model_training.ipynb` - Model training and evaluation
- `lead_agent.py` - Recommendation agent class
- `best_lead_model.pkl` - Saved model
- `agent_testing.ipynb` - Agent testing notebook

---

## Future Improvements
- XGBoost implementation for better performance
- Hyperparameter tuning with GridSearchCV
- Streamlit dashboard for interactive lead scoring
- FastAPI for real-time API deployment
- Collect more data (500+ leads) to reduce overfitting
- Cross-validation for robust evaluation

---

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python | Core programming |
| Pandas | Data manipulation |
| Scikit-learn | ML models (Random Forest, Decision Tree, Logistic Regression) |
| Matplotlib | Visualizations |
| Jupyter Notebook | EDA and model training |
| Joblib | Model serialization |
| Git & GitHub | Version control |

---

## Team Member
Muhammad Usman

---

## Key Learnings
- Lead collection from public business directories
- Website analysis for services and contact information
- Data cleaning and standardization techniques
- Feature engineering for ML-friendly datasets
- Exploratory data analysis with visualizations
- Rule-based lead scoring system
- Training multiple ML classification models
- Handling overfitting in small datasets
- Building a recommendation agent for sales teams
- Model persistence using joblib
- Professional GitHub documentation

---

## Repository Structure

AI-Powered-Lead-Generation-Agent/
├── data/
│ ├── business_leads_50_complete.xlsx
│ ├── cleaned_leads.csv
│ ├── ml_ready_dataset.csv
│ └── scored_leads.csv
├── notebooks/
│ ├── lead_analysis.ipynb
│ ├── lead_eda.ipynb
│ ├── ml_preparation.ipynb
│ ├── model_training.ipynb
│ └── agent_testing.ipynb
├── src/
│ ├── task1_clean.py
│ ├── task2_features.py
│ ├── task4_scoring.py
│ └── lead_agent.py
├── docs/
│ └── Agent Workflow.drawio.png
├── best_lead_model.pkl
├── README.md
└── requirements.txt

text

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
2. Run Lead Agent
bash
python src/lead_agent.py
3. Explore Notebooks
Open Jupyter notebooks in notebooks/ folder using:

bash
jupyter notebook
Status
Phase	Status
Phase 1: Lead Collection	✅ Complete
Phase 2: Data Preparation	✅ Complete
Phase 3: ML & Agent	✅ Complete
