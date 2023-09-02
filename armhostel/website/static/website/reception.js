window.onload = () => { 
    let interval = 10 * 1000;
    setInterval(getBooks, interval);
}

function getBooks() {
    fetch('/books')
        .then( books => {
            return JSON.parse(books)
        })
        .then( books => {
            console.log(books);
            
        })
}

function renderBook();

function applyBook();

function denyBook();

function removeRequest();

