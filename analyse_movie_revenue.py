import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from a CSV file (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv("movie_sales_data.csv")

# Assuming "total_sales" represents the total money made by each movie, calculate the total sales for each film
film_total_sales = data.groupby("film_code")["total_sales"].sum().reset_index()

# Sort the movies by total sales in ascending order to get the top 10 best and worst
top_10_best = film_total_sales.sort_values(by="total_sales", ascending=False).head(10)
top_10_worst = film_total_sales.sort_values(by="total_sales").head(10)

# Create evenly spaced numerical values as placeholders for x-axis ticks
x_ticks_best = np.arange(10)
x_ticks_worst = np.arange(10)

# Create a subplot for the top 10 best movies
fig, ax1 = plt.subplots(figsize=(8, 6))

# Set the x-axis ticks to evenly spaced numerical values
ax1.set_xticks(x_ticks_best)

# Label the x-axis ticks with the film codes of the top 10 best movies
ax1.set_xticklabels(top_10_best["film_code"])

# Plot the top 10 best movies
ax1.bar(x_ticks_best, top_10_best["total_sales"])
ax1.set_xlabel("Film Code")
ax1.set_ylabel("Total Sales")
ax1.set_title("Top 10 Best Movies by Total Sales")

# Save the chart for the top 10 best movies as an image
plt.savefig("top_10_best_movies.png")

# Close the chart
plt.close()

# Create a subplot for the top 10 worst movies
fig, ax2 = plt.subplots(figsize=(8, 6))

# Set the x-axis ticks to evenly spaced numerical values
ax2.set_xticks(x_ticks_worst)

# Label the x-axis ticks with the film codes of the top 10 worst movies
ax2.set_xticklabels(top_10_worst["film_code"])

# Plot the top 10 worst movies
ax2.bar(x_ticks_worst, top_10_worst["total_sales"])
ax2.set_xlabel("Film Code")
ax2.set_ylabel("Total Sales")
ax2.set_title("Top 10 Worst Movies by Total Sales")

# Save the chart for the top 10 worst movies as an image
plt.savefig("top_10_worst_movies.png")

# Close the chart
plt.close()
