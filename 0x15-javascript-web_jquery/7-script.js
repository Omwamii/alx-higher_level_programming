$(document).ready(function () {
  // Fetch data from the URL using jQuery's $.ajax() method
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the character name from the data and display it in the <div> with ID "character"
      $('#character').text(data.name);
    },
    error: function (error) {
      console.log('Error:', error);
    }
  });
});
