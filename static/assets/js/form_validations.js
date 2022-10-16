// # TODO: Form Validation

const form = document.getElementById('form');
const username = document.getElementById('id_username');
const email = document.getElementById('id_email');
const password1 = document.getElementById('id_password1');
const password2 = document.getElementById('id_password2');
const terms_and_condition = document.getElementById('terms_and_condition');

const pattern = /^[^ ]+@[^ ]+\.[a-z](2,3)$/;

function getCookie (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function checkInputs(event) {
    console.log('Function Called.');
    var returnVal = true;

    // Get the Values From the inputs
    const username_value = username.value.trim();
    const email_value = email.value.trim();
    const password1_value = password1.value.trim();
    const password2_value = password2.value.trim();

    if (username_value === '') {
        // Show error 
        // add error class
        setErrorFor(username, 'Username cannot be blank.');
        returnVal = false;
    } else {
        // add success class
        setSuccessFor(username);
    }

    if (email_value === '') {
        email.innerText = 'Please fill email';
        setErrorFor(email, 'Email cannot be blank');
        returnVal = false;
    } else if (!isEmail(email_value)) {
        setErrorFor(email, 'Email is not Valid.');
        returnVal = false;
    } else {
        setSuccessFor(email);
    }

    if (password1_value === '') {
        setErrorFor(password1, 'Enter password');
        returnVal = false;
    } else if (password1_value.length < 8) {
        setErrorFor(password1, 'Minimum 8 character required.');
        returnVal = false;
    } else {
        setSuccessFor(password1);
    }

    if (password2_value === '') {
        setErrorFor(password2, 'Enter password');
        returnVal = false;
    } else if (password2_value.length < 8) {
        setErrorFor(password2, 'Minimum 8 character required.');
        returnVal = false;
    } else {
        setSuccessFor(password2);
    }

    if (password2_value === '') {
        setErrorFor(password2, 'Enter password');
        returnVal = false;
    } else if (password2_value != password1_value) {
        setErrorFor(password2, 'Passwords does not match.');
        returnVal = false;
    } else {
        setSuccessFor(password2);
        setSuccessFor(password1);
    }

    if (!form.terms.checked) {
        alert("Please indicate that you accept the Terms and Conditions");
        form.terms.focus();
        return false;
    }

    return returnVal;

}

function setErrorFor(input, message) {
    const formControl = input.parentElement; // .form-control
    console.log(formControl)
    const small = formControl.querySelector('small');

    // add error message 
    console.log(message);
    small.innerText = message;
    formControl.className = 'form-controls error';
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-controls success';
}

// Email Checking 
function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function isAlphaNumeric(input) {
    return /^[A-Za-z]+$/.test(input);
}