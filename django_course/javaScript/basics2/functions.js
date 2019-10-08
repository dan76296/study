function hello(name){
    yalert('Hello World'+name)
}

function ask(){
    var askVar = prompt("How was your day today?")
    return askVar
}

function greet(name){
    hello(name)
    ask()
}

greet("Dan")