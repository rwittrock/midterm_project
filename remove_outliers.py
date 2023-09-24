import pandas as pd
import numpy as np

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("cleaned_data.csv")

# Define a multiplier to control the outlier threshold (e.g., 1.5 is common)
outlier_multiplier = 1.5

# Create a mask to identify rows with outliers
outlier_mask = np.zeros(len(data), dtype=bool)

# Iterate through each numeric column
for column in data.select_dtypes(include=[np.number]).columns:
    # Calculate the IQR for the column
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - outlier_multiplier * IQR
    upper_bound = Q3 + outlier_multiplier * IQR

    # Update the outlier mask for this column
    outlier_mask |= (data[column] < lower_bound) | (data[column] > upper_bound)

# Filter rows without outliers
cleaned_data = data[~outlier_mask]

columns_with_missing_values = [
    "film_code",
    "tickets_sold",
    "occu_perc",
    "ticket_price",
    "month",
]
data.dropna(subset=columns_with_missing_values, inplace=True)

# Step 2: Removing Duplicates
# Remove duplicate rows based on all columns.
data.drop_duplicates(inplace=True)

# Step 3: Data Type Conversion (if needed)
# Convert columns to appropriate data types (e.g., 'tickets_sold' to int).
data["tickets_sold"] = data["tickets_sold"].astype(int)


# Specify the path for the new CSV file where you want to save the cleaned data
output_file_path = "cleaned_data_no_outliers.csv"

# Save the cleaned data to the new CSV file
cleaned_data.to_csv(output_file_path, index=False)

print(f"Cleaned data (without outliers) saved to {output_file_path}")
