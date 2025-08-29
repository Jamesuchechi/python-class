import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# 1. Create the dataset
n_employees = 500
data = {
    'Name': [f'Employee_{i+1}' for i in range(n_employees)],
    'Age': np.random.randint(22, 65, n_employees),
    'Salary': np.random.randint(30000, 120000, n_employees),
    'Position': np.random.choice(['Analyst', 'Manager', 'Developer', 'Engineer', 'Consultant'], n_employees),
    'Sex': np.random.choice(['M', 'F'], n_employees)
}

# Create DataFrame
df = pd.DataFrame(data)
print(df.to_string())



# Save to CSV (optional)
#df.to_csv('employees_data.csv', index=False)

# Display first few rows
"""print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# 2. Calculate the average salary
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: ${average_salary:.2f}")"""

# 3. Visualize the salary distribution using four different plots
#plt.style.use('seaborn')  # For better aesthetics

# Create a figure with 2x2 subplots
"""fig, axes = plt.subplots(2, 2, figsize=(15, 10))
#fig.suptitle('Salary Distribution Analysis', fontsize=16)

# Histogram
axes[0, 0].hist(df['Salary'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram of Salaries')
axes[0, 0].set_xlabel('Salary ($)')
axes[0, 0].set_ylabel('Frequency')

# Scatter Plot (Salary vs Age)
axes[0, 1].scatter(df['Age'], df['Salary'], alpha=0.5, color='green')
axes[0, 1].set_title('Salary vs Age')
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Salary ($)')

# Box Plot
sns.boxplot(y=df['Salary'], ax=axes[1, 0], color='lightcoral')
axes[1, 0].set_title('Box Plot of Salaries')
axes[1, 0].set_ylabel('Salary ($)')

# Violin Plot
sns.violinplot(y=df['Sex'], ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_title('Violin Plot of Sexes')
axes[1, 1].set_ylabel('Sex ($)')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show plots
plt.show()"""