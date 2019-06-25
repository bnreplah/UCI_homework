## SIEMS Day 3:  Guided Practice - Splunk Statistics with iplocation
--------

## Instructions

--------
In this activity, you will continue using the `fortinet_logs.csv` file to create four different statistical searches based criteria given below. 

#### Getting Started

Your search command will begin in the following way: 

- `source="fortinet_logs.csv" | iplocation src_ip| top limit=20 City, Country` 
 
**Please generate a statistical search for each of the following**: 
    
- Display where the count `is greater` than 30.
    
- Display where the percent `is greater` than 10%.
    
- Display where Country `is` United Kingdom.
    
- Display where Country `is not` United States.
    
* **Hint**: Review the `relational operators` [here](<https://docs.oracle.com/cd/E19253-01/817-6223/chp-typeopexpr-5/index.html>).
    
Activity Complete!


