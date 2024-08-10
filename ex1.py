import pandas as pd

# 1. Read the CSV file into a DataFrame
df = pd.read_csv('C:\weboin company\Python_task\All Bills.csv')

# 2. Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df)

# 3. Filter students who have a grade of 'A'
# df_subset = df.iloc[:10, :90]
weboin_invoice = df.iloc[:13, :35]

print("\nweboin_invoice:")
print(weboin_invoice)

# 5. Save the filtered DataFrame to a new CSV file
weboin_invoice.to_csv('weboin_invoice.csv', index=False)
print("\nFiltered DataFrame saved to 'weboin_invoice.csv'.")

