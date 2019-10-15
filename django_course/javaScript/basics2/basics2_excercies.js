var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
}

function nameLength(name){
    console.log(name.length)
}

nameLength(employee.name)

alert("Name is " + employee.name + ", Job is " + employee.job + ", Age is " + employee.age)

var employee2 = {
    name: "John Smith",
    job: "Programmer",
    age: 31
    nameLength: function(){
        console.log(this.name.length)
    }
}

var employee3 = {
    name: "John Smith",
    job: "Programmer",
    age: 31
    report: function(){
        alert""
    }
}