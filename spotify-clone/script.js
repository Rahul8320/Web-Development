console.log("Welcome to spotify!!");

// Initialize variables
let songIndex = 0;
let audioElement  = new Audio("songs/1.mp3");
let masterPlay = document.getElementById('masterPlay');
let prograssBar = document.getElementById('prograssBar');
let gif = document.getElementById("gif");

let songs = [
    {songName:"1 - Let me love you", filePath: "songs/1.mp3", coverPath:"covers/1.jpg"},
    {songName:"2 - Let me love you", filePath: "songs/2.mp3", coverPath:"covers/2.jpg"},
    {songName:"3 - Let me love you", filePath: "songs/3.mp3", coverPath:"covers/3.jpg"},
    {songName:"4 - Let me love you", filePath: "songs/4.mp3", coverPath:"covers/4.jpg"},
    {songName:"5 - Let me love you", filePath: "songs/5.mp3", coverPath:"covers/5.jpg"},
    {songName:"6 - Let me love you", filePath: "songs/6.mp3", coverPath:"covers/6.jpg"},
    {songName:"7 - Let me love you", filePath: "songs/7.mp3", coverPath:"covers/7.jpg"},
    {songName:"8 - Let me love you", filePath: "songs/8.mp3", coverPath:"covers/8.jpg"},
    {songName:"9 - Let me love you", filePath: "songs/9.mp3", coverPath:"covers/9.jpg"},
    {songName:"10 - Let me love you", filePath: "songs/10.mp3", coverPath:"covers/10.jpg"},
]

// audioElement.play();

// handle play pause events
masterPlay.addEventListener('click', ()=>{
    if(audioElement.paused || audioElement.currentTime <= 0){
        audioElement.play();
        masterPlay.src = "pause.png";
        gif.style.opacity = 1;
    }
    else{
        audioElement.pause();
        masterPlay.src = "play.png";
        gif.style.opacity = 0;
    }
})

// listen to events
audioElement.addEventListener('timeupdate', ()=> {
    console.log('timeupdate');
    // update seekbar
    prograss = parseInt((audioElement.currentTime/audioElement.duration)*100);
    console.log(prograss);
    prograssBar.value = prograss;
})

prograssBar.addEventListener('change', ()=>{
    audioElement.currentTime = prograssBar.value * audioElement.duration/100;
})