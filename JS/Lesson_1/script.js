/* 1. Запросите у пользователя его имя и выведите в ответ:
«Привет, его имя!». */

let yourName = prompt('Enter your name: ');
alert(`Hello ${yourName}!`);

/* 2. Запросите у пользователя год его рождения, посчитайте,
сколько ему лет и выведите результат. Текущий год укажите
в коде как константу. */

let date = new Date();
const CURRENT_YEAR = date.getFullYear();
let yourBirthYear = prompt('Enter your birth year: ');
alert(`You are ${CURRENT_YEAR - yourBirthYear} years old.`);

/* 3. Запросите у пользователя длину стороны квадрата и вы-
ведите периметр такого квадрата. */

let sideOfTheQuad = prompt('Enter the side of the square: ');
let perimeter = sideOfTheQuad * 4;
alert(`The perimeter of a square is ${perimeter} units.`);

/* 4. Запросите у пользователя радиус окружности и выведите
площадь такой окружности. */

let radius = prompt('Enter the radius of the circle: ');
let areaOfACircle = Math.PI * Math.pow(radius, 2);
alert(`The area of the circle is ${areaOfACircle.toFixed(2)} units.`);

/* 5. Запросите у пользователя расстояние в км между двумя
городами и за сколько часов он хочет добраться. Посчи-
тайте скорость, с которой необходимо двигаться, чтобы
успеть вовремя. */

let S = prompt('Enter the distance in kilometers from city A to city B: ');
let t = prompt('Enter the time in hours for which you want to get from city A to city B: ');
let V = S / t;
alert(`The speed at which you need to move - ${V.toFixed(1)} km/h.`);

/* 6. Реализуйте конвертор валют. Пользователь вводит долла-
ры, программа переводит в евро. Курс валюты храните в
константе. */

let usd = prompt('Enter the number in USD: ');
const EUR = 0.8678;
alert(`Your amount in EUR is: ${(usd * EUR).toFixed(2)}.`);

/* 7. Пользователь указывает объем флешки в Гб. Программа
должна посчитать сколько файлов размером в 820 Мб по-
мещается на флешку. */

let flashDriveVolume = prompt('Enter the volume of the flash drive in gb: ') * 1000;
const FILE_SIZE = 820;
alert(`The flash drive will fit ${Math.floor(flashDriveVolume / FILE_SIZE)} files.`);

/* 8. Пользователь вводит сумму денег в кошельке и цену одной
шоколадки. Программа выводит сколько шоколадок может
купить пользователь и сколько сдачи у него останется. */

let yourMoney = prompt('How much money do you have? ');
let chocolateBarPrice = prompt('How much does a chocolate bar cost? ');
alert(`You can buy ${Math.floor(yourMoney / chocolateBarPrice)} chocolate bar. You have ${yourMoney % chocolateBarPrice} change units left.`);

/* 9. Запросите у пользователя трехзначное число и выведите
его задом наперед. Для решения задачи вам понадобится
оператор % (остаток от деления). */

let yourNumber = prompt('Enter a three-digit number: ');
let tmpNumber = yourNumber;
let hundredthPart = tmpNumber % 10;
tmpNumber = Math.trunc(tmpNumber /= 10);
let tenthPart = tmpNumber % 10;
tmpNumber = Math.trunc(tmpNumber /= 10);
let reverseNumber = hundredthPart * 100 + tenthPart * 10 + tmpNumber;
alert(`Reverse number ${yourNumber} is ${reverseNumber}.`);

/* 10. Запросите у пользователя целое число и выведите в ответ,
четное число или нет. В задании используйте логические
операторы. В задании не надо использовать if или switch. */

let number = prompt("Let's check the number for evenness: ");
let odd_or_even = number % 2 === 0;
alert(`Is the number ${number} even? - ${odd_or_even}.`);
