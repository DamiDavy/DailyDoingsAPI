document.addEventListener('DOMContentLoaded', function() {

  console.log('add-todo')

  const title = document.querySelector('#title')
  const date = document.querySelector('#date')
  const addTodoForm = document.querySelector('#add-todo-form')

  addTodoForm.onsubmit = (e) => {

    console.log('adding')

    fetch('todo', {
      method: 'POST',
      body: JSON.stringify({
        title: title.value,
        date: date.value,
      })
    })
    .then(response => response.json())
    .then(result => console.log(result))
    e.preventDefault()
  }

  const id = document.querySelector('#todo-id')
  const deleteTodoForm = document.querySelector('#delete-todo-form')

  deleteTodoForm.onsubmit = (e) => {

    console.log('deleting')

    fetch('todo', {
      method: 'PUT',
      body: JSON.stringify({
        delete: id.value,
      })
    })
    .then(response => response.json())
    .then(result => console.log(result))
    e.preventDefault()
  }

})