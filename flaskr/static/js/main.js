
$('#message').keydown(function(e) {
    if (e.which == 13) {
        $('#send_message_btn').click();
    }
});

function ask(){
    question = $('#message').serializeArray()[0].value;
    $('#message').val('');
    add_msg('You', question);
    $.ajax({
        type: 'POST',
        url: '/ask',
        dataType:'json',
        contentType: 'text/plain',
        data: question,
        success: function(response){
            add_msg('GrandPy', response.data);
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
}
