import pandas as pd
import matplotlib.pyplot as plt
# import matplotlisb.axes as ax

dates = ["2016-07-05 03:00:00", "2016-08-06 16:00:00", "2016-12-07 21:00:00",
         "2016-19-08 23:00:00", "2016-25-09 06:00:00", "2016-12-10 21:00:00",
         "2016-10-11 21:00:00", "2016-10-12 04:00:00", "2017-01-01 07:00:00",
         "2017-01-02 07:00:00"]
app = ["Thermometer","Thermometer","Thermometer","Thermostat","Thermostat","Thermometer",
       "Thermostat","Thermometer","Thermostat","Thermometer"]
values = [22,19,25,21,20,18,21,20,19,23]
df = pd.DataFrame({"Date" : dates, "Appliance" : app, "Value":values})
df.Date = pd.to_datetime(df['Date'], format='%Y-%d-%m %H:%M:%S')
df=df.set_index('Date')

##########

df1 = df[df["Appliance"] == "Thermostat"]
df2 = df[df["Appliance"] == "Thermometer"]

plt.plot(df1.index, df1["Value"].values, marker="o", label="Thermostat")
plt.plot(df2.index, df2["Value"].values, marker="o", label="Thermmeter")
plt.gcf().autofmt_xdate()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig('test1.png')

##########

df1 = df[df["Appliance"] == "Thermostat"]
df2 = df[df["Appliance"] == "Thermometer"]

ax = df1.plot(y="Value", label="Thermostat")
df2.plot(y="Value", ax=ax, label="Thermometer")
ax.legend().figure.savefig('test2.png')
