import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate synthetic data (monthly spending and yearly spending)
np.random.seed(0)  # For reproducibility
monthly_spending = np.random.uniform(200, 5000, 50)  # Random monthly spending between $200 and $5000
yearly_spending = 12 * monthly_spending + np.random.randn(50) * 1000  # Yearly spending = 12 * monthly + some noise (ϵ)

# Step 2: Manually calculate β₀ (intercept) and β₁ (slope) using the Normal Equation
X = monthly_spending  # This is our feature variable (monthly spending)
y = yearly_spending   # This is our target variable (yearly spending)

# We want to solve for y = β₀ + β₁x using the formula for β₁ and β₀
# β₁ = Σ((xᵢ - x̄) * (yᵢ - ȳ)) / Σ((xᵢ - x̄)²)
# β₀ = ȳ - β₁ * x̄

# Calculate the mean of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate β₁ (slope)
beta_1 = np.sum((X - mean_X) * (y - mean_y)) / np.sum((X - mean_X) ** 2)

# Calculate β₀ (intercept)
beta_0 = mean_y - beta_1 * mean_X

# Step 3: Create the regression line (y = β₀ + β₁x)
X_line = np.linspace(min(X), max(X), 100)  # Create a range of values for X
y_line = beta_0 + beta_1 * X_line  # Calculate corresponding y values

# Step 4: Plot the data and the regression line using Matplotlib and Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X, y=y, color='blue', label='Actual Data')  # Scatter plot of actual data
plt.plot(X_line, y_line, color='red', label=f'Regression Line: y = {beta_0:.2f} + {beta_1:.2f}x')  # Regression line
plt.xlabel('Monthly Spending (USD)')
plt.ylabel('Yearly Spending (USD)')
plt.title('Prediction of Yearly Spending based on Monthly Spending')
plt.legend()
plt.grid(True)
plt.show()

# Step 5: Make a prediction for a given monthly spending (e.g., $1500)
monthly_spending_example = 1500
predicted_yearly_spending = beta_0 + beta_1 * monthly_spending_example
print(f"Predicted yearly spending for ${monthly_spending_example} monthly: ${predicted_yearly_spending:.2f}")
