import pandas as pd
import numpy as np

def generate_patient_adherence_data(n_patients=10000):
    """
    Generates a synthetic pharmaceutical dataset to simulate patient adherence.
    Variables are weighted to reflect real-world commercial hurdles like 
    out-of-pocket costs and clinical complexity.
    """
    np.random.seed(42)
    
    data = {
        'patient_id': range(1, n_patients + 1),
        'age': np.random.randint(18, 85, n_patients),
        'out_of_pocket_cost': np.random.uniform(10, 600, n_patients),  # Higher cost = higher risk
        'comorbidity_score': np.random.randint(0, 8, n_patients),     # Clinical complexity
        'last_interaction_days': np.random.randint(0, 120, n_patients), # Days since last refill/call
        'total_prior_refills': np.random.randint(1, 12, n_patients),
        'digital_engagement_score': np.random.uniform(0, 1, n_patients) # App/Portal usage
    }
    
    df = pd.DataFrame(data)
    
    # Mathematical logic for the 'discontinued' target:
    # We weight out-of-pocket costs and low engagement as high-risk factors.
    risk_factor = (
        0.3 * (df['out_of_pocket_cost'] / 600) + 
        0.2 * (df['comorbidity_score'] / 8) +
        0.3 * (1 - df['digital_engagement_score']) +
        0.2 * (df['last_interaction_days'] / 120)
    )
    
    # Set a threshold for discontinuation with a bit of random noise
    df['discontinued'] = (risk_factor + np.random.normal(0, 0.05, n_patients) > 0.55).astype(int)
    
    return df

if __name__ == "__main__":
    print("Generating synthetic patient dataset...")
    df = generate_patient_adherence_data()
    df.to_csv('synthetic_patient_data.csv', index=False)
    print(f"Success! Created 'synthetic_patient_data.csv' with {len(df)} records.")
    print("Columns: ", list(df.columns))
