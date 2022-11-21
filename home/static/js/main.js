
// let body =document.boby
// let toggle = document.querySelector('.toggle')
// let icon = document.querySelector('i')
// // let iconB = document.querySelector('.dark')

// toggle.onclick = () =>{
//     body.classlist.toggle('dark')
//     if(body.classlist.toggle('dark')){
//         icon.classlist.replace('fa-moon', 'fa-sun');
//     }else{
//         icon.classlist.replace('fa-sun', 'fa-moon')
//     }
// }


// let body = document.body
// let toggle = document.querySelector('.toggle')
// let icon = document.querySelector(".fa-moon")

// function checkIcon(){
//     if(body.classlist.contains('dark')){
//         icon.classList.add('fa-moon')
//         icon.classList.remove('fa-sun')
//     }else{
//         icon.classlist.add('fa-sun')
//         icon.classlist.remove('fa-moon')
//     }
// }

// checkIcon()

// toggle.onclick =() =>{
//     body.classlist.toggle("dark")
//     setTimeout(()=>{
//         checkIcon()
//     },100)
// }

let change = document.querySelector('.grab')
let cyber = document.querySelector('.grab')

change.addEventListener('click',() =>{
    change.classList.toggle('shower')
    if(cyber.type === 'password'){
        cyber.type = 'text';
    }else{
        cyber.type = 'password';
    }
})