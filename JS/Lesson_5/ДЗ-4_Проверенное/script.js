/* 1. Написать функцию, которая принимает 2 числа и возвращает:
 -1, если первое меньше, чем второе;
 1 – если первое больше, чем второе;
 0 – если числа равны. */

function returnNum(firstNumber, secondNumber) {
    if (firstNumber == secondNumber) {
        return 0;
    }
    else if (firstNumber < secondNumber) {
        return -1;
    }
    else {
        return 1;
    }
    // else'ы можно записать на строках выше после закрывающих }, т.о. код станет немного ниже и не потеряет своей наглядности
}

console.log('Task 1:');
console.log(returnNum(0, 0));
console.log(returnNum(1, 0));
console.log(returnNum(0, 1));

// /* 2. Написать функцию, которая вычисляет факториал переданного ей числа. */

// Отлично!
function calcFactorial(number) {
    return number != 1 ? number * calcFactorial(number - 1) : 1;
}

console.log('Task 2:');
console.log(calcFactorial(5));
console.log(calcFactorial(6));

/* 3. Написать функцию, которая принимает три отдельные цифры и превращает их в одно число. 
Например: цифры 1, 4, 9 превратятся в число 149. */

function convertThree(a, b, c) {
    return Number(`${a}${b}${c}`);
}

console.log('Task 3:');
console.log(convertThree(1, 4, 9));
console.log(convertThree(8, 3, 1));

/* 4. Написать функцию, которая принимает длину и ширину прямоугольника и вычисляет его площадь. 
Если в функцию передали 1 параметр, то она вычисляет площадь квадрата. */

// Строка 51 пустая. Пустые строки не используются между вышестоящим кодом в верхней области видимости и нижестоящим кодом во внутренней области видимости. Между ними должен быть отступ и этот отступ наглядно показывает различие между двумя строками кода. Поэтому пустые строки между фрагментами кода в различных областях видимости чаще всего не используют.
function calcSquare(a, b) {
    
    if (a && b) {
        return a * b;
    }
    else {
        return a ** 2;
    }
}

console.log('Task 4:');
console.log(calcSquare(4, 9));
console.log(calcSquare(9));

/* 5. Написать функцию, которая проверяет, является ли переданное ей число совершенным. 
Совершенное число – это число, равное сумме всех своих собственных делителей. */

function isPerfect(num) {
    let result = 0;

    // То же самое насчёт строки 72 (комментарий на строке 49)
    for (let i = 0; i < num; i++) {

        if (num % i == 0) {
            result += i;
        }
    }

    return result == num ? num : false;
    // Было бы правильнее, если бы функция возвращала логическое значение true или false в зав-сти от найденного совершенного числа
}

console.log('Task 5:');
console.log(isPerfect(8));
console.log(isPerfect(28));

/* 6. Написать функцию, которая принимает минимальное и максимальное значения для диапазона, 
и выводит только те числа из диапазона, которые являются совершенными. 
Используйте написанную ранее функцию, чтобы узнавать, совершенное число или нет. */

function checkIsPerfect(start, stop) {
    let total = '';

    for (let i = start; i <= stop; i++) {

        // В условиях можно использовать функции, которые возвращают логическое значение. Ваша функция isPerfect по-хорошему должна возвращать логическое значение, которое можн не сравнивать с другим логическим значением.
        if (isPerfect(i) != false) {
            total += i + ' ';
        }
    }

    return total;
}

console.log('Task 6:');
console.log(checkIsPerfect(1, 900));

/* 7. Написать функцию, которая принимает время (часы, минуты, секунды) и выводит его на экран в формате «чч:мм:сс». 
Если при вызове функции минуты и/или секунды не были переданы, то выводить их как 00.
 */

function displayTime(hours = 0, minutes = 0, seconds = 0) {

    if (hours < 10) {
        hours = '0' + hours; 
    }

    if (minutes < 10) {
        minutes = '0' + minutes;
    }

    if (seconds < 10) {
        seconds = '0' + seconds;
    }

    return `${hours}:${minutes}:${seconds}`;
}

console.log('Task 7:');
console.log(displayTime(2));
console.log(displayTime(12, 4));
console.log(displayTime(3, 5, 9));
console.log(displayTime(13, 52, 19));

/* 8. Написать функцию, которая принимает часы, минуты и секунды и возвращает это время в секундах. */

function toSeconds(hours = 0, minutes = 0, seconds = 0) {
    return hours * 3600 + minutes * 60 + seconds;
}

console.log('Task 8:');
console.log(toSeconds(2, 18, 50));
console.log(toSeconds(1, 21, 14));
console.log(toSeconds(0, 21, 14));
console.log(toSeconds(0, 0, 14));

/* 9. Написать функцию, которая принимает количество секунд, переводит их в часы, минуты и секунды и возвращает в виде строки «чч:мм:сс». */

function fromSeconds(seconds = 0) {

    // Здесь очень пригодился бы оператор остатка от деления %. Например чтобы найти кол-во секунд, из которых нельзя получить 1 час, можно выполнить seconds % 3600.

    let hours = Math.floor(seconds / 3600);
    let tmp = Math.floor(seconds - hours * 3600);
    let minutes = Math.floor(tmp / 60);
    let remSeconds = tmp - minutes * 60;

    return displayTime(hours, minutes, remSeconds);
}

console.log('Task 9:');
console.log(fromSeconds(2));
console.log(fromSeconds(182));
console.log(fromSeconds(1825));
console.log(fromSeconds(18256));

/* 10. Написать функцию, которая считает разницу между датами. 
Функция принимает 6 параметров, которые описывают 2 даты, и возвращает результат в виде строки «чч:мм:сс». 
При выполнении задания используйте функции из предыду-щих 2-х заданий: 
сначала обе даты переведите в секунды, 
узнайте разницу в секундах, 
а потом разницу переведите обратно в «чч:мм:сс». */

function calculateDate (hours_1 = 0, minutes_1 = 0, seconds_1 = 0, hours_2 = 0, minutes_2 = 0, seconds_2 = 0) {
    let date_1 = toSeconds(hours_1, minutes_1, seconds_1);
    let date_2 = toSeconds(hours_2, minutes_2, seconds_2);

    return (date_1 - date_2) > 0 ? fromSeconds(date_1 - date_2) : fromSeconds (date_2 - date_1);
    // Здесь более наглядным способом написания кода будет использование конструкции условий. Тернарный оператор используется для присвоения в одну сущность некоторые более-менее готовых значений, а не значений, которые получаться при вызове функций. Вызовы функций с разными аргументами лучше размещать в отдельных ветках конструкции условий.
}

console.log('Task 10:');
console.log(calculateDate(1, 15, 22, 2, 22, 47));
console.log(calculateDate(8, 27, 13, 5, 26, 15));