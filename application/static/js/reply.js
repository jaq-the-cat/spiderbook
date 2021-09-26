// [ Button functionality
document.querySelectorAll('button.add-comment').forEach((el) => {
  el.addEventListener('click', (_e) => {
    el.nextElementSibling.nextElementSibling.classList.toggle('hidden');
  });
});

document.querySelectorAll('button.toggle-comments').forEach((el) => {
  el.addEventListener('click', (_e) => {
    el.innerHTML = el.innerHTML ===
      "open replies" ? "close replies" : "open replies";
    el.nextElementSibling.nextElementSibling.classList.toggle('hidden');
  });
});

// ]


// [ Load comments
function reply(body) {
  const article = document.createElement("ARTICLE");
  article.classList.add('comment');
  const p = document.createElement("P");
  p.appendChild(document.createTextNode(body));
  article.appendChild(p);
  return article;
}

async function updatePost(post_uid, div) {
  let reps = await fetch(`/p/${post_uid}/comments`).then((r) => r.json());
  reps = reps.comments;
  div.innerHTML = '';
  reps.reverse().forEach((rep) => {
    div.appendChild(reply(rep));
  });
}

async function loadReplies(post_uid=null) {
  if (post_uid == null) {
    document.querySelectorAll('article.post').forEach(async (post) => {
      const post_uid = post.id;
      const ul = post.children[post.children.length-1];
      const div = ul.children[ul.children.length-1];
      updatePost(post_uid, div);
    })
  } else {
    const post = document.getElementById(post_uid);
    const ul = post.children[post.children.length-1];
    const div = ul.children[ul.children.length-1];
    updatePost(post_uid, div);
  }
}

window.onload = () => loadReplies();
// ]

// [ Reload comments on comment add
document.querySelectorAll('.comment-section').forEach((el) => {
  const form = el.children[2];
  form.onsubmit = (_e) => {
    const fd = new FormData(form);
    fetch('/user/comment', {
      method: 'post',
      body: fd,
    }).then((r) => r.json()).then((_resp) => {
      loadReplies(fd.get('post_uid'));
    });
    return false;
  };
});
// ]
