function testStr(arr, regexp) {
    arr.forEach(function(element) {
        let result = regexp.test(element);

        console.log(`
        Строка: '${element}'
        РВ: ${String(regexp)}
        Результат: ${result}`);
    });
};

let regexpPhone =/^\+?\d\s\(\w{3}\)\s\w{3}(\b-\w{2}){2}/;
let testsPhone = [' +7(123)456-78-90', '7123456-78-90', '8 123 456 78 90', '380904005060' , 
'asd +7 (123) 456-78-90 asd', '+7 (123) 456-78-90'];

testStr(testsPhone, regexpPhone);
console.log('\t\t------------------------------------------------');

let regexpEmail = /^\w+@((\b\w+.)+)\.\w+/;
let testsEmail = ['email123@domen1.com', 'email123@domen1.domen2.com', 'email123@domen1.domen2.domen3.com',
'words123@domen1com', 'words123@domen1com. ', 'words123@ domen1com', '  words123@domen1com  '];

testStr(testsEmail, regexpEmail);