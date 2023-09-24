import pandas as pd

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("cleaned_data_no_outliers.csv")

# Calculate total sales for each movie based on film_code
data["total_sales"] = data["tickets_sold"] * data["ticket_price"]

# Group the data by film_code and sum the total sales for each movie
movie_sales_data = data.groupby("film_code")["total_sales"].sum().reset_index()

# Specify the path for the new CSV file where you want to save the movie sales data
output_file_path = "movie_sales_data.csv"

# Save the movie sales data to the new CSV file
movie_sales_data.to_csv(output_file_path, index=False)

print(f"Movie sales data saved to {output_file_path}")

import pandas as pd

# Load the movie sales data from the CSV file
movie_sales_data = pd.read_csv("movie_sales_data.csv")

# Calculate the statistics
mean_sales = round(movie_sales_data["total_sales"].mean(), 2)
median_sales = round(movie_sales_data["total_sales"].median(), 2)
std_dev_sales = round(movie_sales_data["total_sales"].std(), 2)

# Create a DataFrame to display the statistics
statistics_df = pd.DataFrame(
    {
        "Statistic": ["Mean", "Median", "Standard Deviation"],
        "Value": [mean_sales, median_sales, std_dev_sales],
    }
)

# Set the display options to avoid scientific notation
pd.set_option("display.float_format", "{:.2f}".format)

# Print the statistics table
print(statistics_df)
