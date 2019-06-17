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
values = [78, 72, 74, 80,
          78, 84, 79, 87,
          74, 71, 72, 79,
          77, 82, 86, 89,
          75, 71, 72, 76,
          79, 82, 84, 86]
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
plt.title(u"Успеваемость кафедры ИУ6")
plt.legend()

plt.savefig('semester_stat_perf.png')
