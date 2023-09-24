import pandas as pd
import matplotlib.pyplot as plt

# Load the cinema data from the CSV file
data = pd.read_csv('cleaned_data_no_outliers.csv')

# Define the ticket price intervals
price_intervals = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000]  # Define your own intervals as needed

# Create a new column 'price_interval' by mapping ticket prices to intervals
data['price_interval'] = pd.cut(data['ticket_price'], bins=price_intervals)

# Group the data by 'price_interval' and calculate the total tickets sold in each interval
ticket_sales_by_interval = data.groupby('price_interval')['tickets_sold'].sum()

# Create a bar chart to visualize ticket sales by price interval
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
ticket_sales_by_interval.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Ticket Sales by Price Interval')
plt.xlabel('Price Interval')
plt.ylabel('Total Tickets Sold')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
