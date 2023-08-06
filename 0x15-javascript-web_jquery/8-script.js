$(document).ready(function () {
  // Fetch data from the URL using jQuery's $.ajax() method
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      // Loop through the data to extract movie titles and append them to the <ul>
      $.each(data.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function (error) {
      console.log('Error:', error);
    }
  });
});
