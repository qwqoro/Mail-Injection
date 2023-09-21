const express = require('express');
const smtp = require('smtp-client');
const path = require('path');
const app = express();
const port = 80;

let s = new smtp.SMTPClient({
  host: "hahacking.local",
  port: 25
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get('/', (req, res) => {
  res.sendFile('index.html', { root: path.join(__dirname, '/public') });
});

app.post('/', (req, res) => {
  let email = req.body.email;
  let text = req.body.text;

  (async function() {
    await s.connect();
    await s.greet({hostname: "hahacking.local"});
    await s.mail({from: email});
    await s.rcpt({to: "contact@hahacking.local"});
    await s.data(text);
    await s.quit();
  })().catch(console.error);

  res.sendFile('index.html', { root: path.join(__dirname, '/public') });
});


app.listen(port, (error) => {
  if (!error) console.log(`[+] App listening on port ${port}`)
  else console.log(`[-] Error occurred during startup`, error)
});
