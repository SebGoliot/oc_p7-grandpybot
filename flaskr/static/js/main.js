
$('#message').keydown(function(e) {
    if (e.which == 13) {
        $('#send_message_btn').click();
    }
});

get_map({lat:42, lng:0}, 2, false);

var user = "You";

function ask(){
    var question = $('#message').serializeArray()[0].value;
    $('#message').val('');
    add_msg(user, question);
    thinking(true);
    $.ajax({
        type: 'POST',
        url: '/ask',
        dataType:'json',
        contentType: 'text/plain',
        data: question,
        success: function(answer){
            thinking(false);
            add_msg('GrandPy', answer.response);
            if(answer.position != null){
                get_map(answer.position, 17);
            }
            if(answer.description != null){
                thinking(true);
                setTimeout(function(){
                    thinking(false);
                    add_msg('GrandPy', answer.description);
                }, 2500);
            }
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
            <div class="content">
                <p class="msg_header">`+ author +` - `+ time +`</p>
                <p class="msg_content">`+ content +`</p>
            </div>
            <div class="profile"></div>
        </div>
        `;
    $('#messages_wrapper').append(msg);
    scroll_to_bottom();
}


function scroll_to_bottom(){
    scrollingElement = document.getElementById('messages_wrapper');
    scrollingElement.scrollTop = scrollingElement.scrollHeight;
}


function thinking(start){
    if (start == true) {
        var loader = `
        <div class="loader_wrapper">
            <div class="loader"></div>
        </div>
        `;
        $('#messages_wrapper').append(loader);
    } else {
        $('.loader_wrapper').remove();
    }
    scroll_to_bottom();
}


function get_map(pos_lat_lng, zoom_level, show_marker=true){
    const map = new google.maps.Map(document.getElementById('map_wrapper'), {
        center: pos_lat_lng,
        zoom: zoom_level,
    });
    if(show_marker == true){
        new google.maps.Marker({
            position: pos_lat_lng,
            map,
            title: "Hello World!",
        });
    }
}

