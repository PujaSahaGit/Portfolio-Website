<?php
$insert = false;
if(isset($_POST['name'])){
    // Set connection variables
    
    $username = "";
    $password = "";

    // Create a database connection
    $con = mysqli_connect('localhost', 'root', '' ,'register_table');

    // Check for connection success
    if(!$con){
        die("connection to this database failed due to" . mysqli_connect_error());
    }
    // echo "Success connecting to the db";

    // Collect post variables
    $name = $_POST['name'];
    $gender = $_POST['gender'];
    $age = $_POST['age'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    // $other = $_POST['other'];
    $other = $_POST['other'];
    // $sql = "INSERT INTO `trip`.`trip` (`name`, `age`, `gender`, `email`, `phone`, `other`, `dt`) VALUES ('$name', '$age', '$gender', '$email', '$phone', '$other', current_timestamp());";
    // echo $sql;
    $sql = "INSERT INTO `trip`.`trip` (`Name`, `age`, `gender`, `email`, `phone`, `other`, `date`) VALUES ('$Name', '$age', '$gender', '$email', '$phone', '$other', current_timestamp());";

    // Execute the query
    if($con->query($sql) == true){
        // echo "Successfully inserted";

        // Flag for successful insertion
        $insert = true;
    }
    else{
        echo "ERROR: $sql <br> $con->error";
    }

    //Close the database connection
    $con->close();
}

    if($insert == true){
        echo "<p class='submitMsg'>Thanks for submitting your form. We are happy to see you joining us for the US trip</p>";
    }
?>
