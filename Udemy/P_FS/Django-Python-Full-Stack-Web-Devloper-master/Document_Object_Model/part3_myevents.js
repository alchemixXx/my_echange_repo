var one = document.querySelector("#one")

var two = document.querySelector("#two")

var three = document.querySelector("#three")



one.addEventListener("mouseover", function(){
  one.textContent = "Mouse is over me!!!"
  one.style.color = "blue";
  one.style.fontSize = "42px";
})
one.addEventListener("mouseout", function(){
  one.textContent = "Hover Over Me!"
  one.style.color = "black";
  one.style.fontSize = "32px";
})


two.addEventListener("click", function(){
  two.textContent = "I'm Clicked!!!"
  two.style.color = "yellow";
  two.style.fontSize = "42px";
})
two.addEventListener("mouseout", function(){
  two.textContent = "Click Me!"
  two.style.color = "black";
  two.style.fontSize = "32px";
})


three.addEventListener("dblclick", function(){
  three.style.color = "red";
  three.style.fontSize = "42px";
})
three.addEventListener("mouseout", function(){
  three.style.color = "black";
  three.style.fontSize = "32px";
})
