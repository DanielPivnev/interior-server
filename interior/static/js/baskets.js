window.onload = function () {
    $('.baskets-list').on('click', 'input[type="number"]', function () {

        let t_href = event.target;
        console.log('value: ' +  t_href.value, '\n', 'name: ' + t_href.name)

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.baskets-list').html(data.result);
            },
        });

        event.preventDefault();
    });
}