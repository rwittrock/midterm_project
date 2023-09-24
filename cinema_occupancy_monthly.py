import pandas as pd

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("cleaned_data_no_outliers.csv")

# Group the data by month and calculate the average occu_perc for each month
monthly_avg_occu_perc = data.groupby("month")["occu_perc"].mean().reset_index()

# Round the 'occu_perc' column to 2 decimal places
monthly_avg_occu_perc["occu_perc"] = monthly_avg_occu_perc["occu_perc"].round(2)

# Specify the path for the new CSV file where you want to save the average occupancy percentage data
output_file_path = "monthly_avg_occu_perc.csv"

# Save the average occupancy percentage data to the new CSV file
monthly_avg_occu_perc.to_csv(output_file_path, index=False)

print(f"Monthly average occupancy percentage saved to {output_file_path}")
