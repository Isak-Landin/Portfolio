function showMore(btn) {
  const personComponent = btn.closest('.person');
  const arrow = personComponent.querySelector('.show-more-div');
  const more = personComponent.querySelector('.more');

  const isClosed = more.style.display == "none";

  if(isClosed){
    arrow.style.display = "rotate(-135deg)";
    more.style.display = "block";
  } else {
    arrow.style.display = "rotate(45deg)";
    more.style.display = "none";
  }
}