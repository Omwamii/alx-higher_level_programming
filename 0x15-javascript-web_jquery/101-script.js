$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  // Add event handler for removing the last item
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // Add event handler for clearing the list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
