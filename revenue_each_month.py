import pandas as pd

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("cleaned_data_no_outliers.csv")

# Calculate the total money made for each month
data["total_money_made"] = data["tickets_sold"] * data["ticket_price"]

# Calculate the number of measurements each month
monthly_measurement_count = data.groupby("month")["film_code"].count().reset_index()
monthly_measurement_count.rename(
    columns={"film_code": "measurement_count"}, inplace=True
)

# Group data by month and calculate sum of tickets_sold, occu_perc, and total_money_made
monthly_data = (
    data.groupby("month")
    .agg({"tickets_sold": "sum", "occu_perc": "sum", "total_money_made": "sum"})
    .reset_index()
)

# Merge the monthly total money made, measurement count, and other variables
monthly_data = pd.merge(monthly_data, monthly_measurement_count, on="month")

# Specify the path for the new CSV file where you want to save the monthly data
output_file_path = "monthly_data_with_measurement_count.csv"

# Save the monthly data to the new CSV file
monthly_data.to_csv(output_file_path, index=False)

print(f"Monthly data with measurement count saved to {output_file_path}")
