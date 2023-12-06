# Parallel Zip Cracker

Developed for the final presentation of a distributed system course.

## How to run

1. Install docker engine on your computer and docker compose.

2. Downloads [rockyou.txt.gz](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz) and extract to `wordlists/`. Modify `ROCKYOU_PATH` at celery environment inside `docker-compose.yml` file.

```bash
# (in this case i use first 200k from rockyou)
split -l 200000 rockyou.txt wordlists/rockyou_chunks/rockyou_
```

3. Build and run with docker compose.

```
docker-compose up -d --build
```

4. Run client on `views` folder.

```
npm i
npm start
```

5. Stop service.

```
docker-compose down
```

## Our Members

- Affan Ashshiddiq - 1301210250
- Dewa Putu Fajar Wijayakusuma - 1301213161
- Fahmi Agung Maulana - 1301213305
- Muhammad Ramdhan Fitra Hidayat - 1301213582
- Nizam Abdullah - 1301213232
