import pandas as pd
from datetime import datetime

class FlightDetails:
    def __init__(self, carrierCode, flightDate, flightNum, orgination, destination, status, lastUpdated, flightKey):
        self.carrierCode = carrierCode
        self.flightDate = flightDate
        self.flightNum = flightNum
        self.orgination = orgination
        self.destination = destination
        self.status = status
        self.lastUpdated = lastUpdated
        self.flightKey = flightKey
    
    def __str__ (self):
        return 'carrierCode=' + str(self.carrierCode) + ' ,flightDate=' + str(self.flightDate) + ' ,flightNum=' + str(self.flightNum) + ' ,orgination=' + str(self.orgination) + ' ,destination=' + str(self.destination) + ' ,status=' + self.status + ' ,lastUpdated=' + str(self.lastUpdated) + ' ,flightKey=' + self.flightKey 

def getAllFlightsStatus(fileName):
    
    mydict = {}
    df = pd.read_csv(fileName, skiprows=7, header =0)
    for index, row in df.iterrows():
        
        if(pd.isna(row['flightkey']) or pd.isna(row['flight_dt']) or pd.isna(row['lastupdt'])) : 
            continue
        
        key = row['flightkey']
        
        if key not in mydict:
            mydict[key] = FlightDetails(row['Carrier Code'], row['flight_dt'], row['flightnum'], row['orig_arpt'], row['dest_arpt'], row['flightstatus'], row['lastupdt'], row['flightkey'])
        else:
           
            date_time_str = str(row['flight_dt']) + " " + str(row['lastupdt'])
            date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %H:%M')
            prev_date_time_str = str(mydict[key].flightDate) +  " " + str(mydict[key].lastUpdated)
            prev_date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %H:%M')
            if date_time_obj > prev_date_time_obj :
                mydict[key] = date_time_obj
                
    return list(mydict.values())

dict_val = getAllFlightsStatus("Dummy_Flight_Leg_Data.csv")

for a in dict_val:
    print(a)

