
$('#message').keydown(function(e) {
    if (e.which == 13) {
        $('#send_message_btn').click();
    }
});

get_map({lat:42, lng:0}, 2, false);

var user = "You";

function ask(){
    // This function is called everytime the user sends a message to GrandPy
    // It performs an AJAX request and then processes the answer

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
                // If there is a description available for the current request,
                // Grandpy "thinks" for 2.5sec, then sends more information.
                thinking(true);
                setTimeout(function(){
                    thinking(false);
                    desc = fmt_wiki_desc_and_link(answer.description, answer.page_id)
                    add_msg('GrandPy', desc);
                }, 2500);
            }
        },
        error: function(error){
            console.log(error);
        }
    });
}


function fmt_wiki_desc_and_link(desc, page_id){
    // Formats the description and link to a single string element that
    // can be used in the add_msg function below

    var wiki_link = `
        <br>
        [<a href='https://fr.wikipedia.org/?curid=`+ page_id +`'
            target="_blank" rel="noopener noreferrer">
            En savoir plus sur Wikipedia
        </a>]
    `;
    return desc + wiki_link;
}

function add_msg(author, content){
    // Adds a message at the bottom of the messages "window"

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
    // This function ensures the "chat window" scrolls to the last messages
    // each time a new message is sent.

    scrollingElement = document.getElementById('messages_wrapper');
    scrollingElement.scrollTop = scrollingElement.scrollHeight;
}


function thinking(start){
    // Function used to handle the "thinking" animation

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
    // Function handling the Google Maps "window"

    const map = new google.maps.Map(document.getElementById('map_wrapper'), {
        center: pos_lat_lng,
        zoom: zoom_level,
    });
    if(show_marker == true){
        new google.maps.Marker({
            position: pos_lat_lng,
            map,
        });
    }
}

