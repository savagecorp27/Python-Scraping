import pandas as pd
import matplotlib.pyplot as plt

sample = "books_scraped.csv"  
df = pd.read_csv(sample)

print("Shape:", df.shape)
print(df.describe())

# Average price by star rating
avg_price_by_rating = df.groupby("rating_stars")["price_gbp"].mean().round(2)
print("\nAverage price by rating:\n", avg_price_by_rating)

# % out of stock
pct_out_of_stock = (df["availability"] == "Out of stock").mean() * 100
print(f"\n% out of stock: {pct_out_of_stock:.1f}%")

# Price distribution plot
plt.figure(figsize=(8, 5))
df["price_gbp"].hist(bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
print("\nSaved price_distribution.png")

# Average price by rating - bar chart
plt.figure(figsize=(6, 4))
avg_price_by_rating.plot(kind="bar")
plt.title("Average Price by Star Rating")
plt.xlabel("Rating (stars)")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("price_by_rating.png")
print("Saved price_by_rating.png")
