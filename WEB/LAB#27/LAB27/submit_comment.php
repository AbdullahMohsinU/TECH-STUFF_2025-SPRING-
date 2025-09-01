<?php
require 'vendor/autoload.php';

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->LAB27->comments;

$collection->insertOne([
    'post_id' => $_POST['post_id'],
    'name' => $_POST['name'],
    'message' => $_POST['message'],
    'time' => new MongoDB\BSON\UTCDateTime()
]);

header("Location: post.php?id=" . $_POST['post_id']);
exit;
