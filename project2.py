print("----------------RAILWAY TICKET RESERVATION & FARE MANAGEMENT SYSTEM----------------\n")
#available classes and base fares
classes=("Sleeper","AC 2 Tier","AC 3 Tier")
base_fare=(450,900,1500)
#entering passenger name
passenger_name=input("Enter passenger name:")
#name validation
if(passenger_name.replace(" ","").isalpha()!=True):
    print("Invalid passenger name!")
    quit()
#entering passenger age
passenger_age=int(input("Enter passenger age:"))
#age validation
if (passenger_age<1 or passenger_age>120):
    print("Invalid age!")
    quit()
#entering passenger gender
passenger_gender=input("Enter passenger gender{Male/Female/other}:")
#gender validation
if(passenger_gender not in ("Male","Female","other")):
    print("Invalid gender!")
    quit()
#entering source & destination
source_station=input("Enter source station:")
dest_station=input("Enter destination station:")
#validation of stations
if(source_station==dest_station):
    print("Source and destination cannot be same!")
    quit()
#entering travel class
travel_class=input("Choose travel class:-Sleeper,AC 2 Tier,AC 3 Tier:")
#validating travel class
if(travel_class not in classes):
    print("Invalid Travel Class!")
    quit()
#finding index of travel class
class_index=classes.index(travel_class)
#finding cost of travel without discount
class_fare=base_fare[class_index]
#cost with discount
if(passenger_age<5):
    dist_fare=class_fare-100/100*class_fare
elif(passenger_age>=5 and passenger_age<=11):
    dist_fare=class_fare-50/100*class_fare
elif(passenger_age>=60):
    dist_fare=class_fare-30/100*class_fare
else:
    dist_fare=class_fare-0/100*class_fare
#finding passenger category
if(passenger_age<5):
    category="Infant"
elif(passenger_age>=5 and passenger_age<=17):
    category="Child"
elif(passenger_age>=18 and passenger_age<=59):
    category="Adult"
else:
    category="Senior Citizen"
#allocating coach
if(travel_class=="Sleeper"):
    coach="C1"
elif(travel_class=="AC 3 Tier"):
    coach="B2"
else:
    coach="A1"
#assigning seat type
if(passenger_age<12 or passenger_age>=60):
    berth="Lower"
else:
    berth="Upper"
#final ticket display
print("====================================================")
print("             INDIAN RAILWAYS E-TICKET")
print("====================================================")
#alignment of output
print(f"{'Passenger Name':<18}: {passenger_name}")
print(f"{'Age':<18}:{passenger_age}\nGender: {passenger_gender}")
print(f"{'Category':<18}: {category}")
print(f"{'Journey':<18}: {source_station}->{dest_station}")
print(f"{'Travel Class':<18}: {travel_class}")
print(f"{'Coach':<18}: {coach}\nSeat type: {berth}")
print(f"{'Base fare':<18} : ₹{class_fare}")
print(f"{'Discount':<18} : ₹{class_fare-dist_fare}")
print(f"{'Total fare':<18} : ₹{dist_fare:.2f}")
print(f"{'Booking status':<18} : Confirmed")
      