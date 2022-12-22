const mainUl = document.getElementsByClassName('directories')[0];
// Почему бы не назвать эту константу так же, как называется класс у искомого элемента?
// Стоит создавать максимально предсказуемый, однородный и соответствующий своим частям код.

// Не стоит выполнять какую-то работу программно, в данном случае – оборачивание в span'ы, если это можно сделать один раз в исходном коде, и не озадачивать интерпретатор лишней работой. Вместо оборачивания в span'ы также можно применить CSS-свойство width и значение fit-content для того, чтобы область взаимодействия с элементами li определялась только его текстом.
// Вся работа, которую мы можем произвести с кодом в момент написания кода, должна быть выполнена в этот момент написания кода. Всё остальное будет усложнением решения.
for (let elem of mainUl.querySelectorAll('li')) {
    let spanElem = document.createElement('span');
    elem.prepend(spanElem);
    spanElem.append(spanElem.nextSibling);
}

function click(event) {
    let elem = event.target.parentNode.querySelector('ul');

    // Здесь точно так же можно проверять имя целевого элемента на соответствие с 'LI' или проверять наличие у целевого элемента необходимого класса 
    if (event.target.tagName != 'SPAN') {
      return;
    }

    if (!elem) return;

    elem.hidden = !elem.hidden;
}

mainUl.addEventListener('click', click);