const form = document.forms['form2'];
const emailInput = form['name'];
const passwordInput = form['password'];
const passwordDiv = document.querySelector('.buo');
const submitBtn = form['next'];

const emailError = document.createElement('div');
emailError.style.color = 'red';
emailError.style.fontSize = '0.9em';
emailError.style.marginTop = '5px';
const passwordError = document.createElement('div');
passwordError.style.color = 'red';
passwordError.style.fontSize = '0.9em';
passwordError.style.marginTop = '5px';
emailInput.parentElement.appendChild(emailError);
passwordInput.parentElement.appendChild(passwordError);
passwordDiv.style.display = 'none';
emailInput.addEventListener('blur', function () {
    const email = emailInput.value.trim();
    const emailPattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = 'Please enter a valid email address';
        passwordDiv.style.display = 'none';
    } else {
        emailError.textContent = '';
        passwordDiv.style.display = 'block';
    }
});
form.addEventListener('submit', function (e) {
    let valid = true;
    const email = emailInput.value.trim();
    const emailPattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = 'Invalid email format';
        valid = false;
    } else {
        emailError.textContent = '';
    }
    if (passwordInput.value.trim() === '') {
        passwordError.textContent = 'Password is required';
        valid = false; } 
else {
        passwordError.textContent = '';       }

    if (!valid) {
        e.preventDefault(); // stop form from submitting
    }
});

