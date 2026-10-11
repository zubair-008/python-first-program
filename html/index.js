// alert("Welcome to my website.");
// let name = "Zubair";
// alert("My name is " + name + " and I am web developer");

// let fullname ="Zubair", age = 25, city="Lahore";
// let users = [fullname, age, city];
// console.log(users);

// let user = {
//     name: "Zubair",
//     age: 25,
//     city: "Lahore"
// }

// console.log("User Information Object:", user);


// let studen_name = "Zubair Tariq";
// console.log("Initial Student Name:", studen_name)
// studen_name = "Zee";
// console.log("Updated Student Name:", studen_name);

// let first_name= "Zubair";
// let last_name="Tariq";
// console.log("Concate Name:", first_name + " " + last_name);

// console.log(`Hello ${first_name} ${last_name}. How are you?`)
// console.log(first_name.toUpperCase());


// let num = 10;

// console.log("Initial Number:", num);
// num += 5;

// console.log("After Addition:", num);
// num *=2;
// console.log("After Multiplication:", num);

// num -=3;
// console.log("After Substraction:", num);

// num /=4;
// console.log("After Division:", num);

// function calculate(){
//     let num1 = 10;
//     let num2 = 5;
//     let sum = num1 + num2;
//     let sub = num1 - num2;
//     console.log("Sum:", sum);
//     console.log("Subtraction:", sub)
// }

// calculate();

// function calculate(num1, num2, num3, num4){
//     let sum = num1 + num2;
//     let sub = num1 - num2;
//     let multiply = num3 * num4;
//     let divide = num3 / num4;
//     console.log("Sum:", sum);
//     console.log("Subtraction:", sub);
//     console.log("Multiply:", multiply);
//     console.log("Divide:", divide);
// }

// calculate(10,5, 10, 5);

const calculate = (num1, num2) =>{
    let sum = num1 + num2;
    let sub = num1 - num2;
    console.log("Sum", sum);
    console.log("Subsraction:", sub)
}
calculate(10,5)