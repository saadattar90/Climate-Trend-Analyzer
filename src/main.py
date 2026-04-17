import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("outputs"):
    os.makedirs("outputs")

data = {
    "Year": list(range(2000, 2021)),
    "Temperature": [14.1, 14.3, 14.5, 14.6, 14.8, 15.0, 15.1, 15.3, 15.5, 15.7,
                    15.8, 16.0, 16.2, 16.4, 16.5, 16.7, 16.9, 17.0, 17.2, 17.4, 17.6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Temperature"], marker='o')
plt.title("Global Temperature Trend")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid()

plt.savefig("outputs/temperature_trend.png")
plt.show()

print("Project Run Successful!")