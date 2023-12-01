# Paralel Zip Cracker

## How to run

1. Install docker engine on your computer and `docker-compose`.

2. Downloads [rockyou.txt.gz](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz) and extract to `wordlists/`.
3. Run api with docker

```
docker-compose up -d --build
```

4. Run client on `views` folder

```
npm i
npm start
```
