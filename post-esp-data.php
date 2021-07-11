<?php
$servername = "localhost";
$username = "root";
$password = "medbeds@123";
$dbname = "medbeds";

/*$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);*/

$api_key_value = "tPmAT5Ab3j7F9";

$api_key= $Department = $Date = $Time = $No_of_beds_occ = $No_of_beds_vac = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $api_key = test_input($_POST["api_key"]);
    if($api_key == $api_key_value) {
        $Department = test_input($_POST["Department"]);
        $Date = test_input($_POST["Date"]);
        $Time = test_input($_POST["Time"]);
        $No_of_beds_occ = test_input($_POST["No_of_beds_occ"]);
        $No_of_beds_vac = test_input($_POST["No_of_beds_vac"]);
        
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 
        
        $sql = "INSERT INTO real_time_amri_data (Department, Date, Time, No_of_beds_occ, No_of_beds_vac)
        VALUES ('" . $Department . "', '" . $Date . "', '" . $Time . "', '" . $No_of_beds_occ . "', '" . $No_of_beds_vac . "')";
        
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    
        $conn->close();
    }
    else {
        echo "Wrong API Key provided.";
    }

}
else {
    echo "No data posted with HTTP POST.";
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}