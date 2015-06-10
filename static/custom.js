function changeSong() {
  current.pause();
  current.src = document.getElementById("song").value;
  current.load();
  current.play();
}

// Start a song right away.
document.addEventListener('DOMContentLoaded', function(){
  current = new Audio(document.getElementById("song").value);
  current.play();
}, false);
