/* const username = 'Dominic' */
let myTypenumber: number = 12;
let myTypeString: string = 'hello world';
let myTypebool: boolean = true;

//arrays
let arraynumber: Array <number> = [1,2,3];
let arraynumber2: number[] = [1,2,3];

let arrayAny: any[] = [1,2,3,true];
let arrayString: string[] = ["1","2","3"];
arrayString.push("hello world"); 

//tuple

let arrayTuple: [string, number, boolean] = ["popo" ,5 ,true];
let arrayTuple2: [string, number, boolean][]; 
arrayTuple2 = [
    ["popo" ,5 ,true], ["popo" ,5 ,false], ["popo" ,5 ,false] 
];

let tata: string | number;

//objects

let object1 = {
    name: 'objete',
    age: 5,
    color: 'yellow'
}

object1.age = 0;