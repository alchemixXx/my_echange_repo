function helloYou(name){
  // var name = prompt("Enter your name: ")
  console.log("Hello, " + name+"!")
}

// deafualt values
function helloName(name = "Pavel") {
    console.log("Hello, " + name+"!")
}
// Returning value from the function

function formal(name="Sam", title="Sir") {
console.log(title + " " + name);
return (title + " " + name)
}
