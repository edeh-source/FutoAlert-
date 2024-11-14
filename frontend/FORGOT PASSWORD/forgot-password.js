// Handle form submission
function handleFormSubmission(event) {
    event.preventDefault();
  
    // Get email input and error elements
    const email = document.getElementById("email");
    const emailError = document.getElementById("emailError");
  
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email.value.trim())) {
      emailError.textContent = "Please enter a valid email address";
      emailError.style.display = "block";
    } else {
      emailError.style.display = "none";
      alert("If this email is associated with an account, a reset link will be sent.");
      // Here you can add form submission logic to send the email
    }
  }
  