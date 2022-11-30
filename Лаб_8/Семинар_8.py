import pandas as pd
import random
import matplotlib.pyplot as plt
import math as math

pasg = pd.read_csv("./titanic.csv")

a_s = pasg[(pasg["Age"]<20) & (pasg["Sex"] == "male")]

a_s2 = pasg[((pasg["Age"]>20) & (pasg["Age"]<30)) & ((pasg["Sex"] == "female") | (pasg["Pclass"] == 1)) ]
            #Пассажиры первого класса и девушка и в возрасте от 20 до 30

a_s3 = pasg.loc[(pasg["Age"]>40) & (pasg["Pclass"] == 3), ["Name"]]

sl = pasg.iloc[500:-100,[1,3,6]]
            # Вывел от 500 до -100 с конца 1,3,6 столбец

sex_surv = pasg[["Sex", "Survived"]]
s_s = sex_surv.groupby(["Sex", "Survived"]).size()
s_s.plot.bar()
plt.show()


# print(sl)
