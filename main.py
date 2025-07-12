import pandas as pd 
airlines = pd.read_csv("D:/pandas project/airlines.csv")
airports = pd.read_csv("D:/pandas project/airports.csv")
flights = pd.read_csv("D:/pandas project/flights.csv" , dtype = {7 : str , 8 : str})

airlines.columns = airlines.columns.str.strip()
airports.columns = airports.columns.str.strip()
flights.columns = flights.columns.str.strip()

# 📌 1. Which airline had the most flights in the dataset?

# merged = pd.merge(airlines , flights , left_on = 'IATA_CODE' , right_on = 'AIRLINE' , how = 'right' , suffixes = ("_airline" , "_flights"))
# res_merged = merged.groupby("AIRLINE_airline").size().reset_index()
# res_merged.columns = ['Airrline' , 'No_of_flights']
# res_merged.sort_values(by = 'No_of_flights' , inplace = True ,ascending=False)
# print(res_merged.head(1))

# 📌 2. Which airport had the highest number of departures?

# merged = pd.merge(flights , airports , left_on = 'ORIGIN_AIRPORT' , right_on = 'IATA_CODE' ,how = 'left' , suffixes = ('_flights' , '_airports'))
# depart_count = merged.groupby('AIRPORT').size().reset_index()
# depart_count.columns = ['Airport' ,'No_of_Dept']
# depart_count.sort_values(by = 'No_of_Dept' , ascending= False , inplace = True )
# print(depart_count.head(1))

# 📌 3. What is the average arrival delay per airline?

# merged = pd.merge(flights , airlines , left_on = 'AIRLINE' , right_on = 'IATA_CODE' , how = 'left' , suffixes=('_flights' , '_airlines'))
# avg_arvl_delay = merged.groupby('AIRLINE_airlines')['ARRIVAL_DELAY'].mean().reset_index()
# avg_arvl_delay.columns = ['Airline' , 'Avg_ar_delay']
# print(avg_arvl_delay)

# 📌 4. Which route (origin to destination) is the busiest?

# flights['Route'] = flights['ORIGIN_AIRPORT'] + '-' + flights['DESTINATION_AIRPORT']
# busy_route = flights.groupby('Route').size().reset_index()
# busy_route.columns = ['Route' , 'flight_count']
# busy_route.sort_values(by ='flight_count' , ascending= False ,inplace=True )
# print(busy_route.head(1))

# 📌 5. Top 5 cities with most incoming flights.

# merged = pd.merge(flights , airports , left_on = 'DESTINATION_AIRPORT' , right_on = 'IATA_CODE' , how = 'left' , suffixes = ('_flights ' , '_airports'))
# top_city = merged.groupby('CITY').size().reset_index()
# top_city.columns = ['City' ,'incm_flights']
# top_city.sort_values(by = 'incm_flights' , ascending=False , inplace=True )
# print(top_city.head(5))

# 📌 6. Which airline had the highest average departure delay?

# merged = pd.merge(flights, airlines , left_on = 'AIRLINE' , right_on = 'IATA_CODE' , how='left' , suffixes=('_flight' ,'_airlines'))
# avg_dep_delay = merged.groupby('AIRLINE_airlines')['DEPARTURE_DELAY'].mean().reset_index()
# avg_dep_delay.columns = ['Airline' , 'Avg_delay']
# avg_dep_delay.sort_values(by = 'Avg_delay' , ascending=False , inplace=True)
# print(avg_dep_delay.head(1))

# 📌 7. What percentage of flights were cancelled per airline?

# merged = pd.merge(flights , airlines , left_on='AIRLINE' , right_on ='IATA_CODE' , how='left' , suffixes=('_flights' , '_airlines'))
# cncl_per = merged.groupby('AIRLINE_airlines').agg(total_flights  = ('CANCELLED' , 'count') , cncl_flights = ('CANCELLED' , 'sum')).reset_index()
# cncl_per['cncl_percentage'] = cncl_per['cncl_flights']/cncl_per['total_flights']*100
# cncl_per.sort_values(by = 'cncl_percentage' , ascending=False , inplace=True)
# print(cncl_per[['AIRLINE_airlines' , 'cncl_percentage']])

# 📌 8. What is the average air time for each airline on flights longer than 1000 miles?

merged = pd.merge(flights , airlines , left_on='AIRLINE' , right_on ='IATA_CODE' , how='left' , suffixes=('_flights' , '_airlines'))
merged = merged[merged['DISTANCE'] > 1000]
avg_air_time = merged.groupby('AIRLINE_airlines')['AIR_TIME'].mean().reset_index()
avg_air_time.columns = ['Airline'  , 'avg_airTime']
print(avg_air_time)
