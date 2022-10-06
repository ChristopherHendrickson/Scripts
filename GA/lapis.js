const choices = ["Lapis", "Papyrus", "Scalpellus"];

const player = {
    currentChoice: null,
}
const computer = {
    currentChoice: null,
}

player.currentChoice = choices[0]

function comupterChooses() {
    const randomIndex = Math.floor(Math.random()*3);
    computer.currentChoice = choices[randomIndex]
}

function compareChoices() {
    comupterChooses()
    if (player.currentChoice == choices[0]) {
        if (computer.currentChoice == choices[0]){
            result=("It's a tie! the player and computer both chose "+choices[0])
        } else if (computer.currentChoice == choices[1]) {
            result=("The computer wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        } else {
            result=("The player wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        }
    }
    if (player.currentChoice == choices[1]) {
        if (computer.currentChoice == choices[1]){
            result=("It's a tie! the player and computer both chose "+choices[1])
        } else if (computer.currentChoice == choices[2]) {
            result=("The computer wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        } else {
            result=("The player wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        }
    }   
    if (player.currentChoice == choices[2]) {
        if (computer.currentChoice == choices[2]){
            result=("It's a tie! the player and computer both chose "+choices[2])
        } else if (computer.currentChoice == choices[0]) {
            result=("The computer wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        } else {
            result=("The player wins! The computer chose " + computer.currentChoice+" and the player chose "+player.currentChoice)
        }
    }
    document.body.append(result)
}

compareChoices()

document.querySelector("#lapis")