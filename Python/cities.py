import pandas as pd
import os

OUTPUT_FILE = "data/cities.csv"

os.makedirs("data", exist_ok=True)

cities = [
    ("Mumbai","Maharashtra","West",20411000),
    ("Delhi","Delhi","North",32900000),
    ("Bengaluru","Karnataka","South",13608000),
    ("Hyderabad","Telangana","South",10628000),
    ("Ahmedabad","Gujarat","West",8450000),
    ("Chennai","Tamil Nadu","South",11324000),
    ("Kolkata","West Bengal","East",15134000),
    ("Pune","Maharashtra","West",7764000),
    ("Jaipur","Rajasthan","North",4300000),
    ("Lucknow","Uttar Pradesh","North",3382000),
    ("Kanpur","Uttar Pradesh","North",3200000),
    ("Nagpur","Maharashtra","West",3100000),
    ("Indore","Madhya Pradesh","Central",3000000),
    ("Thane","Maharashtra","West",2900000),
    ("Bhopal","Madhya Pradesh","Central",2500000),
    ("Visakhapatnam","Andhra Pradesh","South",2400000),
    ("Patna","Bihar","East",2500000),
    ("Vadodara","Gujarat","West",2200000),
    ("Ghaziabad","Uttar Pradesh","North",2100000),
    ("Ludhiana","Punjab","North",2000000),
    ("Agra","Uttar Pradesh","North",1900000),
    ("Nashik","Maharashtra","West",1800000),
    ("Faridabad","Haryana","North",1800000),
    ("Meerut","Uttar Pradesh","North",1700000),
    ("Rajkot","Gujarat","West",1700000),
    ("Varanasi","Uttar Pradesh","North",1600000),
    ("Srinagar","Jammu & Kashmir","North",1500000),
    ("Aurangabad","Maharashtra","West",1500000),
    ("Dhanbad","Jharkhand","East",1400000),
    ("Amritsar","Punjab","North",1400000),
    ("Allahabad","Uttar Pradesh","North",1300000),
    ("Ranchi","Jharkhand","East",1300000),
    ("Howrah","West Bengal","East",1200000),
    ("Coimbatore","Tamil Nadu","South",2200000),
    ("Jabalpur","Madhya Pradesh","Central",1200000),
    ("Gwalior","Madhya Pradesh","Central",1200000),
    ("Vijayawada","Andhra Pradesh","South",1100000),
    ("Jodhpur","Rajasthan","North",1200000),
    ("Madurai","Tamil Nadu","South",1600000),
    ("Raipur","Chhattisgarh","Central",1500000),
    ("Kota","Rajasthan","North",1100000),
    ("Guwahati","Assam","North East",1200000),
    ("Chandigarh","Chandigarh","North",1100000),
    ("Solapur","Maharashtra","West",1000000),
    ("Hubballi","Karnataka","South",950000),
    ("Mysuru","Karnataka","South",920000),
    ("Tiruchirappalli","Tamil Nadu","South",1000000),
    ("Bareilly","Uttar Pradesh","North",900000),
    ("Aligarh","Uttar Pradesh","North",900000),
    ("Moradabad","Uttar Pradesh","North",890000)
]

rows = []

for i, city in enumerate(cities, start=1):
    rows.append({
        "city_id": i,
        "city_name": city[0],
        "state": city[1],
        "region": city[2],
        "population": city[3],
        "is_active": 1
    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print("===================================")
print("cities.csv generated successfully!")
print(f"Total Cities : {len(df)}")
print("===================================")