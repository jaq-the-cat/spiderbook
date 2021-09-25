function toggleNextNextSibling(el) {
  el.addEventListener('click', (_e) => {
    el.nextElementSibling.nextElementSibling.classList.toggle('hidden');
  });
}

document.querySelectorAll('button.reply').forEach(toggleNextNextSibling);
document.querySelectorAll('button.replies').forEach(toggleNextNextSibling);

function onReply(el) {
  console.log(new FormData(el).get('post_uid'));
  fetch('/user/comment', {
    method: "post",
    body: new FormData(el),
  }).then((r) => r.json()).then((data) => {
    console.log(data);
  });
  return false;
}
