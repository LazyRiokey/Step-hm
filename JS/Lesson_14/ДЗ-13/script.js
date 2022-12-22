const directories = document.getElementsByClassName('directories')[0];
const spans = directories.getElementsByTagName('span');

function click(event) {
    let ul = event.target.parentNode.querySelector('ul');

    if (event.target.tagName != 'SPAN') {
      return;
    }

    if (!ul) return;

    ul.hidden = !ul.hidden;
};

directories.addEventListener('click', click);

let spanCounter = -1;

document.addEventListener('keydown', function(event) {
    if (event.key == 'ArrowDown') {
        if (spanCounter < 0) {
            spanCounter = 0;
            spans[spanCounter].focus();
        }
        else if (spanCounter == spans.length-1) {
            spanCounter = spans.length-1;
            alert('End of list');
        }
        else {
            spans[spanCounter].setAttribute('tabindex', -1);
            spans[++spanCounter].setAttribute('tabindex', 0);
            spans[spanCounter].focus();
        }
    }

    if (event.key == 'ArrowUp') {
        if (spanCounter == 0) {
            spanCounter = 0;
            alert('End of list');
        }
        else {
            spans[spanCounter].setAttribute('tabindex', -1);
            spans[--spanCounter].setAttribute('tabindex', 0);
            spans[spanCounter].focus();
        }
    }

    if (event.key == 'Enter') {
        click(event);
    }
});