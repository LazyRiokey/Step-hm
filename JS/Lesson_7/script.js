/* Задание 1
Написать функцию, которая принимает строку и выводит статистику о ней: количество букв, количество цифр и количество других знаков. */

function calcLetters(string = '') {
    string = string.toLowerCase();
    let lettersRU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя';
    let lettersENG = 'abcdefghijklmnopqrstuvwxyz';
    let fromCalculation = calculation(string, lettersRU, lettersENG);
    return {
        counter: fromCalculation.counter,
        newString: fromCalculation.newString
    }
}

function calcNumbers(string = '') {
    let numbers = '0123456789';
    let fromCalculation = calculation(string, numbers);
    return {
        counter: fromCalculation.counter,
        newString: fromCalculation.newString
    }
}

function calcSpaces(string = '') {
    let spaces = ' ';
    let fromCalculation = calculation(string, spaces);
    return {
        counter: fromCalculation.counter,
        newString: fromCalculation.newString
    }
}

function calcSymbols(string) {
    let symbols = '~`!@"#№$;%^:&?*()_-+={[}]:;"\'<,>./?';
    let fromCalculation = calculation(string, symbols);
    return {
        counter: fromCalculation.counter,
        newString: fromCalculation.newString 
    }
}

function calculation(string = '', firstRegex = '', secondRegex = '') {
    let counter = 0;
    let newString = '';

    for (let i = 0; i < string.length; i++) {
        if (firstRegex.includes(string[i])) {
            counter += 1;
        }
        else if (secondRegex.includes(string[i])) {
            counter += 1;
        }
        else {
            newString += string[i];
        }
    }
    return {
        counter,
        newString
    };
}

function getString() {
    let newString = prompt('Fill in the line with any letters, symbols, numbers and spaces: ');
    return newString;
}

function getNewString() {
    let fromGetString = getString();
    let letters = calcLetters(fromGetString);
    let numbers = calcNumbers(letters.newString);
    let spaces = calcSpaces(numbers.newString);
    let symbols = calcSymbols(spaces.newString);
    return {
        currentString: fromGetString,
        letters: letters.counter,
        numbers: numbers.counter,
        spaces: spaces.counter,
        symbols: symbols.counter
    }
}

function displayStrInfo(string = getNewString()) {
    console.log(`
    Your str: ${string.currentString}
    It includes:
    Letters: ${string.letters}
    Numbers: ${string.numbers}
    Spaces: ${string.spaces}
    Other symbols: ${string.symbols}`);
}

let statString = displayStrInfo();

/* Задание 2
Написать функцию, которая принимает двузначное число и возвращает его в текстовом виде. Например: 35 – тридцать пять, 89 – восемьдесят девять, 12 – двенадцать и т.д. */

function getNumber() {
    let number = +prompt("Enter a number and we'll turn it into a string: ");
    return number;
}

function getUp2Nine(number) {
    switch (Number(number)) {
        case 1:
            return 'один';
        case 2:
            return 'два';
        case 3:
            return 'три';
        case 4:
            return 'четыре';
        case 5:
            return 'пять';
        case 6:
            return 'шесть';
        case 7:
            return 'семь';
        case 8:
            return 'восемь';
        case 9:
            return 'девять';
    }
}

function getUp2Twenty(number) {
    let getNumber = getUp2Nine(String(number)[1]);
    let secondHalfNumber = 'надцать';

    if (number == 10) {
        return 'десять';
    }
    else if (number == 11 || number == 13) {
        return getNumber.concat(secondHalfNumber);
    }
    else if (number == 12) {
        getNumber = getNumber.replace('а', 'е');
        return getNumber.concat(secondHalfNumber);
    }
    else {
        let firstHalfNumber = getNumber.slice(0, -1);
        return firstHalfNumber.concat(secondHalfNumber);
    }
}

function getAfterTwenty(number) {
    let result = getUp2Nine(String(number)[0]);
    
    if (number <= 30) {
        return result.concat('дцать');
    }
    else if (number == 40) {
        return 'сорок';
    }
    else if (number == 90) {
        result = result.replace('ть', '');
        return result.concat('носто');
    }
    else {
        return result.concat('десят');
    }
}

function displayNumber(twoDigitNumber = getNumber()) {
    if (twoDigitNumber < 20) {
        console.log(`${twoDigitNumber} = ${getUp2Twenty(twoDigitNumber)}`);
    }
    else if (twoDigitNumber % 10 == 0) {
        console.log(`${twoDigitNumber} = ${getAfterTwenty(twoDigitNumber)}`);
    }
    else {
        let firstWord = Math.trunc(twoDigitNumber / 10) * 10;
        let secondWord = twoDigitNumber % 10;
        console.log(`${twoDigitNumber} = ${getAfterTwenty(firstWord)} ${getUp2Nine(secondWord)}`);
    }
}

let newNum = displayNumber();

/* Задание 3
Написать функцию, которая преобразует названия CSS-стилей с дефисом в название в camelCase стиле: font-size в fontSize, background-color в backgroundColor, text-align в textAlign. */

function createCssProperty() {
    return prompt('Enter your CSS property with "-": ');
}

function convertString(string) {
    let index = string.indexOf('-');
    let firstWord = string.slice(0, index);
    let secondWord = string.slice(index + 1, string[-1]);
    secondWord = secondWord[0].toUpperCase() + secondWord.replace(secondWord[0], '');
    return firstWord.concat(secondWord);
}

function displayString(property = createCssProperty()) {
    console.log(`Your property is ${property}.\nConverted property is ${convertString(property)}.`);
}

let newString = displayString();