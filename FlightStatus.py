import pandas as pd
def getAllFlightsStatus(filename):
    df = pd.read_csv(filename, skiprows=7, header =0)
    df['lastupdt'] = df['lastupdt'].astype(str)
    df['flight_dt'] = df['flight_dt'].astype(str)
    df = df.dropna(subset=['flightkey', 'flight_dt', 'lastupdt'])
    df['date_time'] = df[['flight_dt', 'lastupdt']].agg(' '.join, axis=1)
    df['date_time'] = pd.to_datetime(df['date_time'], format = '%m/%d/%Y %H:%M', errors='coerce')
    df.sort_values(by='date_time', ascending=False, inplace=True)
    df.drop_duplicates(subset='flightkey', keep='first', inplace=True)
    df.sort_values(by='flightnum', ascending=True, inplace=True)
    df.drop('date_time', inplace=True, axis=1)
    return df


display(getAllFlightsStatus("Dummy_Flight_Leg_Data.csv"))
