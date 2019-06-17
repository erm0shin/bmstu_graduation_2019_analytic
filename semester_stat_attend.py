# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

dates = ["1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр",
         "1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр",
         "1 семестр", "2 семестр", "3 семестр", "4 семестр",
         "5 семестр", "6 семестр", "7 семестр", "8 семестр"]
app = ["2016", "2016", "2016", "2016",
       "2016", "2016", "2016", "2016",
       "2017", "2017", "2017", "2017",
       "2017", "2017", "2017", "2017",
       "2018", "2018", "2018", "2018",
       "2018", "2018", "2018", "2018"]
values = [82, 76, 70, 70,
          60, 63, 72, 65,
          84, 77, 72, 70,
          66, 68, 76, 75,
          80, 75, 71, 71,
          64, 66, 75, 72]
df = pd.DataFrame({"Date": dates, "Appliance": app, "Value": values})
df = df.set_index('Date')

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
plt.title(u"Посещаемость кафедры ИУ6")
plt.legend()

plt.savefig('semester_stat_attend.png')
