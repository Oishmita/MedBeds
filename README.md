# MedBeds

A software used to track the number of vacant and occupied beds based on the readings from the ESP32 microcontroller (which detects the occupancy of each bed with the help of the readings obtained from the piezoelectric sensors attached to each bed).

# A brief overview

I have developed a system where we can keep a track of the no. of occupied and no. of vacant beds, for each department of a particular hospital.

On the hospital side, we have an ESP32 microcontroller in each department of a particular hospital. In each department, every bed will be provided with a mesh of piezoelectric sensors underneath, which would be able to detect the presence of a human via his weight.

The readings from each bed will then be fed to the ESP32 microcontroller unit. The readings will be checked against a threshold value, provided in the code and accordingly, number of beds occupied and number of beds vacant will be obtained, provided that the total number of beds is given in each ESP32 unit, for each department. Then it will send the data collected to the php file, via Wi-Fi network, only after a specified amount of time (Here, around 1 min. It can be altered to 1 or 2 hours, when used in real time, so that the status of bed occupancy doesn't change when a patient is away for a specified amount of time, ignoring the reading of the sensors for that amount of time.)

The data from the ESP32 unit will then be fed to one php file, which will collect the data from the ESP32 and enter the data into the database located in the localhost, phpMyAdmin.

Another php file will extract the real-time data from the database and display it on the website.

Database is created with the help of phpMyAdmin. XAMPP is used to connect the computer to the phpMyAdmin MySQL DBMS and to enable Apache (So that python can be used to connect with the database.) 

The database will have the bed status of every hospital, with every department specified. Since we do not have the scope to build such a hospital system in real-time, we have used dummy databases to show how the python application will filter the data after collecting it from the database and show the results in the application. 
The application has 2 windows and 2 python program files linked. As we run the application, first the main page will be displayed then if we click on the “check hospitals” button, Hospital name, along with the departments under the hospital will be displayed on the right display. 

When the “Book a bed” button is clicked, another page will open up, to enter the details. If we enter the correct details, then the no. of beds occupied and the no. of beds vacant will be displayed on the application. Then after that if we click the “Book and get token” button, an unique token will be generated and displayed on the application, which will then be noted down by the hospital. The patient has to note down the token number and get to the hospital within 24 Hours to book a bed with that token. (Token will be invalid after 24 Hours and will be different for every patient). 
If we enter wrong department name in the application, then the bed count will show “NA” 
If we enter wrong hospital name in the application, then an error pop up will be generated and will show “Wrong input!” and the application will be closed automatically.  
Then, to book a bed, the application has to be re-started. 
