const textAnswer = document.getElementById('text-focus');
const img = document.getElementById('eight-ball');
const submit = document.getElementById('submit');

function getRandomIntInclusive() {
    
    min = Math.ceil(1);
    max = Math.floor(20);
    // Не объявленные сущности.
    // Округление целых чисел не имеет смысла. Также, если вы можете на момент написания кода выполнить какую-либо операцию, то записывайте в коде её результат, не стоит передавать эти вычисления интерпретатору – граничные значения генерации случайных чисел можно записать прямо в выражении генерации внизу.

    return Math.floor(Math.random() * (max - min + 1)) + min;
};


// Все варианты ответов можно было расположить в одной функции. Но если так угодно для структуризации и наглядности решения, то можно расположить и в нескольких функциях под разными именами.

function getPositiveAnswer(id) {
    switch(id) {
        case 1:
            return 'It is certain';
        case 2:
            return 'It is decidedly so';
        case 3:
            return 'Without a doubt';
        case 4:
            return 'Yes — definitely';
        case 5:
            return 'You may rely on it';
    };
};

function getHesitantlyPositiveAnswer(id) {
    switch(id) {
        case 6:
            return 'As I see it, yes';
        case 7:
            return 'Most likely';
        case 8:
            return 'Outlook good';
        case 9:
            return 'Signs point to yes';
        case 10:
            return 'Yes';
    };
};

function getNeutralAnswer(id) {
    switch(id) {
        case 11:
            return 'Reply hazy, try again';
        case 12:
            return 'Ask again later';
        case 13:
            return 'Better not tell you now';
        case 14:
            return 'Cannot predict now';
        case 15:
            return 'Concentrate and ask again';
    };
};

function getNegativeAnswer(id) {
    switch(id) {
        case 16:
            return 'Don’t count on it';
        case 17:
            return 'My reply is no';
        case 18:
            return 'My sources say no';
        case 19:
            return 'Outlook not so good';
        case 20:
            return 'Very doubtful';
    };
};

function chooseAnswer(id) {
    if (id < 6) {
        return getPositiveAnswer(id);
    }
    else if (id < 11) {
        return getHesitantlyPositiveAnswer(id);
    }
    else if (id < 16) {
        return getNeutralAnswer(id);
    }
    else { return getNegativeAnswer(id); };
};

function getAnswer() {
    let id = getRandomIntInclusive();
    textAnswer.textContent = chooseAnswer(id);
};

function toggleClass () {
    textAnswer.classList.toggle('text-focus-animation');
    img.classList.toggle('div-img-animation');
};

submit.onclick = function() {
    textAnswer.textContent = '';
    toggleClass();
    setTimeout(getAnswer, 1000);
    setTimeout(toggleClass, 1000);
};