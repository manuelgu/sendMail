# sendMail - An easy class to send E-Mail in Python using SMTP

### How To Use

Clone this repository
```sh
$ git clone https://github.com/manuelgu/sendMail
```

Setup SMTP credentials
  - Edit `sender`, `key` and `receivers` to insert your own data
  - You might have to enable SMTP in your e-mail settings

You need to give the file `+x` so it can be executed
```sh
$ chmod +x sendMail.py
```

Simply run the file and provide the text you wish to send
```sh
$ ./sendMail.py "Hey! How is it going?"
```

### Disclaimer

This is not really useful to use for sending emails, but can rather be used in little scripts that e-mail you when something is going horribly wrong.
