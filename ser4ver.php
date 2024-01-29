<?php

$name = $_POST["name"];
$mobile=$_POST["mobile"];
$email    = $_POST["email"];

$message=$_POST["message"];
$errors = array(); 

// connect to the database
$connection = mysqli_connect("localhost", "root", "", "contactme") or die("connection failed");
$sql = "INSERT INTO userdata(name,mobile,email,message) VALUES('{$name}','{$mobile}','{$email}','{$message}')";
$result = mysqli_query($connection, $sql) or die("query failed");
// header("location:index2.php");
mysqli_close($connection);
?>
