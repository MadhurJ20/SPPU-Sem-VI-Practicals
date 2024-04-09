function validateForm() {
    var name = document.getElementById('name').value;
    var password = document.getElementById('password').value;
    var number = document.getElementById('number').value;
    var dob = document.getElementById('dob').value;
    var tnc = document.getElementById('tnc').checked;

    if(name === '') {
        alert('Name cannot be empty');
    }
    if (password.length < 8) {
        alert('Password cannot be less than 8 characters');
    }
    if (tnc === false) {
        alert('Please agree to the terms and conditions');
    }
}