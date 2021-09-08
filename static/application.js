$(document).ready(() => {
  $('#files-form').submit(function(event) {
    event.preventDefault();

    const form = $(this);
    const url = form.attr('action');
    const formData = new FormData(document.getElementById('files-form'))

    $.ajax({
      url,
      type: 'POST',
      enctype: 'multipart/form-data',
      data: formData,
      processData: false,
      contentType: false,
      success: function(data){
        if (data.redirect_url) {
          window.location.href = data.redirect_url;
        } else {
          let stock_data = '';
          for(stock of data.stocks){
            stock_data += stock.join(';').replaceAll('.', ',');
            stock_data += '<br/>';
          }
          $('.stocks-content').html(stock_data);
          $('.stocks-content').removeClass('hidden');

          if (data.template) {
           $('.alert').remove();
           $(data.template).insertBefore('#content');
          }
        }
      },
      error: function(data){
        window.location.href = data.responseJSON.redirect_url
      }
    });
  });
});