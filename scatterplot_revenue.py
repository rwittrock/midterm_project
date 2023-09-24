import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("movie_sales_data.csv")

# Assuming "total_sales" represents the total money made by each movie, create a scatter plot
sorted_data = data.sort_values(by="total_sales")
plt.figure(figsize=(10, 6))
plt.scatter(range(len(sorted_data)), sorted_data["total_sales"])
plt.ylabel("Total Sales")
plt.title("Revenue of Each Movie (Ascending Order)")
plt.grid(True)

# Remove x-axis labels and ticks
plt.xticks([])

# Save the scatter plot as an image
plt.savefig("movie_revenue_scatter_ascending_no_x_axis.png")

# Display the scatter plot (optional)
plt.show()
