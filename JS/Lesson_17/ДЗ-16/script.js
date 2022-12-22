const regForm = document.forms[0];

const loginElem = regForm.elements.login;
const passwordElem = regForm.elements.pass;
const emailElem = regForm.elements.email;
const phoneElem = regForm.elements.phone;

const regexpLogin = /^[a-z]\w+$/i;
const regexpPass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/; 
const regexpPhone =/^\+\d \(\w{3}\) \w{3}(-\w{2}){2}$/;
const regexpEmail = /^\w+@((\w+\.)+.)\w+/;

loginElem.addEventListener('input', function() {
    if (loginElem.value == '') {
        loginElem.nextElementSibling.src = "";
        loginElem.nextElementSibling.alt = "";
        loginElem.setCustomValidity('');
    }
    else if (!regexpLogin.test(loginElem.value)) {
        loginElem.nextElementSibling.src = "res/error.png";
        loginElem.nextElementSibling.alt = "error";
        loginElem.setCustomValidity('There is an error in the login line.');
    } else {
        loginElem.nextElementSibling.src = "res/check.png";
        loginElem.nextElementSibling.alt = "check";
        loginElem.setCustomValidity('');
    }
});

passwordElem.addEventListener('input', function() {
    if (passwordElem.value == '') {
        passwordElem.nextElementSibling.src = "";
        passwordElem.nextElementSibling.alt = "";
        passwordElem.setCustomValidity('');
    }
    else if (!regexpPass.test(passwordElem.value)) {
        passwordElem.nextElementSibling.src = "res/error.png";
        passwordElem.nextElementSibling.alt = "error";
        passwordElem.setCustomValidity('There is an error in the password line.');
    }
     else {
        passwordElem.nextElementSibling.src = "res/check.png";
        passwordElem.nextElementSibling.alt = "check";
        passwordElem.setCustomValidity('');
    }
});

emailElem.addEventListener('input', function() {
    if (emailElem.value == '') {
        emailElem.nextElementSibling.src = "";
        emailElem.nextElementSibling.alt = "";
        emailElem.setCustomValidity('');
    }
    else if (!regexpEmail.test(emailElem.value)) {
        emailElem.nextElementSibling.src = "res/error.png";
        emailElem.nextElementSibling.alt = "error";
        emailElem.setCustomValidity('There is an error in the email line.');
    } else {
        emailElem.nextElementSibling.src = "res/check.png";
        emailElem.nextElementSibling.alt = "check";
        emailElem.setCustomValidity('');
    }
});

phoneElem.addEventListener('input', function() {
    if (phoneElem.value == '') {
        phoneElem.nextElementSibling.src = "";
        phoneElem.nextElementSibling.alt = "";
        phoneElem.setCustomValidity('');
    }
    else if (!regexpPhone.test(phoneElem.value)) {
        phoneElem.nextElementSibling.src = "res/error.png";
        phoneElem.nextElementSibling.alt = "error";
        phoneElem.setCustomValidity('There is an error in the phone line.');
    } else {
        phoneElem.nextElementSibling.src = "res/check.png";
        phoneElem.nextElementSibling.alt = "check";
        phoneElem.setCustomValidity('');
    }
});
