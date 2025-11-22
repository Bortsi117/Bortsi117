<?php
session_start();
include("connect.php");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
</head>
<body>
    <div style="text-align: center; padding:15%;">
    <p style="font-size:50px; font-weight:bold;">
    Hello <?php
    if(isset($_SESSION['email'])){
        $email=$_SESSION['email'];
        $query=mysqli_query($conn,"SELECT firstName, lastName FROM users WHERE email='$email'");
        while($row=mysqli_fetch_array($query)){
            echo $row['firstName'].' '. $row['lastName'];
        }
    }
    else{
        echo "Guest";
    }
    ?>
</p>
    <a href="logout.php" style="font-size:20px; text-decoration:none; color:white; background-color:blue; padding:10px 20px; border-radius:5px;">Logout</a> 

    </div>
    
</body>
</html>