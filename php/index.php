<!DOCTYPE html>
<html>
  <head>
    <title>HaHacking - Обратная связь</title>
    <link rel="stylesheet" href="index.css">
  </head>
  <header>
    <div class="logo">
      <h1>[HaHacking] E-mailI&ensp;&#128231;</h1>
    </div>
  </header>
  <body>
    <div class="contact">
      <h2 class="title">Связаться</h2>
      <form action="send.php" method="post">
        <label for="name">Адрес электронной почты:</label><br/>
        <input type="email" id="email" name="email" placeholder="you@example.org"/><br/>
        <label for="text">Текст обращения:</label><br/>
        <textarea id="text" name="text" minlength="10" placeholder="Здравствуйте!"></textarea><br/>
        <button class="submit">Отправить&ensp;→</button>
      </form>
    </div>
  </body>
  <footer>
    <div class="link">
      <hr/>
      <p><a href="https://t.me/hahacking">@HaHacking</a> &copy; 2023</p>
    </div>
  </footer>
</html>
