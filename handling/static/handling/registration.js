document.addEventListener('DOMContentLoaded', function() {

  console.log('reg')

  const login = document.querySelector('#login')
  const email = document.querySelector('#email')
  const password = document.querySelector('#password')
  const confirmation = document.querySelector('#confirmation')
  const regForm = document.querySelector('#registration-form')

  regForm.onsubmit = (e) => {

    console.log('submitted')

    fetch('registration', {
      method: 'POST',
      body: JSON.stringify({
        login: login.value,
        email: email.value,
        password: password.value,
        confirmation: confirmation.value
      })
    })
    .then(response => response.json())
    .then(result => console.log(result))
    e.preventDefault()
  }
})