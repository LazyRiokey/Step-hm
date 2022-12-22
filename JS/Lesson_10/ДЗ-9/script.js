/* Задание 1
Используя средства и возможности навигации по DOM, получите доступ к следующим HTML-элементам: */

console.log('------------');
console.log('Task 1:');
console.log('------------');

// 1. К элементу с текстом «Сезоны года»

console.log('');

console.log('Seasons of the year:');

console.log(document.body.firstElementChild);

console.log('------------');

// 2. К элементу с текстом «Дополнительная информация»

console.log('Additional Information:');

console.log(document.body.childNodes[3].childNodes[1]);

console.log('------------');

// 3. К элементу со списком всех сезонов года

console.log('Seasons:');

console.log(document.body.children[2]);

console.log('------------')

// 4. К элементу списка с текстом «Зима» и списком зимних месяцев

console.log('Winter:')

console.log(document.body.children[2].firstElementChild);

console.log('------------')

// 5. К элементу с текстом «Весна» и списком весенних месяцев от предыдущего элемента с текстом «Зима»

console.log('Spring:')

console.log(document.body.children[2].firstElementChild.nextElementSibling);

console.log('------------')

// 6. К элементу с месяцем вашего рождения или к любому другому любимому месяцу.

console.log('Month of birth:')

console.log(document.body.children[2].firstElementChild.firstElementChild.lastElementChild);

console.log('');

/* Задание 2
Используя средства и возможности поиска элементов по DOM вместе с навигацией по DOM, получите доступ к следующим HTML-элементам:
 */

console.log('------------');
console.log('Task 2:');
console.log('------------');

// 1. К элементу с текстом «Сезоны года»

console.log('');

console.log('Seasons:');

console.log(document.getElementById('header'));

console.log('------------');

// 2. К элементу с текстом «Дополнительная информация»

console.log('Additional Information:');

console.log(document.getElementsByClassName('text')[0]);

console.log('------------');

// 3. К элементу с текстом текущего месяца

console.log('Current month:');

const december = document.getElementsByClassName('month')[0];
console.log(december);

console.log('------------');

// 4. Проверьте находится ли элемент текущего месяца в элементе сезона с текстом «Осень», который является 3-м по счёту (используя метод matches)

console.log('Matches:');

console.log(december.matches('.season:last-child .month'));

console.log('------------');

// 5. Получите доступ к элементу со списком всех сезонов года от элемента текущего месяца (используя метод closest)

console.log('Closet:');

console.log(december.closest('.season').parentNode);

console.log('------------');

// 6. Проверьте вложен ли элемент текущего месяца в элемент со списком всех сезонов года (используя метод contains)

console.log('Contains:');

const seasons = document.getElementById('season-list');
console.log(seasons.contains(december));