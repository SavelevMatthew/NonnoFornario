$(document).on('submit', '#booking-form', function (e) {
    e.preventDefault();
    $('#submit', '#booking-form').value = 'Sending...'
    console.log($('#date').val())
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            name: $('#name').val(),
            phone: $('#phone').val(),
            date: $('#date').val(),
            time_from: $('#time_from').val(),
            time_to: $('#time_to').val(),
            capacity: $('#capacity').val(),
            location: $('#location').val(),
            smoking: $('input[name=smoking]:checked', '#booking-form').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            $('#booking-form').replaceWith(response)
        }
    })
})