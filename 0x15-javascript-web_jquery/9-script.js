$(document).ready(function () {
  // Fetch data from the URL using jQuery's $.ajax() method
  $.ajax({
	  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
	  type: 'GET',
	  dataType: 'json',
    success: function (data) {
      // Extract the hello value and display
      $('#hello').text(data.hello);
    },
    error: function (error) {
      console.log('Error:', error);
    }
  });
});
