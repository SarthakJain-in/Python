import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

temp = data["temp"]

mean_temp = temp.mean()
print(mean_temp)

max_temp = temp.max()
print(max_temp)

print(data[data.temp == data.temp.max()])