var host = window.location.protocol+'//'+window.location.host;
var username ,email,password,phone

function get(){
    username = document.getElementById("username_id").value
    email = document.getElementById("email_id").value
    password = document.getElementById("password_id").value
    phone = document.getElementById("phone_id").value
}
console.log(username,email,password,phone)
fetch('http://127.0.0.1:8000/signup-post/',{
    method: 'POST',
    body: JSON.stringify({
        'username':username,
        'email':email,
        'password':password,
        'phone':phone
}),headers :new Headers({
    'Content-Type': 'application/json',
})
}).then(res => {

    return res.json()

  }).then(data => {
    console.log(data)
    
  })

   