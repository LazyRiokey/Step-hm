const myForm = document.forms[0];
const loginElem = myForm.elements.login;
const passwordElem = myForm.elements.pass;

myForm.addEventListener('submit', function(event) {
    event.preventDefault();

    if (loginElem.value.includes('!') ||
        loginElem.value.includes('@') ||
        loginElem.value.includes(' ') ||
        loginElem.value.length < 4) {
        alert('Login must not contain characters: "!", "@" or "space" and less than 4 symbols');
    }
    else if (passwordElem.value.length > 8 || passwordElem.value.length < 4) {
        alert('The password must be no longer than eight and less than four characters.')
    }
    else { event.target.submit(); }
});
