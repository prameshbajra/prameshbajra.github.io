$(document).ready(() => {
    const quote = $('#quote'),
        author = $('#author'),
        anotherQuote = $('#anotherQuote'),
        blockQuote = $('.blockquote-reverse'),
        container = $('.container')

    container.hide()
    blockQuote.hide()
    setInterval(() => {
        $('canvas').hide()
        $('.container').fadeIn(1000)
    }, 1200)

    const quoteFun = () => {
        fetch("https://favqs.com/api/qotd")
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                const quoteFetch = data.quote.body,
                    quoteAuthor = data.quote.author

                quote.html(quoteFetch)
                author.html(quoteAuthor)
                anotherQuote.html("<h6>Don't like the quote? Click here and wait !</h6>")
                blockQuote.slideDown()
            })
            .catch((error) => {
                console.log(error)
            })
    }

    quoteFun()

    anotherQuote.on('click', (e) => {
        quoteFun()
    });


})

