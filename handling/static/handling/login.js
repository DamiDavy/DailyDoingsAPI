document.addEventListener('DOMContentLoaded', function() {

  const login = document.querySelector('#login')
  const password = document.querySelector('#password')
  const loginForm = document.querySelector('#login-form')

  const buttonLogout = document.querySelector('#button-logout')

  const buttonChecking = document.querySelector('#button-checking')

  loginForm.onsubmit = (e) => {

    fetch('login', {
      method: 'POST',
      body: JSON.stringify({
        login: login.value,
        password: password.value,
      })
    })
    .then(response => response.json())
    .then(result => console.log(result))
    e.preventDefault()
  }

  if (buttonLogout) {
    buttonLogout.onclick = () => {

      console.log('log out?')

      fetch('logout')
      .then(response => response.json())
      .then(result => console.log(result))
    }
  }

  buttonChecking.onclick = () => {

  console.log('log in?')

  fetch('todos', {
      method: 'POST',
      body: JSON.stringify({
        login: login.value,
      })
    })
  .then(response => response.json())
  .then(result => console.log(result))
  }
  
})