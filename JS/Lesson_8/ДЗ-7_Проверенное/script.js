/* Создать массив «Список покупок».
Каждый элемент массива должен быть объектом покупки, который содержит следующие свойства:
− название продукта
− необходимое количество/объём
− единицы измерения кол-ва/объёма
− свойство куплен/не куплен.
Написать функцию для вывода списка покупок на экран в понятном для пользователя виде с поясняющими словами и обозначениями. */

let shoppingList = [
    {
        productName: 'Bread',
        quantity: 2,
        boxing: 'loaf',
        units: '200g',
        req2Buy: false
    },
    {
        productName: "Bottle of water",
        quantity: 4,
        boxing: 'bottle',
        units: '500ml',
        req2Buy: true
    },
    {
        productName: 'Rice',
        quantity: 4,
        boxing: 'package',
        units: '300g',
        req2Buy: false
    },
    {
        productName: 'Cat food',
        quantity: 3,

        // 
        boxing: 'package',
        units: '50g',
        // С одной стороны такая подробность воспринимается позитивно. Однако с другой стороны, при добавлении новой покупки, пользователю придётся указывать все эти подробности. Необходимо сохранять баланс между функциональностью, детализацией, лёгкостью и удобством в использовании.

        req2Buy: true
    }
];


function displayShopingList(list) {
    console.log('Today, your shopping list is: ');

    // Конструкции условий и циклы отделяйте пустыми строками от остального кода на том же уровне вложенности
    for (let elem of list) {

        // Зхначит свойство req2Buy обозначает необходимость покупки. Важно не перепутать его в будущем ДЗ со свойством куплен/ не куплен.
        if (elem.req2Buy) {
            console.log(`You need to buy:\n${elem.productName}, ${elem.quantity} ${elem.boxing} of ${elem.units}.`);
        }
        else {
            // Слово else можно поднять на одну строку закрывающей фигурной скобкой от верхнего блока if
            console.log(`Already in the cart:\n${elem.productName}, ${elem.quantity} ${elem.boxing} of ${elem.units}.`);
        }
    }
}

displayShopingList(shoppingList);