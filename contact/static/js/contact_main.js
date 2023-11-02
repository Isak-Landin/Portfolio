function showMore(btn) {
  const personComponent = btn.closest('.person');
  const skillsContainer = personComponent.querySelector('.skills');
  const moreText = personComponent.querySelector('.more');

  if (skillsContainer.style.display === "block") {
    btn.innerHTML = "Read more";
    skillsContainer.style.display = "none";
    moreText.style.display = "none";
  } else {
    btn.innerHTML = "Read less";
    skillsContainer.style.display = "block";
    moreText.style.display = "inline";
  }
}