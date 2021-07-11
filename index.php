<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="5" >
    <link rel="stylesheet" type="text/css" href="style.css" media="screen"/>

	<title> Sensor Data </title>

</head>

<body>

    <h1>SENSOR DATA</h1>
<?php
$servername = "localhost";
$username = "root";
$password = "medbeds@123";
$dbname = "medbeds";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT Department, Date, Time, No_of_beds_occ, No_of_beds_vac FROM real_time_amri_data"; /*select items to display from the real_time_amri_data table in the data base*/

echo '<table cellspacing="5" cellpadding="5">
      <tr> 
        <th>Department</th> 
        <th>Date</th>  
        <th>Time</th> 
        <th>No_of_beds_occ</th> 
        <th>No_of_beds_vac</th>      
      </tr>';
 
if ($result = $conn->query($sql)) {
    while ($row = $result->fetch_assoc()) {
        $row_Department = $row["Department"];
        $row_Date = $row["Date"];
        $row_Time = $row["Time"];
        $row_No_of_beds_occ = $row["No_of_beds_occ"];
        $row_No_of_beds_vac = $row["No_of_beds_vac"]; 
        
        // Uncomment to set timezone to - 1 hour (you can change 1 to any number)
       // $row_ = date("Y-m-d H:i:s", strtotime("$row_ - 1 hours"));
      
        // Uncomment to set timezone to + 4 hours (you can change 4 to any number)
        //$row_ = date("Y-m-d H:i:s", strtotime("$row_ + 4 hours"));
      
        echo '<tr> 
                <td>' . $row_Department . '</td>
                <td>' . $row_Date . '</td> 
                <td>' . $row_Time . '</td> 
                <td>' . $row_No_of_beds_occ . '</td> 
                <td>' . $row_No_of_beds_vac . '</td>
              </tr>';
    }
    $result->free();
}

$conn->close();
?> 
</table>

</body>
</html>

	</body>
</html>