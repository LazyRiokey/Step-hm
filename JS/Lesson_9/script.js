/* Создать массив «Список покупок».
Каждый элемент массива должен быть объектом покупки, который содержит следующие свойства:
− название продукта
− необходимое количество/объём
− единицы измерения кол-ва/объёма
− свойство куплен/не куплен.
Написать функцию для вывода списка покупок на экран в понятном для пользователя виде с поясняющими словами и обозначениями.
1. Сортировка списка покупок: в начале – некупленные продукты, в конце – купленные продукты.
2. Добавление покупки в список. Учтите, что при добавлении покупки с уже существующим в списке продуктом, необходимо увеличивать количество в существующей покупке, а не добавлять новую.
3. Покупка продукта. Функция принимает название продукта и отмечает его как купленный.
4. Расчёт и вывод суммарной и средней стоимости всех покупок. */

let shoppingList = [
    {
        productName: 'Bread',
        quantity: 2,
        boxing: 'package per 350g',
        unitPrice: 2, // USD
        req2Buy: false // already bought
    },
    {
        productName: "Bottle of water",
        quantity: 4,
        boxing: 'package per 500ml',
        unitPrice: 0.48,
        req2Buy: true // need to buy
    },
    {
        productName: 'Rice',
        quantity: 4,
        boxing: 'package per 300g',
        unitPrice: 0.7,
        req2Buy: false
    },
    {
        productName: 'Cat food',
        quantity: 3,
        boxing: 'package per 50g',
        unitPrice: 0.7,
        req2Buy: true
    }
];

function displayShopingList(shopObj) {
    console.log('Today, your shopping list is: ');
    sortShopList(shopObj);

    for (let elem of shopObj) {
        if (!elem.req2Buy) {
            console.log(`You have already bought:\n${elem.productName}, ${elem.quantity} ${elem.boxing} at price ${convertToUSD(elem.unitPrice)} each.`);
        }
        else { console.log(`You need to buy:\n${elem.productName}, ${elem.quantity} ${elem.boxing} at price ${convertToUSD(elem.unitPrice)} each.`); }
    }
    
    console.log(`Total price = ${convertToUSD(calcSum(shoppingList))}:
    * The amount for which you need to make purchases is ${convertToUSD(calcSum(filterToBuy(true)))}.
    * The total cost of items in your cart is ${convertToUSD(calcSum(filterToBuy(false)))}.
    * The average cost of all purchases is ${convertToUSD(calcAVG(shoppingList))}.`);
}

function sortShopList(shopObj) {
    shopObj.sort(
        function(propA, propB) {
            if (propA.req2Buy < propB.req2Buy) {
                return 1;
            }
            else { return -1; }
        });
}

function createElemOfShop() {
    let addPurchase = {
        productName: prompt('Enter product name: '),
        quantity: +prompt('Enter the quantity of the product: '),
        boxing: `package per ${prompt('Enter product packaging and units like "...g or ...ml": ')}`,
        unitPrice: +prompt('Enter unit price in USD: '),
        req2Buy: true
    };
    return addPurchase;
}

function letCompare(newObj, shopObj = shoppingList) {
    let indexPN = shopObj.findIndex(item => item.productName == newObj.productName);

    if (indexPN != -1) {
        if (shopObj[indexPN].req2Buy == false && shopObj[indexPN].boxing.includes(newObj.boxing)) {
            shopObj[indexPN].quantity += newObj.quantity;
        }
        else {shopObj.push(newObj);}
        }
    else {shopObj.push(newObj);}
}

function buyProduct(product, shopObj = shoppingList) {
    let productIndex = shopObj.findIndex(item => item.productName == product);

    if (productIndex != -1) {
        if (shopObj[productIndex].req2Buy == true) { 
            shopObj[productIndex].req2Buy = false;
            console.log(`${product} was purchased successfully.`);
        }
        else { console.log(`${product} is already in the cart.`); }
    }
    else{ console.log(`${product} is not on the shopping list.`); }
}

function calcSum(shopObj = shoppingList) {
    let sumPrice = shopObj.reduce(
        function(sum, curVal) {
            return sum + curVal.unitPrice * curVal.quantity;
        },
        0
    );
    return sumPrice;
}

function calcAVG(shopObj = shoppingList) {
    let avgPrice = shopObj.reduce (
        function(avg, curVal, index, array) {
            return avg + curVal.unitPrice * curVal.quantity / array.length;
        },
        0
    );
    return avgPrice;
}

function filterToBuy(req2Buy = Boolean(), shopObj = shoppingList) {
    let allProdPrice = shopObj.filter(
        price => {
            return price.req2Buy == req2Buy;
        }
    );
    return allProdPrice;
}

function convertToUSD(price) {
    return price.toLocaleString('en-US', {style: 'currency', currency: 'USD'});
}


displayShopingList(shoppingList);
console.log(``);
let newShopObj = createElemOfShop();
letCompare(newShopObj);
displayShopingList(shoppingList);
console.log(``);
buyProduct('Onion');
console.log(``);
buyProduct('Bread');
console.log(``);
buyProduct('Cat food');
console.log(``);
displayShopingList(shoppingList);