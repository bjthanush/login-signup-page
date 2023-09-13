// JavaScript code for user registration
function registerUser() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var role = document.getElementById('role').value;

    // Simulate saving user data to a database
    var user = {
      name: name,
      email: email,
      password: password,
      role: role
    };

    // Simulate the matching algorithm and redirect to the matching page
    if (role === 'consultant') {
      // Redirect to the consultant matching page
      window.location.href = 'Buissness.html';
    } else {
      // Redirect to the business matching page
      window.location.href = 'IT-consultants.html';
    }
  }