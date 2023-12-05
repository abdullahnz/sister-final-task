# Paralel Zip Cracker

## How to run

1. Install docker engine on your computer and `docker-compose`.

2. Downloads [rockyou.txt.gz](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz) and extract to `wordlists/`.

```bash
# split wordlist to chunks
$ split -l 200000 rockyou.txt wordlists/rockyou_chunks/rockyou_
```

3. Build and run with docker compose

```
$ docker-compose up -d --build
```

4. Run client on `views` folder

```
$ npm i
$ npm start
```

5. Stop service

```
$ docker-compose down
```
