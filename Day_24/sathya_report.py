import json,csv

# d = pd.read_json('data.json')
# print(d)

# 1. Parse the JSON into a Python dictionary.
with open('data.json','r') as f:
    data = json.load(f)
    # print(data)


# 2. Compute the following for each category (across all stores):


# Flattening the nested dictionary structure
rows = []
category_totals = {}

for store in data['stores']:
    store_name = store.get('name', 'Unknown Store')
    for category in ['fruits', 'groceries', 'vegetables', 'dairy']:
        items = store.get(category, {})
        for item_name, item_data in items.items():
            initial_stock = item_data['initial_stock']
            closing_stock = item_data['stock']
            cost_price = item_data['cost_price']
            selling_price = item_data['selling_price']
            units_sold = initial_stock - closing_stock
            profit = units_sold * (selling_price - cost_price)
            warning = 'YES' if closing_stock < 10 else ''

            # Append row as a list
            rows.append([
                store_name,
                category,
                item_name,
                initial_stock,
                closing_stock,
                units_sold,
                profit,
                warning
            ])

            # Update category totals
            if category not in category_totals:
                category_totals[category] = {'Units Sold': 0, 'Profit': 0}
            category_totals[category]['Units Sold'] += units_sold
            category_totals[category]['Profit'] += profit

# Write to CSV
header = ["Store Name", "Category", "Item", "Initial Stock", "Closing Stock", "Units Sold", "Profit", "Warning"]
with open("report.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

# Display the nightly summary report in the terminal
print("Nightly Sales Summary")
print("-" * 40)
print(f"{'Category':<15} | {'Units Sold':>10} | {'Profit':>10}")
print("-" * 40)
total_profit = 0
for category in ['fruits', 'groceries', 'vegetables', 'dairy']:
    if category in category_totals:
        units = category_totals[category]['Units Sold']
        profit = category_totals[category]['Profit']
        total_profit += profit
        print(f"{category:<15} | {units:>10} | Rs.{profit:>9,.2f}")
print("-" * 40)
print(f"{'TOTAL PROFIT':<25} Rs.{total_profit:>9,.2f}")
print()
print("Low Stock Warnings")
print("-" * 40)
for row in rows:
    if row[7] == 'YES':
        print(f"{row[0]} - {row[2]} - Remaining: {row[4]}")
