$(document).ready(function () {
  function fetchAndPrintTranslation () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Fetch data from the URL using jQuery's $.ajax() method
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'GET',
      data: { lang: languageCode },
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (error) {
        console.log('Error:', error);
        $('#hello').text('Error fetching translation. Please try again.');
      }
    });
  }

  // Add event handler for clicking the Translate button
  $('#btn_translate').click(fetchAndPrintTranslation);

  // Add handler for pressing ENTER in the language_code input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchAndPrintTranslation();
      event.preventDefault();
    }
  });
});
