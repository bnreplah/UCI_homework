## SIEMS Day 3:  Guided Practice - Splunk Statistics with iplocation
--------

## Solution

--------

Generate a statistical search for each of the following: 

- Display where the count is greater than 30

   **Solution:** source="fortinet_logs.csv" | iplocation src_ip| top limit=20 City , Country | where count > 30

- Display where the percent is greater than 10%

   **Solution:** source="fortinet_logs.csv" | iplocation src_ip| top limit=20 City , Country | where percent > 10

- Display where Country is United Kingdom

   **Solution:** source="fortinet_logs.csv" | iplocation src_ip| top limit=20 City , Country | where Country = "United Kingdom"

- Display where Country is not United States

   **Solution** source="fortinet_logs.csv" | iplocation src_ip| top limit=20 City , Country | where Country != "United States"
  
- Explain that it's advantageous to sort by count of city and country because if you are looking at an attack that has occurred, you can see whether there is a location that has the greatest volume of source IPs. Once you have this information, you can consider temporarily blocking traffic from that location. 