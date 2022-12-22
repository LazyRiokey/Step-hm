/* Задание 1
Создать объект, описывающий автомобиль (производитель,
модель, год выпуска, средняя скорость), и следующие функции
для работы с этим объектом.
1. Функция для вывода на экран информации об автомобиле.
2. Функция для подсчета необходимого времени для пре-
одоления переданного расстояния со средней скоростью.
Учтите, что через каждые 4 часа дороги водителю необхо-
димо делать перерыв на 1 час. */

function displaвyCar(manufacturer, model, issue, avgSpeed) {
    return `Manufacturer: ${manufacturer}\nModel: ${model}\nYear of issue: ${issue}\nAverage speed: ${avgSpeed}km/h`;
}

function showDriveTime(distance, avgSpeed) {

    // Самое главное, что здесь нужно понять и попрактиковать, так это то, что на месте параметр может быть передан объект со свойствами, и если в функции нужно работать с этими свойствами, то с ними работают, как со свойствами объекта.
    // Если бы эта на месте параметра avgSpeed был передан объект машины car, то к его свойствам можно было бы получить доступ как car.avgSpeed.

    let driveTime = getAverageTime(distance, avgSpeed);
    let driveTimeHours = Math.trunc(driveTime);
    let driveTimeMinutes = Math.round(driveTime % 1 * 60);

    let result = `At a speed of ${avgSpeed}km/h, the emptying time will be ${driveTimeHours} hour(s) and ${driveTimeMinutes} minute(s) for a distance of ${distance}km.`;
    console.log(result);
}

function getRest(hours) {
    if (hours / 4 != 0) {
        return hours + Math.trunc(hours / 4);
    }
    else {
        return hours;
    }
}

function getAverageTime(distance, avgSpeed) {
    return getRest(distance / avgSpeed);
}

function createCarInfo() {
    let manufacturer = prompt('Enter your car brand: ');
    let model = prompt('Enter your car model: ');
    let issue = +prompt('Enter the year of manufacture of the car: ');
    let avgSpeed = +prompt('Enter the average vehicle speed: ');
    console.log(`Characteristics of your vehicle:\n${displayCar(manufacturer, model, issue, avgSpeed)}`);
    return {
        manufacturer,
        model,
        issue,
        avgSpeed
    };
}

let newCar = createCarInfo();

newCar = showDriveTime(900, newCar.avgSpeed);
// Функция showDriveTime ничего не возвращает.
// И также совершенно не верно перезаписывать переменную в которой находится объект, иначе вы потеряете объект.


/* Задание 2
Создать объект, хранящий в себе отдельно числитель и зна-
менатель дроби, и следующие функции для работы с этим объ-
ектом.
1. Функция сложения 2-х объектов-дробей.
2. Функция вычитания 2-х объектов-дробей.
3. Функция умножения 2-х объектов-дробей.
4. Функция деления 2-х объектов-дробей.
5. Функция сокращения объекта-дроби. */

function displayFraction(dividend, devisor) {
    console.log(`${dividend}/${devisor}`);
}

function getSumFraction(firstDev, firstDiv, secondDiv, secondDev) {
    let dividend = firstDev * secondDev + secondDiv * firstDiv;
    let devisor = firstDiv * secondDev;
    return {
        dividend,
        devisor
    };
}

function getSubFraction(firstDev, firstDiv, secondDiv, secondDev) {
    let dividend = firstDev * secondDev - secondDiv * firstDiv;
    let devisor = firstDiv * secondDev;
    return {
        dividend,
        devisor,
    };
}

function getMultFraction(firstDev, firstDiv, secondDiv, secondDev) {
    let dividend = firstDev * secondDiv;
    let devisor = firstDiv * secondDev;
    return {
        dividend,
        devisor,
    };
}

function getDivFraction(firstDev, firstDiv, secondDiv, secondDev) {
    let dividend = firstDev * secondDev;
    let devisor = firstDiv * secondDiv;
    return {
        dividend,
        devisor,
    };
}

function getReductFraction(dividend, devisor) {
    for (let i = Math.min(dividend, devisor); i != 1; i--) {
        if (dividend % i == 0 && devisor % i == 0) {
            dividend /= i;
            devisor /= i;
            break;
        }
    }
    return {
        dividend,
        devisor
    };
}

function createFraction() {
    let dividend = +prompt('Enter the dividend: ');
    let devisor = +prompt('Enter the devisor: ');
    return {
        dividend,
        devisor,
    };
};

let firstFraction = createFraction(10, 15);

// Данный вывод можно назвать как большое переиспользуемое действие, которое можно было бы зхаписать как функцию. Можно было бы написать функцию, которая возвращала бы преобразованную в строку дробь из объекта. А затем эту строку можно было бы вставить в другую строку и вывести всё через console.log.
console.log(`First fraction: ${firstFraction.dividend}/${firstFraction.devisor}`);

let secondFraction = createFraction(4, 16);
console.log(`Second fraction: ${secondFraction.dividend}/${secondFraction.devisor}`);

console.log('Sum of fractions:')
let sumResult = getSumFraction(firstFraction.dividend, firstFraction.devisor, secondFraction.dividend, secondFraction.devisor);
console.log(displayFraction(sumResult.dividend, sumResult.devisor));
sumResult = getReductFraction(sumResult.dividend, sumResult.devisor);
console.log(displayFraction(sumResult.dividend, sumResult.devisor));

/* Задание 3
Создать объект, описывающий время (часы, минуты, секунды), и следующие функции для работы с этим объектом.
1. Функция вывода времени на экран.
2. Функция изменения времени на переданное количество
секунд.
3. Функция изменения времени на переданное количество
минут.
4. Функция изменения времени на переданное количество
часов.
Учтите, что в последних 3-х функциях, при изменении одной
части времени, может измениться и другая. Например: если ко
времени «20:30:45» добавить 30 секунд, то должно получиться
«20:31:15», а не «20:30:75». */

let time = {
    hours: null,
    minutes: null,
    seconds: null,

    createCurTime() {
        this.hours = +prompt('Enter hours: ');
        this.minutes = +prompt('Enter minutes: ');
        this.seconds = +prompt('Enter seconds: ');
        // Одной записи в свойства текущего объекта достаточно, возвращать из этого метода ничего не нужно
    },

    displayTime() {
        let newHours = String(this.hours).padStart(2, '0');
        let newMinutes = String(this.minutes).padStart(2, '0');
        let newSeconds = String(this.minutes).padStart(2, '0');

        console.log(`${newHours}:${newMinutes}:${newSeconds}`);
    },

    addHours(hours) {
        Number(this.hours += hours)
        // Здесь также и везде в подобных ситуациях должен быть не возврат, а присвоение нового занчения в свойство текущего объекта
    },

    addMinutes(minutes) {
        let newMinutes = this.minutes + minutes;
        if (newMinutes >= 60) {
            this.addHours(Math.trunc(newMinutes / 60));
            this.minutes = Math.trunc(newMinutes % 60);
            return Number(this.minutes);
        }
        else {
            this.minutes = newMinutes;
            return Number(this.minutes);
        }
    },

    addSeconds(seconds) {
        let newSeconds = this.seconds + seconds;
        if (newSeconds >= 60) {
            this.addMinutes(Math.trunc(newSeconds / 60));
            this.seconds = Math.trunc(newSeconds % 60);
            return Number(this.seconds);
        }
        else {
            this.seconds = newSeconds;
            return Number(this.seconds);
        }
    },
};

time.createCurTime();
time.displayTime();
time.addSeconds(98);
time.displayTime();
time.addHours(1);
time.displayTime();
time.addMinutes(39);
time.displayTime();


// Решение на освании функций или метод не является чем-то плохими или хорошими – есть только более или менее подходящие решения и есть решения, которые вообще не решают задачу.
