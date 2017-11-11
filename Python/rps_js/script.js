

// let text = document.getElementById('choice');
let output = document.getElementById('output');
let play = document.getElementById('push_btn');
let computer_area = document.getElementById('computer_area');
// let submit = document.getElementById('play_btn');
play.onclick = show_name;

function random_element(array) {
    let random_index = Math.floor(Math.random()*array.length);//gets a random something from an array
    return array[random_index];
}

function show_name() {
    let user_name = document.getElementById('name_q');//asks for the user name to be used later
    user_name.classList.toggle('hidden');
    name_btn.onclick = show_game;//event that will trigger the player choice function when clicked
}

function show_game() {
    let player = document.getElementById('player_choice');//asks for the user game piece choice to be compared to computer random choice
    player.classList.toggle('hidden');//toggles a hidden html makes it visable
    play_btn.onclick = prs_game;//event, will trigger the game function when clicked
}

function prs_game() {
    let gamePieces = ['rock', 'paper', 'scissors'];
    let computerChoice = random_element(gamePieces);

    let name = name_in.value;
    let player = choice.value;

    computer_area.innerText = 'I choose ' + computerChoice;

    if (computerChoice === player) {
        output.innerText = 'Argh, we both win...';
    }

    else if ((computerChoice === gamePieces[0]) && (player === gamePieces[1])) {
        output.innerText = 'Paper covers rock, ' + name + ' wins!';

    }

    else if ((computerChoice === gamePieces[0]) && (player === gamePieces[2])) {
        output.innerText = 'Rock crushes scissors, you lose!';
    }

    else if ((computerChoice === gamePieces[1]) && (player === gamePieces[0])) {
        output.innerText = 'Paper covers rock, you lose';
    }

    else if ((computerChoice === gamePieces[1]) && (player === gamePieces[2])) {
        output.innerText = 'Scissors cut paper ' + name + ' wins!';
    }

    else if ((computerChoice === gamePieces[2]) && (player === gamePieces[0])) {
        output.innerText = 'Rock crushes scissors ' + name + ' wins!';
    }

    else if ((computerChoice === gamePieces[2]) && (player === gamePieces[1])) {
        output.innerText = 'Scissors cut paper, you lose!';
    }
}