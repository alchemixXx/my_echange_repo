// var playerOneName = prompt("Player One, enter your name. Your colour will be Blue")

// Create a global variable which will count clicks
var clicks = 0;

// Create global variables which will contain names
var playerOneName;
var playerTwoName;

// Create global variables whick will grab main instruction and circles
var changeCircle = $(".circle");


  // Create an array with 0. Need to define the winner

  var grid = [[0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0]]

// Create function wich will ask about player names
function startGame(){
  playerOneName = prompt("Player One, enter your name. Your colour will be Blue");
  playerTwoName = prompt("Player Two, enter your name. Your colour will be Red");
  clicks++;
}

// Create a function that will check how many circles in row current player has
function checkRow(a, b, c){
    var inRow = 1;
    // Checking to the right side of row
    for (var i = 1; i <= 4; i++) {
        if ((b + i) > 7) {
          console.log("end of the row");
          break;
        }else if (grid[a][b+i] == c) {
          // console.log("incrementation of inRow");
          inRow++
          if (inRow === 4) {
            console.log("Player reached 4 in line, End of game");
            theEnd();
            break;
          }else {
          console.log(inRow);
          }
        }else if (grid[a][b+i] != c) {
          break;
      }
  }
  // checking to the left side of row
  for (var i = 1; i <= 4; i++) {
      if (b-i < 0) {
        console.log("end of the row");
        break;
      }else if (grid[a][b-i] == c) {
        // console.log("incrementation of inRow");
        inRow++
        if (inRow === 4) {
          console.log("Player reached 4 in line, End of game");
          theEnd();
          break;
        }else {
        console.log(inRow);
        }
      }else if (grid[a][b-i] != c) {
        break;
    }
}
}

// Create a function that will check how many circles in column current player has
function checkColumn(a, b, c){
    var inColumn = 1;
    // Checking to the down side of table
    for (var i = 1; i <= 4; i++) {
      if ((a + i) >= 8) {
        console.log("end of the column");
        break;
    }else if (grid[a+i][b] == c) {
          console.log("incrementation of inCol");
          inColumn++
          if (inColumn === 4) {
            console.log("Player reached 4 in line, End of game");
            theEnd();
            break;
          }else {
          console.log(inColumn);
          }
    }else if (grid[a+i][b] != c) {
          break;
      }
    }

    // Checking to the up side of table
  for (var i = 1; i <= 4; i++) {
    if ((a - i) < 0) {
      console.log("end of the column");
      break;
  }else if (grid[a-i][b] == c) {
        console.log("incrementation of inCol");
        inColumn++
        if (inColumn === 4) {
          console.log("Player reached 4 in line, End of game");
          theEnd();
          break;
        }else {
        console.log(inColumn);
        }
      }else if (grid[a-i][b] != c) {
        break;
    }
}
}

// Create a function that will check how many circles in first diagonal current player has
function checkDiagonalLeftToRight(a, b, c){
    var inColumn = 1;
    // Checking to the down side of table
    for (var i = 1; i <= 4; i++) {
      if ((a - i) < 0 || (b + i) >= 8) {
        console.log("end of the column");
        break;
    }else if (grid[a-i][b+i] == c) {
          console.log("incrementation of inCol");
          inColumn++
          if (inColumn === 4) {
            console.log("Player reached 4 in line, End of game");
            theEnd();
            break;
          }else {
          console.log(inColumn);
          }
    }else if (grid[a-i][b+i] != c) {
          break;
      }
    }

    // Checking to the up side of table
  for (var i = 1; i <= 4; i++) {
    if ((a + i) >= 8 || (b - i) < 0) {
      console.log("end of the column");
      break;
  }else if (grid[a + i][b - i] == c) {
        console.log("incrementation of inCol");
        inColumn++
        if (inColumn === 4) {
          console.log("Player reached 4 in line, End of game");
          theEnd();
          break;
        }else {
        console.log(inColumn);
        }
      }else if (grid[a + i][b - i] != c) {
        break;
    }
}
}

// Create a function that will check how many circles in first diagonal current player has
function checkDiagonalRightToLeft(a, b, c){
    var inColumn = 1;
    // Checking to the down side of table
    for (var i = 1; i <= 4; i++) {
      if ((a + i) >= 8 || (b + i) >= 8) {
        console.log("end of the column");
        break;
    }else if (grid[a+i][b+i] == c) {
          console.log("incrementation of inCol");
          inColumn++
          if (inColumn === 4) {
            console.log("Player reached 4 in line, End of game");
            theEnd();
            break;
          }else {
          console.log(inColumn);
          }
    }else if (grid[a+i][b+i] != c) {
          break;
      }
    }

    // Checking to the up side of table
  for (var i = 1; i <= 4; i++) {
    if ((a - i) < 0 || (b - i) < 0) {
      console.log("end of the column");
      break;
  }else if (grid[a-i][b - i] == c) {
        console.log("incrementation of inCol");
        inColumn++
        if (inColumn === 4) {
          console.log("Player reached 4 in line, End of game");
          theEnd();
          break;
        }else {
        console.log(inColumn);
        }
      }else if (grid[a-i][b - i] != c) {
        break;
    }
}
}


// Create a function witch will animate the end of the game
function theEnd(){
    $(".container").fadeOut(3500);
    if (clicks % 2 == 0) {
      $(".congrads").val("display", "block").text(playerOneName + " has won. Please refresh the page to start the game again").fadeIn(5500);
    }else {
      $(".congrads").val("display", "block").text(playerTwoName + " has won. Please refresh the page to start the game again")
    }
  }


// Create function, wich will change name and colour of circles and count number of clicks. Main function
function changeInstruction(){
var changeInstruction = $("#instruction")
  if (clicks === 0) {
    startGame();
    changeInstruction.text(playerOneName + ": it's your turn, please pick a column to drop your Blue chip");
  }
  else if (clicks % 2 === 0){
    if ($(this).attr('class') == 'circle getRed' || $(this).attr('class') == 'circle getBlue') {
      alert("This point is already chosen!")
    } else {
      // changeCircle.addClass("getBlue");
      $(this).addClass("getRed");
      $(this).disabled = true
      clicks++;
      changeInstruction.text(playerOneName + ": it's your turn, please pick a column to drop your Blue chip");

      // getting the id and changing the grid
      var x = $(this).attr("id");
      grid[x[0]][x[2]] = 1;
      console.log("Value in grid is ", grid[x[0]][x[2]]);

      // check the results
      checkRow(Number(x[0]), Number(x[2]), grid[x[0]][x[2]]);
      checkColumn(Number(x[0]), Number(x[2]), grid[x[0]][x[2]]);
      checkDiagonalLeftToRight(Number(x[0]), Number(x[2]), grid[x[0]][x[2]]);
      checkDiagonalRightToLeft(Number(x[0]), Number(x[2]), grid[x[0]][x[2]]);
  }
}else if (clicks % 2 !== 0) {
  if ($(this).attr('class') == 'circle getRed' || $(this).attr('class') == 'circle getBlue') {
    alert("This point is already chosen!")
  } else {
    $(this).addClass("getBlue");
    clicks++;
    changeInstruction.text(playerTwoName + ": it's your turn, please pick a column to drop your Red chip");

    // getting the id and changing the grid
    var y = $(this).attr("id");
    grid[y[0]][y[2]] = 2;

    // check the results
    checkRow(Number(y[0]), Number(y[2]), grid[y[0]][y[2]]);
    checkColumn(Number(y[0]), Number(y[2]), grid[y[0]][y[2]]);
    checkDiagonalLeftToRight(Number(y[0]), Number(y[2]), grid[y[0]][y[2]]);
    checkDiagonalRightToLeft(Number(y[0]), Number(y[2]), grid[y[0]][y[2]]);

  }
  console.log(clicks);
}
}



// Main body of program :)
$(".circle").click(changeInstruction);
