$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Fetch data from the URL using jQuery's $.ajax() method
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'GET',
      data: { lang: languageCode },
      dataType: 'json',
      success: function (data) {
        // Display the translation of "Hello"
        $('#hello').text(data.hello);
      },
      error: function (error) {
        console.log('Error:', error);
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
