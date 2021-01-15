
$('#message').keydown(function(e) {
    if (e.which == 13) {
        $('#send_message_btn').click();
    }
});

get_map(42, 0, 2);

var user = "You";

function ask(){
    var question = $('#message').serializeArray()[0].value;
    $('#message').val('');
    add_msg(user, question);
    $.ajax({
        type: 'POST',
        url: '/ask',
        dataType:'json',
        contentType: 'text/plain',
        data: question,
        success: function(response){
            add_msg('GrandPy', response);
        },
        error: function(error){
            console.log(error);
        }
    });
}

function add_msg(author, content){

    var dt = new Date();
    var time = dt.getHours() + ":" + dt.getMinutes();

    var msg = `
    <div class="msg_div `+ author +`">
      <p class="msg_header">`+ author +` - `+ time +`</p>
      <p class="msg_content">`+ content +`</p>
    </div>`;
    $('#messages_wrapper').append(msg);

    if(author != user){
        setTimeout(function(){
            get_map(content.position.lat, content.position.lng, 15);
        }, 250);
    }
}

function get_map(pos_lat, pos_lng, zoom_level){
    new google.maps.Map(document.getElementById('map_wrapper'), {
        center: { lat: pos_lat, lng: pos_lng },
        zoom: zoom_level,
    });
}

