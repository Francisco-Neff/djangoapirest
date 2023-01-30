function enviopeticion(type,url,data) {
    return $.ajax({
        type: type,
        url: url,
        async : false,
        headers: {
                "X-CSRFToken": getCookie('csrftoken'),
                "X-Requested-With": "XMLHttpRequest"
            },
        data: data,
        dataType: "text/html",
    })
}