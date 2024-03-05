<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login Page</title>
<style>
    body {
        font-family: Arial, sans-serif;
    }
    .container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    input[type="text"], input[type="password"] {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    button {
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
    }
    button:hover {
        background-color: #45a049;
    }
</style>
</head>
<body>

<div class="container" id="loginContainer">
    <h2>Login</h2>
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" id="username" required>

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" id="password" required>

    <button onclick="login()">Login</button>
</div>

<div class="container" id="logoutContainer" style="display:none;">
    <h2>Logout</h2>
    <button onclick="logout()">Logout</button>
</div>

<script>
    function login() {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        // Here you can perform authentication, for simplicity, let's check if username and password match "admin"
        if (username === 'admin' && password === 'admin') {
            // Hide login container and show logout container
            document.getElementById('loginContainer').style.display = 'none';
            document.getElementById('logoutContainer').style.display = 'block';
            alert('Login successful!');
        } else {
            alert('Invalid username or password!');
        }
    }

    function logout() {
        // Hide logout container and show login container
        document.getElementById('logoutContainer').style.display = 'none';
        document.getElementById('loginContainer').style.display = 'block';
        // Optionally you can clear the input fields here
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        alert('Logged out successfully!');
    }
</script>

</body>
</html>

