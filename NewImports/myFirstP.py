import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\zavol\Documents\pythonPrograms\NewImports\FuelConsumption.csv'
df = pd.read_csv(file_path)

# Print the column names
print("Column names:", df.columns)

# Plotting
plt.scatter(df['ENGINESIZE'], df['CO2EMISSIONS'])  # Use 'ENGINESIZE' and 'CO2EMISSIONS'
plt.title('Engine Size vs. CO2 Emissions')
plt.xlabel('Engine Size')
plt.ylabel('CO2 Emissions')
plt.grid(True)
plt.show()


