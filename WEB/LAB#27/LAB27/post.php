<?php
require 'vendor/autoload.php';

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->LAB27->comments;

$postId = $_GET['id'] ?? "1";
$comments = $collection->find(['post_id' => $postId]);

$title = "Blog Post";
$content = "Post content here.";

if ($postId == "1") {
  $title = "The Future of AI: What's Next?";
  $content = "
    AI is no longer science fiction—it's already changing our daily lives.
    From self-driving cars to smart assistants like Siri and Alexa, AI is everywhere.
    In this post, we talk about how AI might evolve and what exciting innovations we can expect in the next decade.
  ";
} elseif ($postId == "2") {
  $title = "Web Development in 2025: Trends You Should Know";
  $content = "
    Web development has moved far beyond basic HTML and CSS.
    With tools like Tailwind, React, and AI-assisted coding, even beginners can build stunning websites.
    Let’s explore the hottest trends developers are using in 2025.
  ";
}
?>

<!DOCTYPE html>
<html>
<head>
  <title><?= htmlspecialchars($title) ?></title>
  <link rel="stylesheet" href="style.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-4">
  <a href="index.html" class="btn btn-secondary mb-3">← Back to Home</a>
  <h2><?= htmlspecialchars($title) ?></h2>
  <p><?= nl2br(htmlspecialchars($content)) ?></p>

  <hr>
  <h4>Leave a Comment</h4>
  <form method="POST" action="submit_comment.php" id="commentForm">
    <input type="hidden" name="post_id" value="<?= htmlspecialchars($postId) ?>">
    <input type="text" name="name" placeholder="Your name" class="form-control mb-2" required>
    <textarea name="message" placeholder="Your comment" class="form-control mb-2" required></textarea>
    <button class="btn btn-success">Submit</button>
  </form>

  <hr>
  <h4>Comments</h4>
  <?php foreach ($comments as $comment): ?>
    <div class="comment-box">
      <strong><?= htmlspecialchars($comment['name']) ?>:</strong><br>
      <?= nl2br(htmlspecialchars($comment['message'])) ?>
    </div>
  <?php endforeach; ?>
</div>

<script>
  document.getElementById("commentForm").addEventListener("submit", function(e) {
    const name = document.querySelector('input[name="name"]').value.trim();
    const message = document.querySelector('textarea[name="message"]').value.trim();
    if (!name || !message) {
      alert("Both name and message are required!");
      e.preventDefault();
    }
  });
</script>
</body>
</html>
