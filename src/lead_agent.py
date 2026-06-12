import joblib
import pandas as pd
import os

class LeadRecommendationAgent:
    def __init__(self, model_path="best_lead_model.pkl"):
        """Load the trained model"""
        # Get the absolute path to the model file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, model_path)
        self.model = joblib.load(full_path)
        print("✅ Lead Recommendation Agent initialized")
    
    def predict_lead(self, website_exists, contact_form, services_count, about_word_count, country_score):
        """
        Predict lead quality based on input features
        Returns: Prediction (High/Medium/Low) and Recommendation message
        """
        features = pd.DataFrame([[
            website_exists, contact_form, services_count, about_word_count, country_score
        ]], columns=['website_exists', 'contact_form', 'services_count', 'about_word_count', 'country_score'])
        
        prediction = self.model.predict(features)[0]
        
        if prediction == "High":
            message = "🔴 Priority Lead - Contact within 24 hours"
        elif prediction == "Medium":
            message = "🟡 Potential Opportunity - Add to nurture campaign"
        else:
            message = "🟢 Low Priority - Monitor for future engagement"
        
        return prediction, message

if __name__ == "__main__":
    agent = LeadRecommendationAgent()
    pred, msg = agent.predict_lead(1, 1, 5, 120, 3)
    print(f"\nPrediction: {pred}")
    print(f"Recommendation: {msg}")