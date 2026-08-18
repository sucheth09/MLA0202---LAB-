import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Year":[2018,2019,2017,2020,2016,2021,2019,2018,2022,2017],
    "Mileage":[30000,25000,45000,20000,60000,15000,28000,35000,10000,50000],
    "Engine":[1200,1500,1200,1800,1000,1800,1500,1300,2000,1200],
    "Price":[600000,700000,500000,900000,400000,1000000,720000,620000,1200000,480000]
})

X = data[["Year","Mileage","Engine"]]
y = data["Price"]

model = LinearRegression()
model.fit(X,y)

new_car = pd.DataFrame({
    "Year":[2021],
    "Mileage":[18000],
    "Engine":[1800]
})

price = model.predict(new_car)

print("Predicted Car Price: ₹",round(price[0],2))

print("U.Lakshmi Chenna Kesava Reddy  - 192425206")
