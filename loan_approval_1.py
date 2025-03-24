import pandas as pd

# Loan scoring function
def calculate_loan_score(credit_score, annual_income, debt_to_income_ratio, employment_status, loan_amount):
    credit_score_normalized = (credit_score - 300) / 550 * 100
    max_income = 500000
    annual_income_normalized = min(annual_income / max_income * 100, 100)
    debt_to_income_score = (1 - debt_to_income_ratio) * 100
    employment_status_score = {"Employed": 100, "Self-Employed": 80, "Unemployed": 0}.get(employment_status, 0)
    loan_to_income_ratio = loan_amount / annual_income
    loan_to_income_score = 100 if loan_to_income_ratio <= 2 else 80 if loan_to_income_ratio <= 3 else 50

    loan_score = (
        credit_score_normalized * 0.4 +
        annual_income_normalized * 0.25 +
        debt_to_income_score * 0.2 +
        employment_status_score * 0.1 +
        loan_to_income_score * 0.05
    )
    return round(loan_score, 2)

# Generate test scenarios
test_scenarios = [
    {"Credit Score": 300, "Annual Income": 20000, "Debt-to-Income Ratio": 0.5, "Employment Status": "Unemployed", "Loan Amount": 50000},
    {"Credit Score": 850, "Annual Income": 500000, "Debt-to-Income Ratio": 0.1, "Employment Status": "Employed", "Loan Amount": 100000},
    {"Credit Score": 650, "Annual Income": 60000, "Debt-to-Income Ratio": 0.3, "Employment Status": "Self-Employed", "Loan Amount": 150000},
    {"Credit Score": 720, "Annual Income": 100000, "Debt-to-Income Ratio": 0.4, "Employment Status": "Employed", "Loan Amount": 300000},
    {"Credit Score": 850, "Annual Income": 500000, "Debt-to-Income Ratio": 0.5, "Employment Status": "Self-Employed", "Loan Amount": 1000000},
]

# Evaluate test scenarios
results = []
for scenario in test_scenarios:
    score = calculate_loan_score(
        scenario["Credit Score"],
        scenario["Annual Income"],
        scenario["Debt-to-Income Ratio"],
        scenario["Employment Status"],
        scenario["Loan Amount"]
    )
    decision = "Loan Approved" if score >= 80 else "Loan Approved with Conditions" if score >= 60 else "Loan Rejected"
    scenario["Loan Score"] = score
    scenario["Decision"] = decision
    results.append(scenario)

# Convert results to DataFrame and display
df = pd.DataFrame(results)
print(df)