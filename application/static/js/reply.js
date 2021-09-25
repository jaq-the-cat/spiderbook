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

async function loadReplies(post_uid) {
  const response = await fetch(`/p/${post_uid}/comments`).then((r) => r.json());
  return response.comments;
}

function reply(body) {
  const article = document.createElement("ARTICLE");
  article.classList.add('comment');
  const p = document.createElement("P");
  p.appendChild(document.createTextNode(body));
  article.appendChild(p);
  return article;
}

window.onload = async () => {
  document.querySelectorAll('article.post').forEach(async (post) => {
    const ul = post.children[post.children.length-1];
    const reps = await loadReplies(post
      .children[0].children[0].children[0] // h5 > a > span
      .innerHTML);
    reps.forEach((rep) =>
      ul.children[ul.children.length-1].appendChild(reply(rep)));
  })
}
