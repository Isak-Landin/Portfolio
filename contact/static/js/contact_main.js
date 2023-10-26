const showMoreButton = document.getElementById('.show-more-button');
const descriptionDiv = document.querySelector('.description-div');

showMoreButton.addEventListener('click', function () {
  if (descriptionDiv.style.display === 'none') {
    descriptionDiv.style.display = 'block';
    showMoreButton.textContent = 'Show Less';
  } else {
    descriptionDiv.style.display = 'none';
    showMoreButton.textContent = 'Show More';
  }
});