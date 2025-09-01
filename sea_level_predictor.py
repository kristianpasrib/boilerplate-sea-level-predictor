import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.6)

    # Create first line of best fit (1880–2050)
    slope1, intercept1, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept1 + slope1 * years_extended, 'r', label="Best Fit (1880–2050)")

    # Create second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = pd.Series(range(2000, 2051))
    plt.plot(years_recent_extended, intercept2 + slope2 * years_recent_extended, 'g', label="Best Fit (2000–2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
