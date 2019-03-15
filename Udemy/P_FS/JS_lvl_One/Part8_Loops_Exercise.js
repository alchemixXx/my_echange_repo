/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var counter = 0;
while (counter < 5){
  console.log("hello");
  counter++
}


// For Loop
for (cnter2 = 0; cnter2 < 5; cnter2++){
  console.log("hello");
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var number1 = 1;
while (number1 <= 25){
  if (number1%2 !== 0){
    console.log(number1);
  }
  number1++;
}

// METHOD TWO
// For Loop
for (number2=1; number2<=25; number2++){
  if(number2%2 !== 0){
    console.log(number2);
  }
}
