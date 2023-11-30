# Paralel Zip Cracker

## How to run

1. Run redis service (with default configuration)
2. Run celery

```
celery -A tasks.zipcracker_tasks worker -P threads --loglevel=INFO
```

3. Run main.py

```
python3 main.py
```

4. Run client on `views` folder

```
npm i
npm start
```
