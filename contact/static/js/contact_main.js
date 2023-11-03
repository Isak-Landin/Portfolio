function showMore(show_more_div) {
  const personComponent = show_more_div.closest('.person');
  const more = personComponent.querySelector('.more');

  const isClosed = more.style.display != "block";

  if(isClosed){
    more.style.display = "block";
  } else {
    more.style.display = "none";
  }
}