import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Function to compute Poisson probability
def poisson_probability(k, lam):
    return (lam ** k) * math.exp(-lam) / math.gamma(k + 1)

# Read in the data
df = pd.read_csv(r'C:\Users\IoannisZografakis-Re\Downloads\vgsales.csv')
# Drop rows with missing values
df.dropna(inplace=True)

# Group data by game name and sum global sales
game_sales = df.groupby('Name')['Global_Sales'].sum()
# Sort by global sales
game_sales = game_sales.sort_values(ascending=False)
# Display top 10 games
print(game_sales.head(10))

# Group data by platform and sum global sales
platform_sales = df.groupby('Platform')['Global_Sales'].sum()
# Sort by global sales
platform_sales = platform_sales.sort_values(ascending=False)
# Display platform sales
print(platform_sales)

# Group data by genre and sum global sales
genre_sales = df.groupby('Genre')['Global_Sales'].sum()
# Sort by global sales
genre_sales = genre_sales.sort_values(ascending=False)
# Display genre sales
print(genre_sales)

# Create a bar chart showing sales by region with custom colors
region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
region_sales.plot(kind='bar', color=['#FF5733', '#33FF57', '#3357FF', '#F4C300'])  # Custom colors
plt.title('Video Game Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales (millions)')
plt.show()

# Create a scatter plot showing the relationship between year of release and global sales with a custom color
plt.scatter(df['Year'], df['Global_Sales'], color='#FF5733')  # Custom color for scatter points
plt.title('Year of Release vs Global Sales')
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.show()

# Group data by publisher and sum global sales
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()
# Sort by global sales
publisher_sales = publisher_sales.sort_values(ascending=False)

# Create a bar chart showing top publishers by global sales with custom colors
top_publishers = publisher_sales.head(10)
colors = plt.cm.viridis(np.linspace(0, 1, len(top_publishers)))  # Generate a range of colors
top_publishers.plot(kind='bar', color=colors)
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()

# Calculate mean and variance of global sales data
mean_sales = df['Global_Sales'].mean()
var_sales = df['Global_Sales'].var()

# Calculate expected mean and variance of Poisson distribution
exp_mean = var_sales
exp_var = var_sales

# Compare mean and variance to expected values for Poisson distribution
print('Mean of global sales data:', mean_sales)
print('Variance of global sales data:', var_sales)
print('Expected mean of Poisson distribution:', exp_mean)
print('Expected variance of Poisson distribution:', exp_var)

# Generate a histogram of the global sales data
n, bins, patches = plt.hist(df['Global_Sales'], bins=50, density=True, alpha=0.5, color='#33A0FF')  # Custom color for histogram
# Calculate the Poisson distribution for the mean
poisson_dist = [poisson_probability(b, mean_sales) for b in bins]
# Plot the Poisson distribution over the histogram
plt.plot(bins, poisson_dist, 'r-', linewidth=2)  # Red line for the Poisson distribution
# Label the plot
plt.title('Global Sales Data and Poisson Distribution')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Probability')
plt.show()
