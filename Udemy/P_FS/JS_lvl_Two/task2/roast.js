// start the programm, creating empty array
var roast = [];

// function add

function add(){
  var name = prompt("Enter name What name would you like to add?")
  var roast.push(name)
}

// funcion remove
function remove(){
  var nameToRemove = prompt("What name would you like to remove?")
  var index = roast.indexOf(nameToRemove)
  var removed = roast.splice(index, 1);
}

// function dispaly
function display(){
  console.log(roast);
}

// To make stop for infinitr loop
var checker = true;

// Main logic of progtam

  var work = prompt("Would you like to start the roster web app? y/n")
  if (work == "y" || work == "yes") {
    while (checker) {
    var input = prompt ("Please select an action: add, remove, display, or quit.");
    if (input == "add" || input == "Add"){
      add();
    } else if (input == "remove" || input == "Remove") {
      remove();
    }else if (input == "display" || input == "Display") {
      display();
    }else if (input == "quit" || input == "Quit") {
      alert("Thanks for using the Web App! Please refresh the page to start over.");
      checker = false;
    }else {
      alert("Unknown command!")
    }
    }

  } else {
    alert("Thanks for using the Web App! Please refresh the page to start over.");
  }
