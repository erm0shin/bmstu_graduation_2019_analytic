# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

# dates = ["2016-07-05 03:00:00", "2016-08-06 16:00:00", "2016-12-07 21:00:00",
#          "2016-19-08 23:00:00", "2016-25-09 06:00:00", "2016-12-10 21:00:00",
#          "2016-10-11 21:00:00", "2016-10-12 04:00:00", "2017-01-01 07:00:00",
#          "2017-01-02 07:00:00"]
dates = ["1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр",
         "1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр",
         "1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр"]
# app = ["Thermometer","Thermometer","Thermometer","Thermostat","Thermostat","Thermometer",
#        "Thermostat","Thermometer","Thermostat","Thermometer"]
app = ["2016", "2016", "2016", "2016",
       "2016", "2016", "2016", "2016",
       "2017", "2017", "2017", "2017",
       "2017", "2017", "2017", "2017",
       "2018", "2018", "2018", "2018",
       "2018", "2018", "2018", "2018"]
# values = [22,19,25,21,20,18,21,20,19,23]
values = [22, 19, 25, 21,
          20, 18, 21, 20,
          32, 39, 35, 31,
          30, 38, 31, 30,
          42, 49, 45, 41,
          40, 48, 41, 40]
df = pd.DataFrame({"Date": dates, "Appliance": app, "Value": values})
# df.Date = pd.to_datetime(df['Date'], format='%Y-%d-%m %H:%M:%S')
df=df.set_index('Date')

##########

df1 = df[df["Appliance"] == "2016"]
df2 = df[df["Appliance"] == "2017"]
df3 = df[df["Appliance"] == "2018"]

plt.plot(df1.index, df1["Value"].values, marker="o", label="2016")
plt.plot(df2.index, df2["Value"].values, marker="o", label="2017")
plt.plot(df3.index, df3["Value"].values, marker="o", label="2018")
plt.gcf().autofmt_xdate()
plt.xlabel(u"Семестр")
plt.ylabel(u"Успеваемость, %")
plt.title(u"Успеваемость кафедры ИУ6 по предмету \"Информатика\"")
plt.legend()

plt.savefig('semester_stat.png')
