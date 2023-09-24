import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('monthly_data_with_measurement_count.csv')  # Replace with your actual file path

# Convert the 'tickets_sold' column to a NumPy array
tickets_sold = data['tickets_sold'].to_numpy()

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(range(2, 12), tickets_sold, marker='o', linestyle='-')  # Assuming months range from 2 to 11
plt.title('Tickets Sold Over Months')
plt.xlabel('Month')
plt.ylabel('Tickets Sold')

# Manually set x-axis ticks and labels
plt.xticks(range(2, 12), ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'])

# Show the plot
plt.grid(True)  # Add a grid to the plot (optional)
plt.tight_layout()  # Ensure labels are not cut off
plt.show()
