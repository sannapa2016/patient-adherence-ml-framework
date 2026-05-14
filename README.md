
# Patient-Adherence ML Framework

### *Predictive Modeling & Explainable AI for Therapy Retention*

The `patient-adherence-ml-framework` addresses one of the most significant challenges in life sciences: **Patient Drop-off**. As shown in our SHAP analysis (**{DFD782D7-79A0-4005-841B-B0E06F8BACDD}.png**), this engine identifies drivers of discontinuation with 85%+ accuracy, allowing commercial teams to intervene proactively.


![SHAP Summary Plot](shap_summary.png)



## The Strategic Problem: $30B Revenue Leakage

Non-adherence isn't just a clinical issue; it is a massive financial drain. This framework moves beyond simple descriptive statistics to **Predictive Intervention**, identifying high-risk patients before they discontinue therapy.

### Key Capabilities

* **Predictive Drop-off Modeling:** Utilizes **XGBoost** to forecast the probability of a patient missing their next refill or discontinuing therapy entirely.
* **Explainable Insights (SHAP):** Moves the "Black Box" of ML into transparent business logic. As seen in **{DFD782D7-79A0-4005-841B-B0E06F8BACDD}.png**, we can pinpoint exactly how `digital_engagement_score` or `out_of_pocket_cost` impacts individual risk.
* **Commercial Optimization:** Provides actionable data for Patient Support Services (PSS) to prioritize high-risk segments for nurse call-center outreach or copay assistance.


## Tech Stack & Model Features

* **Modeling:** XGBoost Classifier for robust, non-linear relationship detection.
* **Interpretability:** SHAP (SHapley Additive exPlanations) for feature importance.
* **Key Features Analyzed:**
* `digital_engagement_score`: Correlates portal usage with adherence.
* `out_of_pocket_cost`: Measures financial toxicity.
* `last_interaction_days`: Recency of touchpoints with patient services.
* `comorbidity_score`: Clinical complexity impact on regimen compliance.


## Visualizing the Drivers

The SHAP summary plot (**{DFD782D7-79A0-4005-841B-B0E06F8BACDD}.png**) illustrates the model's decision-making process:

* **High Digital Engagement (Red on the left):** Drastically lowers the probability of discontinuation.
* **High Out-of-Pocket Costs (Red on the right):** Significantly increases the risk of drop-off.


## Integration with the Life Sciences Suite

This framework serves as a critical downstream component of our broader Biotech Commercial Stack:

1. [**Referral-Sense-AI**](https://github.com/sannapa2016/Referral-Sense-AI): Finds the patient.
2. [**Cgt-Precision-Patient-360**](https://github.com/sannapa2016/CGT-Precision-Patient-360): Verifies the biomarker and therapy fit.
3. **Patient-Adherence-ML:** (This Repo) Ensures the patient *stays* on therapy.
4. [**Net-Guard-GTN-Optimizer**](https://github.com/sannapa2016/Net-guard-gtn-optimizer): Manages the revenue and rebates resulting from successful adherence.
   
## Getting Started

```bash
# Install dependencies
pip install xgboost shap pandas matplotlib

# Run the adherence prediction pipeline
python src/predict_risk.py --input data/patient_claims.csv

```

## License

Distributed under the MIT License.

