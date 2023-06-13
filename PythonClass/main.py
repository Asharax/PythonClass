import os

#import keras as keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy as np
from pandas import Series, DataFrame
import seaborn as sns


#pandas profiling çalışmayacak
#ydata_profiling kütüphanesi kullanarak yapılacak bu ödev.... (Sunu 10)

# kütüphanenin import edilmesi
import pandas as pd
# ydata_profiling kütüphanesi import edilmesi
from ydata_profiling import ProfileReport

import ydata_profiling
print(ydata_profiling.__version__)

print("pandas versiyon")
print(pd.__version__)


# veri setinin GitHub’tan alınması
df =pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/article-resources/master/Essential%20Statistics/middle_tn_schools.csv')
print(df)

print (df.columns)
print()
print (df.info())
print()


print(df.describe())
print()
print(df.shape)
print()
print(df.size)
print()




print(df.isnull())
print()
print(df.count())
print()
print( df.isnull().sum().sum())
print()
print(df.isnull().sum())

# dataframe'deki her satırın NaN sayısının hesabı
for i in range(len(df.index)) :
    print("Dataframe Satırlarındaki NaN sayısı ", i , " : " ,df.iloc[i].isnull().sum())

print( )
print(ydata_profiling.__version__)
print()
print()
print()



exit('file_reading_bellow')
df = pd.read_csv("https://raw.githubusercontent.com/LearnDataSci/article-resources/master/Essential%20Statistics/middle_tn_schools.csv")
# profil raporunun üretilmesi
profile = ProfileReport(df, title="Okul Profil Raporu")
# profil raporunun kaydedilmesi
profile.to_file("okul__profil__raporu.html")







exit('9. sunu sonu')

#versiyon=keras.__version__
#print("keras kütüphanesi versiyon: ", versiyon)


exit('8. sunu sonu')


df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv')

# Grafik oluşturma
fig, ax = plt.subplots()
# sepal uzunluğu ve sepal genişliği için dağılım grafiği(scatter)
ax.scatter(df['sepal_length'], df['sepal_width'])
# başlık ilavesi
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_uzunluk')
ax.set_ylabel('sepal_genişlik')

 # Renkler için dictionary oluşturulması
colors = {'setosa':'red', 'versicolor':'green','virginica':'yellow'}
fig, ax = plt.subplots()
for i in range(len(df['sepal_length'])):
    ax.scatter(df['sepal_length'][i], df['sepal_width'][i],color=colors[df['species'][i]])

# başlık ve eksenlerin tanımlanması
ax.set_title('iris Dataset')
ax.set_xlabel('sepal uzunluk')
ax.set_ylabel('sepal genişlik')



plt.show()



exit(ax)


print('sys.path')
print(sys.path)
print('sys.platform')
print(sys.platform)
print('os.getcwd()')
print(os.getcwd())
print('os.name')
print(os.name)
print('os.listdir()')
print(os.listdir())





# Hafta 8 Sayfa 55'e kadar dahil
# 70 sorudan vize final, samle, head, tail

titanic_df =pd.read_csv('https://raw.githubusercontent.com/felipegonzalez/aprendizaje_estadistico_2015/master/clases/clase_12/datos/train_titanic.csv')
import matplotlib.pyplot as plt
ERP = ['Infor','Oracle','SAP','Axapta']
pazar_payi = [10,30,45,15]
colors = ['yellow','green','red','blue']
plt.pie(pazar_payi, labels=ERP, colors=colors)
plt.axis('equal')
plt.show()



print(titanic_df.tail(15))
print(titanic_df.sample()) # sample fuınction returns 1 random row by default.
print(titanic_df.info())
print(titanic_df.info(verbose=False )) # verbose=False will give you a more compact summary

#print (sns.factorplot('Sex', data=titanic_df,kind='count'))
print (sns.catplot('Sex', data=titanic_df,kind='count'))
print (sns.catplot(x="Sex", hue="Survived", kind="count", data=df))
print (sns.catplot(x ="Survived", kind ="count", data = df))
##print(sns.factorplot('Sex', data=titanic_df,kind='count')) ##Does not work



df = pd.DataFrame({
'ülke': ['Kazakistan', 'Romanya', 'Polonya', 'Macaristan'],
'nüfus': [17.04, 19.6, 38.1, 10.0],
'yüzölçüm': [2724902, 230170, 312679, 93025]
}, index=['KZ', 'RO', 'PL', 'HU'] )

#find null data count in a dataframe named df
print('df.isnull().sum().sum()')



df['nüfus__yoğunluğu'] = df['nüfus'] /df['yüzölçüm'] * 1000000

df['nüfus__yoğunluğu']
print('df.size')
print(df.size)
#find dataframe size
print('df.shape')
print(df.shape)
del df['nüfus__yoğunluğu']
## soru 5??????
print (df)

print (df.sample())
print ('df.sample()')
print (df.sample())

exit()


df=pd.read_csv("https://raw.githubusercontent.com/roberthryniewicz/datasets/master/airline-dataset/flights/flights.csv")

print(df.loc[:,'FlightNum'])











# 1.Veri setini oku
AYTAN_DF = pd.read_csv("steam.csv")

# 2.Dataframe ile ilgili özet bilgiler
print(AYTAN_DF.info())

# 3.Pandas versionu
print(f"pandas versiyonu: {pd.__version__}")

# 4.Install edilen kütüphanelerin listesi
## print(sys.modules.keys())

# 5.Python Yazılımın Versiyonunu bulunuz
print(sys.version)

# 6.İlk 5 veri
print(AYTAN_DF.head())

# 7.Son 5 veri
print(AYTAN_DF.tail())

# 8.Bütün veriler
print(AYTAN_DF)

# Numerik alanları listele
# AYTAN_DF.select_dtypes(include='number')

# Veri setindeki nümerik olmayan alanların frekans dağılımının analizi
AYTAN_DF.describe(include=['object', 'bool']).T
print(AYTAN_DF.describe(include=['object', 'bool']).T)
# Histogram diyagramının çizimi
plt.show()

# AYTAN_DF.describe(include=['object', 'bool']).T
# plt.pyplot.show()



df = pd.read_csv(
    'https://raw.githubusercontent.com/yew1eb/DM-Competition-Getting-Started/master/AV-loan-prediction/train.csv')
# print(csvDf['Property_Area'].value_counts())
df['ApplicantIncome'].hist(bins=50)
print(AYTAN_DF.describe().T)

plt.pyplot.show()

okyanus_derinlik = pd.Series({
    'Kuzey Denizi': 1205,
    'Atlas': 3646,
    'Hint': 3741,
    'Pasifik': 4080,
    'Güney Okyanusu': 3270
})

max_derinlik = pd.Series({
    'Kuzey Denizi': 5567,
    'Atlas': 8486,
    'Hint': 7906,
    'Pasifik': 10803,
    'Güney Okyanusu': 7075
})

derinlikler = pd.DataFrame({
    'ortalama Derinlik (metre)': okyanus_derinlik,
    'Maksimum Derinlik (metre)': max_derinlik
})

df = derinlikler

print(df.tail(-1))

print(df.sample(5))

dates = pd.date_range('20170101', periods=14)
print(dates)

dates = pd.date_range('20170101', periods=14,
                      freq='M')
print(dates)

dates = pd.date_range(start='1/1/2017', end='1/08/2017')
print(dates)

dates = pd.date_range(start='1/1/2017', end='1/08/2017', freq='2D')
print(dates)

dates = pd.date_range('20170101', freq='5H', periods=14)
print(dates)
