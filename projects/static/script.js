document.addEventListener('DOMContentLoaded', function() {
  var fadeInElement = document.getElementById('fadeInElement');

  // Add the 'fade-in' class after a delay
  setTimeout(function() {
      fadeInElement.classList.add('fade-in');
  }, 500); // Adjust the delay as needed
});