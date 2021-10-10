function infoAboutMe() {
    console.log("Hello I'am Raphael Boussidan, 25 years old and leaving in Tel Aviv." )
}
infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies ) {
    console.log("My favorite color is blue." )
    for (let i = 0, j = personHobbies.length; i < j; i++){
        console.log(personHobbies[i]+' ');
    }
}

infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])