import pandas as pd
import random
import matplotlib.pyplot as plt

pasg = pd.read_csv("./titanic.csv")
print(pasg) #Задание 1

zad2_1 = pasg.loc[((pasg["Age"]>30) & (pasg["Age"]<40)) & (pasg["Sex"] == "male"), ["Name", "Sex", "Age"]]
zad2_2 = pasg.loc[((pasg["Age"]<25) & (pasg["Sex"] == "female")) | (pasg["Pclass"] == 1), ["Name", "Sex", "Age" ,"Pclass"]]

print(zad2_1)
print(zad2_2)

#Задание 3
sex_surv = pasg[["Sex", "Pclass"]]
s_s = sex_surv.groupby(["Sex", "Pclass"]).size()
s_s.plot.bar()
plt.show()


#Задание 4
zad4 = pasg[(pasg["Age"]<25)]
s_s = zad4.groupby(["Sex","Pclass","Survived"]).size()
s_s.plot.bar()
plt.show()

