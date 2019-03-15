var fname = prompt("What is your first name?");
var lname = prompt("What is your last name?");
var age = prompt("How old are you?");
var height = prompt("What is your height?");
var pet = prompt("What your pet's name?");


var last = pet.length;

// console.log(last);
// console.log(pet[last-1]);

if ((fname[0] == lname[0]) && (20 < age < 30) && (height >= 170) && (pet[last-1] === "y")){
  console.log("Welcome, Spy!");
}else {
  console.log("Nothing here...");
}
