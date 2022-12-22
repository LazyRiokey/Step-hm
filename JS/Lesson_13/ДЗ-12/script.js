const mainUl = document.getElementsByClassName('directories')[0];

for (let elem of mainUl.querySelectorAll('li')) {
    let spanElem = document.createElement('span');
    elem.prepend(spanElem);
    spanElem.append(spanElem.nextSibling);
}

function click(event) {
    let elem = event.target.parentNode.querySelector('ul');

    if (event.target.tagName != 'SPAN') {
      return;
    }

    if (!elem) return;

    elem.hidden = !elem.hidden;
}

mainUl.addEventListener('click', click);