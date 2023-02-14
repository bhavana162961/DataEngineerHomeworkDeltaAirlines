# DataEngineerHomeworkDeltaAirlines
**Pre-Requisites :**
If you have any pre installed IDE's like VsCode, jupyter notebook, PyCharm etc. Please feel free to use those IDE's to run the python file
If you want to run through the CLI, follow the below steps:
Open the command prompt and run the following command to check that a suitable Python version is installed: 

python --version

If is it not installed, please install python.
Update Pip and Wheel to ensure you have the latest version installed: 

pip install --upgrade pip wheel

To install pandas package:
pip install pandas

**How to run the python file?**
Firsty, Clone the Git project

If you are running the python file in the command prompt, please follow the steps below:
1. Find the python file path
2.Open command prompt and switch to your Python file's directory
3.Enter the "python" command and your file's name. 
For ex :  python "FlightStatus.py" in our case

**Note :** Make sure the input file is in the same folder as that of the project.

If you are using any IDE
Open the folder which contains the clone from git repository and click on FlightStatus.py file. The code should shown on editor. 
On top, check for run button and click on it to run the file.


**Method Description:**
getAllFlightStatus(filePath)
We can implement this method in two different approaches

Input : csv file path
Output: Dataframe displaying the all the flights with there recent flight status

This method takes csv file path as input. Here we are skipping the first 7 lines as those contain the departure statistics which is not the data we want to parse.

Approach 1 : (Time complexity O(NlogN))

From 8th line, using pandas package, read the data from csv into a data frame. Add an extra column (date_time) which is a combination of flight_dt and lastupdt cloumns time and converted it to datetime object. Sorted all the data by date_time in descending order. By using the fight key, drop duplicates by keeping the first record. And the drop the newly created date_time column, return and display the data frame. 

Approach 2 : (Time complexity O(N))
From 8th line, using pandas package imported the data into a dataframe and iterated to those records and inserted into a dictionary with key as flightKey and value as FlightDetails object.
While iterating, If a new record comes in, we insert into the dictionary.If an existing record comes in, then the flight datetime will be compared with prev datetime. If current datetime is greater, then replace the dictionary with current flight details for the same flightkey.
At the end of iteration, take all the dict values as list, print and also return the same.

**Sample test cases:** 
Testcase 1:
Carrier Code	flight_dt	flightnum	orig_arpt	dest_arpt	flightstatus	lastupdt	flightkey
DL			1/1/2019	15		ATL		TPA		Arrived		19:48		DL4346615ATLTPA
DL			1/1/2019	15		ATL		TPA		Boarding		19:17		DL4346615ATLTPA
DL			1/1/2019	91		ATL		RSW		Boarding		17:20		DL4346691ATLRSW

output
Carrier Code	flight_dt	flightnum	orig_arpt	dest_arpt	flightstatus	lastupdt	flightkey
DL			1/1/2019	15		ATL		TPA		Arrived		19:48		DL4346615ATLTPA
DL			1/1/2019	91		ATL		RSW		Boarding		17:20		DL4346691ATLRSW

Testcase 2:
Carrier Code	flight_dt	flightnum	orig_arpt	dest_arpt	flightstatus	lastupdt	flightkey
DL			1/1/2019	15		ATL		TPA		Arrived		19:48		DL4346615ATLTPA
DL			1/2/2019	15		ATL		TPA		Boarding		19:17		DL4346615ATLTPA
DL			1/1/2019	91		ATL		RSW		Boarding		17:20		DL4346691ATLRSW

output
Carrier Code	flight_dt	flightnum	orig_arpt	dest_arpt	flightstatus	lastupdt	flightkey
DL			1/2/2019	15		ATL		TPA		Boarding		19:17		DL4346615ATLTPA
DL			1/1/2019	91		ATL		RSW		Boarding		17:20		DL4346691ATLRSW

**Note :** Make sure the input file is in the same folder as that of the project.
