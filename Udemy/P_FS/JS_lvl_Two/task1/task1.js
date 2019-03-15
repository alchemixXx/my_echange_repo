
// Exercise #1

function sleepIn(weekday, vacation) {
    if (weekday === true && vacation === false){
      return false;
    } else if (weekday === true && vacation === true) {
      return true;
    } else if (weekday === false && (vacation === true || vacation === false)) {
      return true;
  };
};

// Solution from Udemy:
// function sleepIn(weekday, vacation) {
//   return (!weekday || vacation)
// }

// Exercise #2

function monkeyTrouble(aSmile, bSmile) {
    if (aSmile === true && bSmile === true){
      return true;
    } else if (aSmile === false && bSmile === false) {
      return true;
    } else {
      return false;
    }
}

// Solution from Udemy:
// function monkeyTrouble(aSmile, bSmile) {
//   return (aSmile && bSmile) || (!aSmile && !bSmile)
// }

// Exercise #3
function stringTimes(str, n) {
  var result = str;
  var counter = 1;
  while (counter < n){
    result += str
    counter++
  }
  return result;
}

c
// almost the same that my solution!!!

// Exercise #4
function luckySum(a, b, c){
  var result = 0;
  if (a !== 13 && b !== 13 && c !== 13){
    result = a + b + c;
  } else if (c === 13) {
    result = a + b;
  } else if (b === 13) {
    result = a;
  } else if (a === 13) {
    result = 0;
  }
  return result;
}

// Solution from Udemy:
// almost the same that my solution!!!

// Exercise #5
function caught_speeding(speed, is_birthday){
  if (is_birthday === false){
    if (speed < 60){
      return 0;
    } else if (speed >= 61 && speed <= 80) {
      return 1;
    } else {
      return 2;
    }
  } else if (is_birthday === true) {
    if (speed <= 65){
      return 0;
    } else if (speed >= 66 && speed <= 85) {
      return 1;
    } else {
      return 2;
    }
  }
}

// Solution from Udemy:
function caught_speeding(speed, is_birthday){
if (is_birthday){
  speed -= 5;
}
if (speed <= 60) {
return 0;
} else if (60 < speed <= 80) {
return 1;
}else {
  return 2;
}
}

// Exercise bonus!
function makeBricks(small, big, goal){

  return ((small * 1 + big * 5) >= goal);
}

// Solution from Udemy:
function makeBricks(small, big, goal){
  return (goal%5 >= 0 && goal%5 - small <=0 && (small * 1 + big * 5) >= goal);
}
