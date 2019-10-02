var firstName = prompt("What is your first name?");

var lastName = prompt("What is your last name?");

if (firstName[0] == lastName[0]){
    console.log("Potential spy: First letter of both names are the same.")
    var age = prompt("How old are you?")
    if (20 < age < 30){
        console.log("Looking more likely to be a spy now: Age between 20-30")
        var height = prompt("How tall are you? (CM)")
        if (height > 170){
            console.log('Surely must be a spy... Taller than 170cm..')
            var petName = prompt("What is the name of your pet?")
            var lastChar = petName[petName.length -1]
            if ((lastChar == "y") || (lastChar == "Y")){
                console.log("Definitely a spy! Hello Spy. We've been watching you")
            } else {
                console.log("Damn! I thought they were one of em'!")
            }
        } else {
            console.log('Too short. Not a spy!')
        }
    } else {
        console.log("Not a spy: Too young/Old")
    }

} else {
    console.log("Not the spy: Letters don't match up")
}