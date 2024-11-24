import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack",
            "Kathy", "Leo", "Mona", "Nina", "Oscar"],
    "Age": [25, 30, 35, 40, 22, 28, 33, 27, 45, 50, 29, 38, 31, 26, 34],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Francisco", "Boston", "Miami", "Dallas", "Seattle",
            "Austin", "Denver", "Portland", "San Diego", "Orlando"],
    "Salary": [70000, 80000, 120000, 95000, 50000, 65000, 105000, 72000, 110000, 125000,
              68000, 90000, 85000, 95000, 102000],
    "Department": ["Engineering", "Marketing", "Sales", "HR", "Finance", "Engineering", "Marketing", "Sales", "HR", "Finance",
                  "Engineering", "HR", "Sales", "Marketing", "Engineering"],
    "Years of Experience": [3, 7, 12, 15, 2, 5, 9, 6, 18, 22, 4, 10, 8, 3, 14]
}
df = pd.DataFrame(data)

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df["Name"])
# print(df[["Name", "Age"]])
# print(df.iloc[0])
# print(df.loc[0])

# print(df[df["Age"] > 30])  # Rows where Age > 30

# df["Salary"] = [50000, 60000, 70000]  # Add a new column

# df = df.drop("Salary", axis=1)        # Remove a column
# df = df.drop(0, axis=0)               # Remove a row

# print(df.isnull().sum())  # Count of missing values in each column

# df["Age"] = df["Age"].fillna(df["Age"].mean())  # Replace with mean

# df = df.dropna()         # Drop rows with missing values

# df = df.sort_values("Age", ascending=False)  # Sort by column

# filtered = df[df["Age"] > 30]  # Rows where Age > 30

# df["Age"] = df["Age"].apply(lambda x: x * 2)  # Multiply each Age by 2

# grouped = df.groupby("Name")["Salary"].sum()  # Group by 'Name' and sum 'Salary'

# df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Alice", "Bob"]})
# df2 = pd.DataFrame({"ID": [1, 2], "Age": [25, 30]})
# merged = pd.merge(df1, df2, on="ID")  # Merge on 'ID'

# df1 = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
# df2 = pd.DataFrame({"Name": ["Alice", "Bob"], "Salary": [50000, 60000]})
# joined = df1.join(df2.set_index("Name"), on="Name")  # Join on 'Name'

# df.to_csv("output.csv", index=False)

# df = pd.read_csv("output.csv")

# df = pd.read_csv("file.txt", delimiter=" ")  # Adjust 'delimiter' as needed

# df.to_csv("output.csv", index=False)