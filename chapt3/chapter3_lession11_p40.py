email = "thotyno@vlute.com"

Dem_Username = 1
Dem_Companyname = 1

Dem_Username=email.find('@')
username = email[:Dem_Username]

Dem_Companyname=email.find('.')
Companyname = email[Dem_Username+1:Dem_Companyname]

print("username là", username, "và companyname là", Companyname)