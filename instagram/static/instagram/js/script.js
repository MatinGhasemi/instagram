let heart = document.getElementById('heart')
let heart_red = document.getElementById('heart-red')


heart.style.zIndex = 1
heart_red.style.zIndex = -1

heart.onclick = function(){
    heart_red.style.zIndex = 1
    heart.style.zIndex = -1
}
heart_red.onclick = function(){
    heart_red.style.zIndex = -1
    heart.style.zIndex = 1
}