document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message'); // Assuming an element with this ID

    // Handle the form submission
    loginForm.addEventListener('loginButton', function (e) {
        e.preventDefault(); // Prevent default form submission

        // Gather the form data
        const formData = {
            username: document.getElementById('username').value,
            password: document.getElementById('password').value,
        };

        // Send a POST request to the login endpoint
        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
            console.log("Response:", response);
            // Check if the response status is not OK (200)
            if (!response.ok) {
                // Parse the response as JSON and throw an error to be caught later
                return response.json().then(data => {
                    throw new Error(data.error || "An error occurred during login.");
                });
            }
            console.log("Login successful")
            return response.json();
        })
        .then(data => {
            // Login successful
            console.log('Login successful', data);
            // Redirect to the dashboard or display a success message
            window.location.href = 'dashboard.html';
        })
        .catch(error => {
            // Log the error to the console
            console.error('Error:', error);
            // Update the UI to show the error message
            if (errorMessage) {
                errorMessage.textContent = error.message;
                errorMessage.style.display = 'block'; // Make the error message visible
            }
        });
    });
});
