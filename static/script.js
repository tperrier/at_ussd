$(function() { // On Startup

  var at_hist = [];
  $('#clientResponseForm').on('submit',function(evt){
    var data = $(this).serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});
    evt.preventDefault();

    at_hist.push(data.text);
    data.text = at_hist.join('*').slice(1);
    $(this).find('textarea').val('');
    $('#ussdText').html(data.text);


    // Do POST to URL
    $.ajax({
      url:data.url,
      data:data,
      type:'POST',
      success:at_ussd_respond
    });

  });

  // Set form defaults
  var current_location = window.location.href.split('/');
  console.log(current_location);
  $('#clientResponseForm input[name=url]').val(current_location[0] + '//' + current_location[2]);
  var session_id = 'AT_' + Math.floor(Math.random()*9999);
  $('#clientResponseForm input[name=sessionId]').val(session_id);
});

var at_ussd_respond = function(at_text){
    var action = at_text.slice(0,3);
    var text = at_text.slice(4);

    if ( ! (action == 'CON' || action == 'END') ) {
        text = 'Invalid USSD command. String must start with CON or END';
        console.log(at_text);
    }

    $('#mockDisplay').html(text);
}
