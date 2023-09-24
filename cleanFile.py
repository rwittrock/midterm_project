import pandas as pd

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("cinemaTicket_Ref.csv")

# Extract month from the "date" column and create a new column
data["month"] = data["date"].str.split("-").str[1]

# Keep only the specified variables
selected_variables = ["film_code", "tickets_sold", "occu_perc", "ticket_price"]

# Keep only the selected variables and the new 'month' column
cleaned_data = data[selected_variables + ["month"]]

# Specify the path for the new CSV file where you want to save the cleaned data
output_file_path = "cleaned_data.csv"

# Save the cleaned data to the new CSV file
cleaned_data.to_csv(output_file_path, index=False)

print(f"Cleaned data saved to {output_file_path}")
