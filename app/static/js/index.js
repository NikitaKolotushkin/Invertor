function scrollTo(element) {
    window.scroll({
        left: 0, 
        top: element.offsetTop, 
        behavior: 'smooth'
    })
}
    
var button = document.querySelector('.registration_btn');
var footer = document.querySelector('#register');

button.addEventListener('click', () => {
    scrollTo(footer);
})


// Плавное удаление flash уведомления
setTimeout(function(){
    document.getElementById('flash').style.opacity = 0;
}, 2000);