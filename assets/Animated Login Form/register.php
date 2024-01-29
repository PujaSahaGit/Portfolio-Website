<?php
$insert = false;
if(isset($_POST['name'])){
    // Set connection variables
    $server = "localhost";
    $username = "root";
    $password = "";

    // Create a database connection
    $con = mysqli_connect($server, $username, $password);

    // Check for connection success
    if(!$con){
        die("connection to this database failed due to" . mysqli_connect_error());
    }
    echo "Success connecting to the db";
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="AF.css">
    <title>Registration</title>
</head>

<body>

    <form action="" class="rh">
        <h1 style="text-decoration: underline">Register Here</h1>
        <div class="registerbox">
            <div class="">
                <input type="name" id="name" required>
                <label for="">Name</label>
            </div>
            <br>
            <div class="">
                <input type="username" id="username" required>
                <label for="">Username</label>
            </div>
            <br>
            <div class="">
                <input type="email" id="email" required>
                <label for="">Email</label>
            </div>
            <br>
            <div class="">
                <input type="password" id="password" required>
                <label for="">Password</label>
            </div>
        </div>
        <button class="btn">Register</button>
        <!-- onclick="validateee()" -->
    </form>
    <!-- <script src="AF.js"></script> -->

</body>

</html>

<!-- INSERT INTO `sl.no` (`SL.No`, `Name`, `Username`, `Email`, `Password`, `Date`) VALUES ('1', 'Puja Saha', 'pujasaha',
'this@tis.com', '880@', current_timestamp()); -->