import pandas as pd

chocolates = pd.read_csv("/tmp/flavors_of_cocoa.csv")
chocolates.rename(columns={"Company Location": "Location"}, inplace=True)
chocolates.to_csv("/tmp/cocoa_backup.csv")

chocolates["Cocoa Percent"] = chocolates["Cocoa Percent"].str.rstrip("%").astype(float)

#print(chocolates.head(10))
#print(chocolates[['Company', 'Company Location', 'Rating']])

#print(chocolates[chocolates['Rating'] > 4])

#print(chocolates['Rating'].mean())

#chocolates["Cocoa Percent"] = chocolates["Cocoa Percent"].str.rstrip("%").astype(float)
#print(chocolates["Cocoa Percent"].agg(["min", "max"]))

#print(chocolates[chocolates["Company Location"] == 'France'])

#print(chocolates.sort_values(by="Rating",ascending=False))

#print(chocolates.groupby("Company Location")['Rating'].mean())

#print(chocolates[(chocolates['Company Location'] == 'France') & (chocolates['Rating'] >= 4.0)][['Company','Rating']])

#print(chocolates[chocolates['Company Location'] == 'France']['Rating'].mean())

#print(chocolates.loc[chocolates['Company Location'] == 'France', 'Rating'].mean())

#print(chocolates[chocolates['Cocoa Percent'] == '90%'])

#print(chocolates['Company'].nunique())

#print(len(chocolates.groupby('Company Location')))

#print(chocolates['Company Location'].nunique())


#print(chocolates[
#          (chocolates['Rating'] >= 3.5) & (chocolates['Rating'] <= 4.0)
#      ])

#print(chocolates.sort_values(by=['Company Location','Rating'], ascending=[True,False]))

#print(chocolates[
#    (chocolates['Company Location'] == 'France') & (chocolates['Rating'] > 1.0)
#].sort_values("Rating",ascending=False)[['Company','Company Location','Rating']])

#print(chocolates[ chocolates["Company Location"] == 'France'].sort_values("Rating",ascending=False).head(5))

#french_chocolates = chocolates[ chocolates['Company Location'] == 'France']
#average = french_chocolates['Rating'].mean()
#print( french_chocolates[ french_chocolates['Rating'] > average ])


#print(chocolates[ chocolates['Company Location'] == chocolates.groupby("Company Location")["Company Location"].count().sort_values(ascending=False).head(1).idxmax()] )
#print(chocolates[ chocolates['Company Location'] == chocolates.groupby("Company Location")["Company Location"].count().idxmax()])

#print(chocolates.groupby("Location")['Rating'].mean().idxmax())


#print(chocolates[ chocolates['Location'] != 'France'].
#      sort_values(by='Rating',ascending=False).head(5)[['Company', 'Location', 'Rating', 'Cocoa Percent']])






