# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_datadf = pd.read_csv(file_to_load)
purchase_datadf.head(4)
uniquedf = purchase_datadf.drop_duplicates(subset='SN', keep='first', inplace=False)
playercount =[]
playercount= uniquedf.count()
pcount = playercount[1]
#define player count
pcount
unique_itemsdf = purchase_datadf.drop_duplicates(subset='Item Name' ,keep='first', inplace=False)
unique_itemsdf.count()
itemcount=[]
itemcount = unique_itemsdf.count()
uicount=itemcount[1]
#defined unique item count
groupedbyitemdf = purchase_datadf.groupby(['Item Name']).mean()
avgitemprice=[]
avgitemprice = groupedbyitemdf['Price']
#defined average item price by item 
avgcost=purchase_datadf.mean()
averagepurchcost= avgcost[3]
#defined average purchase cost
totalrevenue = purchase_datadf['Price'].sum()
#defined total revenue
countofpurchasesdf =purchase_datadf.groupby(['Item Name']).count()
totaltransactions= countofpurchasesdf.sum()
transcount =totaltransactions[1]
#definedcountofpurchases
irtotal = purchase_datadf.groupby(['Item Name']).sum()
irtotalprice =[]
irtotalprice=irtotal['Price']
#Defined total revenue by item
newstr=[transcount,averagepurchcost,uicount,totalrevenue]
#topdf = pd.DataFrame({'Transaction Count':str(transcount),'Avg Price':str(averagepurchcost),'Unique Item Count':str(uicount)})
topdf=pd.DataFrame(newstr, index=['Transaction Count','Average Price','Unique Item Count','Total Revenue'])
# Created new DF with toplevel overview
ipcount =[]
ipcount = countofpurchasesdf['Purchase ID']
newdf = pd.DataFrame({'Purchase Count':ipcount[:],'Avg Price':avgitemprice[:],'Total Revenue':irtotalprice[:]})
#Created new DF with item related statistics :D
sorteddf = newdf.sort_values(by=['Total Revenue'], ascending=False)
top5df = sorteddf.head(5)
topdf.head()
top5df
unique_sndf = purchase_datadf.drop_duplicates(subset='SN' ,keep='first', inplace=False)
maledf =unique_sndf[unique_sndf['Gender']=='Male']
otherdf =unique_sndf[unique_sndf['Gender']=='Other / Non-Disclosed']
femaledf =unique_sndf[unique_sndf['Gender']=='Female']
#defined df with gender specific results
meep=maledf.count()
maletot=meep[1]
maletot
meeep=femaledf.count()
femaletot=meeep[1]
meeeep=otherdf.count()
othertot=meeeep[1]
userstot=maletot+femaletot+othertot
#defining counts by gender
maleper=maletot/userstot
femaleper=femaletot/userstot
otherper=othertot/userstot
#defining gender percent breakdown
genstr = [maletot,maleper,femaletot,femaleper,othertot,otherper]
genderdf =pd.DataFrame(genstr, index=['Male Count','Male Percent','Female Count','Female Percent','Other Counnt','Other Percent'])
genderdf
#Print Output :)

writer = pd.ExcelWriter('output1.xlsx')
newdf.to_excel(writer,'Overview')
topdf.to_excel(writer,'ItemBreakdown')
top5df.to_excel(writer,'Top5Items')
genderdf.to_excel(writer,'GenderBreakdown')
writer.save()