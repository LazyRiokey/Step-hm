const button = document.getElementById("toggle");
const red = document.getElementById("box").children[0];
const yellow = document.getElementById("box").children[1];
const green = document.getElementById("box").children[2];

function switchLight() {
    if (count == 1) {
        if (yellow.classList.contains('yellow')) {
            yellow.classList.toggle('yellow');
        }
        red.classList.toggle('red');
    }
    else if (count == 2) {
        yellow.classList.toggle('yellow');
    }
    else if (count == 3) {
        red.classList.toggle('red');
        yellow.classList.toggle('yellow');
        green.classList.toggle('green');
    }
    else {
        green.classList.toggle('green');
        yellow.classList.toggle('yellow');
        count = 0;
    }

    count++;
}

let count = 1;

button.onclick = switchLight;