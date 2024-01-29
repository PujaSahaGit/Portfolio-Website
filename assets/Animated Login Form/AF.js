function validate() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    if (email == "" || password == "") {
        alert("Please enter both email and password");
    } else if (email == "admin" && password == "password") {
        alert("Login successful!");
        // redirect to another page or perform other actions
    } else {
        alert("Invalid email or password");
    }
}
function validatee() {
    var email = document.getElementById("email").value;
    if (email == "") {
        alert("Please enter email")
    }
    else if (email == "admin") {
        alert("Resetpassword Link Sent!");
        // redirect to another page or perform other actions
    } else {
        alert("Invalid email");
    }
}
function validateee() {
    var name=document.getElementById("name").value;
    var username=document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email == "" || password == "" || name == "" || username == "") {
        alert("Please enter fields");
    } 
    // else if (email == "admin" && password == "password" && name == "name" && username == "username")
    // {
    //     alert("Login successful!");
    //     // redirect to another page or perform other actions
    // } 
    else {
        // alert("Invalid user");
        alert("Login successful!");
    }
}

