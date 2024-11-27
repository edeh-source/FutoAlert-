let form = document.getElementById("signup-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();

  let username = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;
  let confirmPassword = document.getElementById("confirmPassword").value;

  if (password.length < 8) {
    alert("Password must be at least 8 characters long.");
    return;
  }
  if (confirmPassword !== password) {
    alert("Password mismatch");
    return;
  }

  let user = {
    name: username,
    email: email,
    password: password,
  };

  fetch("", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("Submitted successfully", data);
    })
    .catch((error) => {
      console.log("error occurred", error);
    });
});
