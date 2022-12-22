// /* 1. Подсчитать сумму всех чисел в заданном пользователем
// диапазоне. */

// let userStartRange = +prompt('Enter start the range: ');
// let userEndRange = +prompt('Enter end the range: ');
// let total = 0;

// for (i = userStartRange; i <= userEndRange; i++) {
//     total += i;
// }

// alert(`The sum of all numbers in the range you specified is: ${total}`);

// /* 2. Запросить 2 числа и найти только наибольший общий
// делитель. */

// let firstNumber = +prompt('Enter the first number: ');
// let secondNumber = +prompt('Enter the second number: ');
// let divisor = 0;

// for (let i = 0; i <= Math.min(firstNumber, secondNumber); i++) {
//     if (firstNumber % i == 0 && secondNumber % i == 0) {
//         divisor = i;
//     }
// }

// alert(`Greatest common divisor ${firstNumber} and ${secondNumber} is ${divisor}.`);

// /* 3. Запросить у пользователя число и вывести все делители
// этого числа. */

// let yourNumber = prompt('Enter dividend: ');
// let newDivisor = [];

// for (let i = 0; i <= yourNumber; i++) {
//     if (yourNumber % i == 0) {
//         newDivisor.push(i);
//     }
// }

// alert(`${newDivisor.join(' ; ')} is all divisors of a number ${yourNumber}. `);

// /* 4. Определить количество цифр в введенном числе. */

// let longNumber = +prompt('Enter a number and we will count the number of digits in it: ');
// let tmpLongNumber = longNumber;
// let numberOfDigits = 0;

// while (tmpLongNumber !== 0) {
//     tmpLongNumber /= 10;
//     tmpLongNumber = Math.trunc(tmpLongNumber);
//     numberOfDigits += 1;
// }

// alert(`In number ${longNumber}, the number of digits is ${numberOfDigits}.`);

// /* 5. Запросить у пользователя 10 чисел и подсчитать, сколько
// он ввел положительных, отрицательных и нулей. При этом
// также посчитать, сколько четных и нечетных. Вывести
// статистику на экран. Учтите, что достаточно одной пере-
// менной (не 10) для ввода чисел пользователем. */

// let totalNumbers = [];
// let positiveNumber = [];
// let negativeNumber = [];
// let zeroNumber = [];
// let even = [];
// let odd = [];
// alert('Enter 10 numbers and we will count them!');

// for (let i = 0; i != 10; i++) {
//     let tenNumbers = prompt('Enter the number: ');
//     totalNumbers.push(tenNumbers);
//     if (tenNumbers == 0) {
//         zeroNumber.push(tenNumbers);
//     }
//     else if (tenNumbers % 2 == 0) {
//         even.push(tenNumbers);
//         if (tenNumbers > 0) {
//             positiveNumber.push(tenNumbers);
//         }
//         else {
//             negativeNumber.push(tenNumbers);
//         }
//     }
//     else if (tenNumbers % 2 != 0) {
//         odd.push(tenNumbers);
//         if (tenNumbers > 0) {
//             positiveNumber.push(tenNumbers);
//         }
//         else {
//             negativeNumber.push(tenNumbers);
//         } 
//     }
// }

// alert(`You entered the numbers: ${totalNumbers.join(' ')}\nPositive: count = ${positiveNumber.length} >> numbers: ${positiveNumber.join(' ')}\nNegative: count = ${negativeNumber.length} >> numbers: ${negativeNumber.join(' ')}\nEven: count = ${even.length} >> numbers: ${even.join(' ')}\nOdd: count = ${odd.length} >> numbers: ${odd.join(' ')}\nZero: count = ${zeroNumber.length} >> numbers: ${zeroNumber.join(' ')}`);

// /* 6. Зациклить калькулятор. Запросить у пользователя 2 числа
// и знак, решить пример, вывести результат и спросить, хо-
// чет ли он решить еще один пример. И так до тех пор, пока
// пользователь не откажется. */

// while (!!confirm('Enter "OK" to start/continue or "Cancel" to stop.')) {
//     let number1 = +prompt('Enter the first number: ');
//     let number2 = +prompt('Enter the second number: ');
//     let userMark = prompt('Enter sign:\n" + " for addition.\n" - " for subtraction.\n" * " for multiplication.\n" / " for division.\n" % " for taking the remainder of the division.\n" ** " for exponentiation.');
//     let total = 0;

//     if (userMark == '+') {
//         total = number1 + number2;
//     }
//     else if (userMark == '-') {
//         total = number1 - number2;
//     }
//     else if (userMark == '*') {
//         total = number1 * number2;
//     }
//     else if (userMark == '/') {
//         total = number1 / number2;
//     }
//     else if (userMark == '%') {
//         total = number1 % number2;
//     }
//     else if (userMark == '**') {
//         total = number1 ** number2;
//     }
    
//     alert(`${number1} ${userMark} ${number2} = ${total.toFixed(2)}`);
// }

// /* 7. Запросить у пользователя число и на сколько цифр его
// сдвинуть. Сдвинуть цифры числа и вывести результат (если
// число 123456 сдвинуть на 2 цифры, то получится 345612). */

// let severalNumbers = prompt('Enter the number: ').split('');
// let shift = prompt('Enter the shift number: ');

// for (let i = 0; i < shift; i++) {
//     severalNumbers.push(severalNumbers.shift());
// }

// alert(severalNumbers.join(''));

// /* 8. Зациклить вывод дней недели таким образом: «День недели.
// Хотите увидеть следующий день?» и так до тех пор, пока
// пользователь нажимает OK. */

// let userWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Suturday', 'Sunday'];
// let userCounter = 0;

// while (!!confirm(`${userWeek[userCounter]}. Do you want to see the next day?`)) {
//     if (userCounter == userWeek.length - 1) {
//         userCounter = 0;
//     }
//     else {
//         userCounter++;
//     }
// }

// /* 9. Вывести таблицу умножения для всех чисел от 2 до 9.
// Каждое число необходимо умножить на числа от 1 до 10. */

let multiplicationTable = String();
alert('The multiplication table will be printed to the console!');

for (let i = 2; i <= 9; i++) {
    for (let k = 1; k <= 10; k++) {
        multiplicationTable += [`${i} * ${k} = ${i * k}\n`];
    }
    console.log(`Multiplication table on ${i}.\n`);
    console.log(multiplicationTable);
    multiplicationTable = String();
}

// /* 10. Игра «Угадай число». Предложить пользователю загадать
// число от 0 до 100 и отгадать его следующим способом:
// каждую итерацию цикла делите диапазон чисел пополам,
// записываете результат в N и спрашиваете у пользователя
// «Ваше число > N, < N или == N?». В зависимости от того
// что указал пользователь, уменьшаете диапазон. Начальный
// диапазон от 0 до 100, поделили пополам и получили 50.
// Если пользователь указал, что его число > 50, то изменили
// диапазон на от 51 до 100. И так до тех пор, пока пользова-
// тель не выберет == N. */

// let requiredNumber = prompt('Enter a number and the computer will guess it: ');
// let computerChoice = toString();
// let rangeNumbers = [];
// let endRange = 100;
// let startRange = 0;
// let counter = 0;
// let question;

// while (computerChoice != requiredNumber) {
//     for (i = startRange; i <= endRange; i++) {
//         rangeNumbers.push(i);
//     }
//     computerChoice = rangeNumbers[Math.floor(rangeNumbers.length / 2)];
//     counter++;
//     question = confirm(`Computer choice this number >> ${computerChoice}.\nThis is your number?`);
//     if (question == true) {
//         alert(`Congratulations! The riddle number has been found!\nThis number is - ${computerChoice}.\nAttempts expended - ${counter}.`);
//     }
//     else {
//         question = confirm('Your number more then computer number?');
//         if (question == true) {
//             alert(`My number is more then computer number!`);
//             startRange = computerChoice + 1;
//             rangeNumbers = [];
//         }
//         else {
//             alert(`My number is less then computer number!`);
//             endRange = computerChoice - 1;
//             rangeNumbers = [];
//         } 
//     }
// }