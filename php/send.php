<?php

if (isset($_POST["email"]) and isset($_POST["text"])){
  $email = $_POST["email"];
  $text = $_POST["text"];

  $headers = "From: " . $email;

  mail("contact@hahacking.local", "Contact Form", $text, $headers, "-f" . $email);
}

header("Location: http://hahacking.local/");

?>
