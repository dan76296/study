var country1 = "USA"
var country2 = "Germany"
var countries = ["USA", "Germany", "CHINA"]

var countries = ["USA",
                "Germany",
                "CHINA"]

var country1 = countries[0]

// REASSIGNMENT
countries[2] = "France"

// Array can take multiple types

// Pop off the last item
var lastItem = countries.pop()

alert(lastItem)
alert(countries)
// Add to end of array
countries.push("Brazil")

//ARRAY ITERATION
for(var i = 0; i <(countries.length+1); i++){
    console.log(countries[i]
}

for (letter of countries){
    console.log(letter)
}

countries.forEach(alert);

function addAwesome(name){
    console.log(name+"is awesome")
}

var topics = ["python", "django", "science"]

topics.forEach(addAwesome)

