var founded = false;
var url =  '';
function load()  {
    $.ajax({
                        type: 'GET',
                        url: '/api/isthere?url='+url,
                        dataType: 'json',
                        success: function (data) {
                            if(data['ok'] == true){
                                $('#status').html('Downloaded')
                                document.location.href = '/api/get?url=' + url;
                            } else {
                                $('#status').html('Downloading...');
                            }
                        }
                    });
}

$(document).ready(function () {
    $('#submit_btn').click(function (e) {
        url = $('#url').val();

        $.ajax({
            type: 'POST',
            url: '/api/new?url='+url,
            success: function ()  {
                load();
                setInterval(load,3000);
            }
        });



        e.preventDefault();
    })
})