
// Pick up all elevemnt with class "selected" - all cells
var byClass = document.querySelectorAll(".selected")

// Pick up restart button
var restButtn = document.querySelector("#restart")

// Function to change cells
function myfunc(){
  var cont = this.textContent;
  if (cont === "") {
    this.textContent = "X";
      this.style.color = "red";
      this.style.fontSize = "45px";
  } else if (cont === "X") {
    this.textContent = "O";
    this.style.color = "blue";
    this.style.fontSize = "45px";
  } else if (cont === "O") {
    this.textContent = ""
  }
    // console.log(cont);
  return cont
}

// Function to restart all field
function restart(){
  alert("Game will be restarted right now")
for (var i = 0; i < byClass.length; i++){
  byClass[i].textContent = "";
}
}

// Add event to all cells of Game via class
for (var i = 0; i < byClass.length; i++) {
  byClass[i].addEventListener("click", myfunc);
}


// Add function to restart button
restButtn.addEventListener("click", restart);


// Add event to all cells of Game via personal ID
// one.addEventListener("click", myfunc);
// two.addEventListener("click", myfunc);
// three.addEventListener("click", myfunc);
// four.addEventListener("click", myfunc);
// five.addEventListener("click", myfunc);
// six.addEventListener("click", myfunc);
// seven.addEventListener("click", myfunc);
// eight.addEventListener("click", myfunc);
// nine.addEventListener("click", myfunc);
