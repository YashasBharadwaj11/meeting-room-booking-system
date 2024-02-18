document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    const errorMessage = document.getElementById('error-message'); // Assuming an element with this ID

    // Handle the form submission
    registerForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent default form submission

        // Gather the form data
        const formData = {
            username: document.getElementById('username').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value,
            name: document.getElementById('name').value,
        };

        // Send a POST request to the registration endpoint
        fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
            console.log("Respose:",response);
            // Check if the response status is not OK (200)
            if (!response.ok) {
                // Parse the response as JSON and throw an error to be caught later
                return response.json().then(data => {
                    throw new Error(data.message || "An error occurred during registration.");
                });
            }
            return response.json();
        })
        .then(data => {
            // Registration successful
            console.log('Registration successful', data);
            // Redirect to the login page or display a success message
            window.location.href = 'login.html';
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