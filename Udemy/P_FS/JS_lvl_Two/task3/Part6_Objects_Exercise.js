// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee1 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLenght: function(){
    console.log(this.name.length);
 }
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee2 = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

var alertfunc = function() {
  for (key in employee2) {
    alert(key + " is " + employee2[key])
  }
}

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee3 = {
  name: "John Smith",
  splited: function(){
  var nameList = this.name.split(" ");
  surname = nameList[1];
  console.log(surname)
  },
  job: "Programmer",
  age: 31
}

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
