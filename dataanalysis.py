import pandas as pd

# Replace 'input_file.csv' with the path to your CSV file.
input_file_path = "cleaned_data_no_outliers.csv"

try:
    # Read the CSV file into a DataFrame.
    df = pd.read_csv(input_file_path)

    # Select the columns of interest.
    columns_of_interest = [
        "film_code",
        "tickets_sold",
        "occu_perc",
        "ticket_price",
        "month",
    ]

    # Calculate the statistics for each selected column.
    statistics = {"Statistic": ["Mean", "Median", "Mode", "Variance", "Std Deviation"]}

    for column in columns_of_interest:
        statistics[column] = [
            round(df[column].mean(), 2),
            round(df[column].median(), 2),
            df[column]
            .mode()
            .values[0],  # Mode can have multiple values, we choose the first one.
            round(df[column].var(), 2),
            round(df[column].std(), 2),
        ]

    # Set the display format for the 'ticket_price' column to avoid scientific notation and format to two decimal places.
    pd.options.display.float_format = "{:.2f}".format

    # Create a DataFrame to display the statistics.
    stats_df = pd.DataFrame(statistics)

    # Print the statistics with custom row names.
    print("Statistics for selected columns:")
    print(stats_df)

except FileNotFoundError:
    print(f"File not found: {input_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Reset the display format to its default setting (if needed).
pd.options.display.float_format = None
