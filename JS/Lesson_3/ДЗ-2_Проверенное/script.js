/*  Маленькая оговорка - хоть все надписи и на английском, но я не
совсем уверен в правильном построении предложений. Если окажусь не прав, 
то пожалуйста поправьте меня. */

/* 1. Запросить у пользователя его возраст и определить, кем он
является: ребенком (0–12), подростком (12–18), взрослым
(18_60) или пенсионером (60– ...). */

let yourAge = +prompt('Please enter your age: ');

if (yourAge <= 0) {
    alert("You weren't born yet!");
}
else if (yourAge <= 11) {
    alert('You are a child!');
}
else if (yourAge <= 17) {
    alert('You are a teenager!');
}
else if (yourAge <= 59) {
    alert('You are an adult!');
}
else if (yourAge >= 60) {
    alert('You are retired!');
}
else {
    alert('This age does not exist!');
}

/* 2. Запросить у пользователя число от 0 до 9 и вывести ему
спецсимвол, который расположен на этой клавише (1–!,
2–@, 3–# и т. д). */

let symbol = +prompt('Enter the number: ');

switch (symbol) {
    case 0:
        alert(')');
        break;
    case 1:
        alert('!');
        break;
    case 2:
        alert('@ or "');
        break;
    case 3:
        alert('# or №');
        break;
    case 4:
        alert('$ or ;');
        break;
    case 5:
        alert('%');
        break;
    case 6:
        alert('^ or :');
        break;
    case 7:
        alert('& or ?');
        break;
    case 8:
        alert('*');
        break;
    case 9:
        alert('(');
        break;
    default:
        alert('You entered a number other than 0 - 9!');
}

/* 3. Запросить у пользователя трехзначное и число и проверить,
есть ли в нем одинаковые цифры. */

let number = prompt('Enter a three-digit number: ');

if (number[0] == number[1] && number[0] == number[2]) {
    alert(`In the number ${number} all symbols are the same.`);
}
else if (number[0] == number[1]) {
    alert(`In the number ${number}, the first symbol ${number[0]} and the second symbol ${number[1]} are the same.`);
}
else if (number[1] == number[2]) {
    alert(`In the number ${number}, the second symbol ${number[1]} and the last symbol ${number[2]} are the same.`);
}
else if (number[0] == number[2]) {
    alert(`In the number ${number}, the first symbol ${number[0]} and the last symbol ${number[2]} are the same.`);
}
else {
    alert(`Number ${number} does not contain the same symbols.`);
}

/* 4. Запросить у пользователя год и проверить, високосный он
или нет. Високосный год либо кратен 400, либо кратен 4 и
при этом не кратен 100. */

let year = prompt('Enter the year to check whether it is a leap year or not: ');

alert(year % 400 == 0 || year % 4 == 0 && year % 100 != 0 ? `${year} is leap year.` : `${year} is not leap year.`);
// Тернарные операторы используются только там, где нужно присвовать одно из значений в одну сущность. Здесь же другая ситуация. Но как бы там ни было это хорошая практика!

/* 5. Запросить у пользователя пятиразрядное число и опреде-
лить, является ли оно палиндромом. */

let yourNumber = prompt('Enter a five-digit number: ');

if (yourNumber[0] == yourNumber[4] && yourNumber[1] == yourNumber[3]) {
    alert(`${yourNumber} is palindrome!`);
}
else {
    alert(`${yourNumber} is not palindrome!`);
}

/* 6. Написать конвертор валют. Пользователь вводит количе-
ство USD, выбирает, в какую валюту хочет перевести: EUR,
UAN или AZN, и получает в ответ соответствующую сумму. */

let money = prompt('Enter the amount of your money in USD: ');
let convertMoney = prompt('What currency do we transfer the amount to? EUR, UAH or AZN: ');
let convertedMoney;
const EUR = 0.8826;
const UAH = 26.4114;
const AZN = 1.6990;

switch (convertMoney.toUpperCase()) {
    case 'EUR':
        convertedMoney = money * EUR;
        alert(`Your amount is ${convertedMoney.toFixed(2)} in EUR.`);
        break;
    case 'UAH':
        convertedMoney = money * UAH;
        alert(`Your amount is ${convertedMoney.toFixed(2)} in UAH.`);
        break;
    case 'AZN':
        convertedMoney = money * AZN;
        alert(`Your amount is ${convertedMoney.toFixed(2)} in AZN.`);
        break;
    default:
        alert('USD can only be converted to EUR, UAH or AZN!');
}

/* 7. Запросить у пользователя сумму покупки и вывести сумму
к оплате со скидкой: от 200 до 300 – скидка будет 3%, от 300
до 500 – 5%, от 500 и выше – 7%. */

let purchaseAmount = prompt('Enter the amount you want to buy something: ');
let discount;
let discountedAmount;

if (purchaseAmount > 0 && purchaseAmount < 200) {
    alert(`The amount to be paid is ${purchaseAmount}`);
}
else if (purchaseAmount >= 200 && purchaseAmount <= 300) {
    discount = 0.03;
    discountedAmount = purchaseAmount - purchaseAmount * discount;

    alert(`The amount to be paid with the discount ${Math.trunc(discount * 100)}% is ${discountedAmount.toFixed(2)}`);
    // Округления нужны именно там, где возможно появление большого кол-ва цифр после точки или запятой. Здесь вы используете округление именно по назначению.

}
else if (purchaseAmount > 0 && purchaseAmount <= 500) {
    // Здесь и в условии ниже часть (purchaseAmount > 0) является избыточными, т.к. к этим условиям интерпретор может прийти только через первое условие, где уже проходит проверка на (purchaseAmount > 0).

    discount = 0.05;
    discountedAmount = purchaseAmount - purchaseAmount * discount;
    alert(`The amount to be paid with the discount ${Math.trunc(discount * 100)}% is ${discountedAmount.toFixed(2)}`);
}
else if (purchaseAmount > 0 && purchaseAmount > 500) {
    discount = 0.07;
    discountedAmount = purchaseAmount - purchaseAmount * discount;
    alert(`The amount to be paid with the discount ${Math.trunc(discount * 100)}% is ${discountedAmount.toFixed(2)}`);
}
else {
    alert('Enter the correct value for the purchase amount');
}

/* 8. Запросить у пользователя длину окружности и периметр
квадрата. Определить, может ли такая окружность поме-
ститься в указанный квадрат. */

let diameter = prompt('Enter the diameter of the circle: ');
let perimeter = prompt('Enter the perimeter of the circle: ');

let result = (diameter / 2) == (perimeter / 8) ? `A circle with a diameter of ${diameter} fits into a square with a perimeter of ${perimeter}.` : `A circle with a diameter of ${diameter} does not fit into a square with a perimeter of ${perimeter}.`;
// Такие длинные строки кода лучше записать в несколько строк – пока вы не поставите ; инструкция продолжается, даже после переноса строки.

alert(result);

/* 9. Задать пользователю 3 вопроса, в каждом вопросе по 3 ва-
рианта ответа. За каждый правильный ответ начисляется 2
балла. После вопросов выведите пользователю количество
набранных баллов. */

let points = 0;
let question = prompt('Which is based on the life story of a real person?\n a) a documentary\n b) a docudrama\n c) a biopic ');

if (question.toLowerCase() == 'c') {
    alert('You are right, the correct answer is:\n c) - a biopic..');
    points += 2;
}
else {
    alert('You are wrong, the correct answer is:\n c) - a biopic.');
}

question = prompt('Which can mean a sad story or a story with an unhappy ending?\n a) romance\n b) tragedy\n c) misery');

if (question.toLowerCase() == 'b') {
    alert('You are right, the correct answer is:\n b) - tragedy.');
    points += 2;
}
else {
    alert('You are wrong, the correct answer is:\n b) - tragedy.');
}

question = prompt("What do we call the mix of anxiety and excitement we feel when we don't know what will happen next?\n a) suspense\n b) suspicion\n c) excitation");

if (question.toLowerCase() == 'a') {
    alert('You are right, the correct answer is:\n a) - suspense.');
    points += 2;
}
else {
    alert('You are wrong, the correct answer is:\n a) - suspense.');
}

if (points > 0) {
    alert(`Congratulations, you have completed the quiz - your score is ${points} points.`);
}
else {
    alert(`Your score is ${points} points. Do not despair, try again!`);
}

/* 10. Запросить дату (день, месяц, год) и вывести следующую
за ней дату. Учтите возможность перехода на следующий
месяц, год, а также високосный год. */

let userDay = +prompt('Enter the day: ');
let userMonth = +prompt('Enter the moth: ');
let userYear = +prompt('Enter the year: ');

alert(`Your date is ${userDay} : ${userMonth} : ${userYear}`);

if (userMonth == 2) {
    if (userYear % 400 == 0 || userYear % 4 == 0 && userYear % 100 != 0) {
        if (userDay == 29) {
            userDay = 1;
            userMonth += 1;
        }
        else {
            userDay += 1;
        }
    }
    else if (userDay == 28) {
        userDay = 1;
        userMonth += 1;
    }
    else {
        userDay += 1;
    }
}
else if (userMonth == 12 && userDay == 31) {
    userDay = 1;
    userMonth = 1;
    userYear += 1;
}
else if (userMonth == 1, 3, 5, 7, 8, 10 && userDay == 31) {
    userDay = 1;
    userMonth += 1;
}
else if (userMonth == 4, 6, 9, 11 && userDay == 30) {
    userDay = 1;
    userMonth += 1;
}
else {
    userDay += 1;
}

alert(`Next date is ${userDay} : ${userMonth} : ${userYear}`);