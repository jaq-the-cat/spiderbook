document.querySelectorAll('button.add-comment').forEach((el) => {
  el.addEventListener('click', (_e) => {
    el.nextElementSibling.nextElementSibling.classList.toggle('hidden');
  });
});

document.querySelectorAll('button.toggle-comments').forEach((el) => {
  el.addEventListener('click', (_e) => {
    el.nextElementSibling.nextElementSibling.classList.toggle('hidden');
  });
});

function loadReplies(post_uid) {
  fetch('')
}
