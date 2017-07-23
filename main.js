$(document).ready(() => {
    $('.container').hide()
    setInterval(() => {
        $('canvas').hide()
        $('.container').fadeIn(1000)
    }, 1200)

})

