<?php
require 'vendor/autoload.php';
$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->simple_blog->comments;

$comments = $collection->find(['post_id' => $_GET['post_id']]);
$result = [];

foreach ($comments as $c) {
  $result[] = ['name' => $c['name'], 'message' => $c['message']];
}

header('Content-Type: application/json');
echo json_encode($result);
