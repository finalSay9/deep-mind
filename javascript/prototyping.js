//dynamic typing and dynamic objects

/**
 * here wallet is
 * starting as a number
 */
let wallet = 50;

/**
 * now changed to 
 * string, thats dynamic 
 * typing easily changed
 * to string
 */
wallet = 'empty';
console.log(wallet)

/**
 * now protype based
 * inheritance
 */
const animalProtype = {
    speak(){console.log('eval speeak')}
}

//create action that inherites directly from animalProtype
const action = Object.create(animalProtype);
action.take = function(){console.log('hello')}

action.take()
action.speak()