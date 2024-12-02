import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('shopping_trends.csv')


# print(df.head())      
# print(df.info())      
# print(df.describe())  


high_purchases = df[df['Purchase Amount (USD)'] > 50]
print(high_purchases)
winter_clothing = df[(df['Season'] == 'Winter') & (df['Category'] == 'Clothing')]
print(winter_clothing)

age_location_df = df[['Age', 'Location']]
print(age_location_df)


purchase_amounts = df['Purchase Amount (USD)'].values

total_amount = np.sum(purchase_amounts)
average_amount = np.mean(purchase_amounts)

purchase_amounts = df['Purchase Amount (USD)'].values
print("Original Purchase Amounts:\n", purchase_amounts)


total_amount = np.sum(purchase_amounts)
average_amount = np.mean(purchase_amounts)
max_amount = np.max(purchase_amounts)
min_amount = np.min(purchase_amounts)
print("\nTotal Purchase Amount:", total_amount)
print("Average Purchase Amount:", average_amount)
print("Maximum Purchase Amount:", max_amount)
print("Minimum Purchase Amount:", min_amount)


sqrt_amounts = np.sqrt(purchase_amounts)
print("\nSquare Root of Purchase Amounts:\n", sqrt_amounts)

discounted_amounts = purchase_amounts * 0.9  
print("\nDiscounted Purchase Amounts (10% off):\n", discounted_amounts)

high_purchases = purchase_amounts[purchase_amounts > 50]
low_purchase_indices = np.where(purchase_amounts < 30)
print("\nHigh Purchases (greater than $50):\n", high_purchases)
print("\nIndices of Low Purchases (less than $30):\n", low_purchase_indices)


std_dev = np.std(purchase_amounts)
variance = np.var(purchase_amounts)
print("\nStandard Deviation of Purchase Amounts:", std_dev)
print("Variance of Purchase Amounts:", variance)


reshaped_array = purchase_amounts[:25].reshape(5, 5)
print("\nReshaped Array (5x5 matrix):\n", reshaped_array)

transposed_array = reshaped_array.T
print("\nTransposed Array:\n", transposed_array)


tax_rates = np.full_like(purchase_amounts, 0.1)  # 10% tax for all
total_with_tax = purchase_amounts + (purchase_amounts * tax_rates)
print("\nTotal Purchase Amounts with 10% Tax:\n", total_with_tax)


sorted_amounts = np.sort(purchase_amounts)
position = np.where(purchase_amounts == 90)
print("\nSorted Purchase Amounts:\n", sorted_amounts)
print("\nPosition of Purchase Amount 90:\n", position)


seasons_array = df['Season'].values
unique_seasons, season_counts = np.unique(seasons_array, return_counts=True)
print("\nUnique Seasons:\n", unique_seasons)
print("Season Counts:\n", season_counts)

adjusted_amounts = purchase_amounts + 5  # Add $5 to all purchases
print("\nPurchase Amounts after Adding $5:\n", adjusted_amounts)

