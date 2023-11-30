#!/usr/bin/python3

from celery import Celery

import zipfile
import concurrent.futures

REDIS_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/0'

app = Celery('zipcracker_tasks', broker=REDIS_URL, backend=BACKEND_URL)

passwords = []
with open("/home/abd/HTB/SecLists/Passwords/Leaked-Databases/rockyou.txt", "rb") as f:
    passwords = f.read().splitlines()

@app.task
def bruteforce(zip_path):
    n_cores = 8
    n_per_core = len(passwords) // n_cores
    
    indexes = [(i, i + n_per_core) for i in range(0, len(passwords), n_per_core)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        found = False
        for start, end in indexes:
            if not found:
                future = executor.submit(crack_zip, zip_path, start, end)
                if future.result():
                    found = True
                    return future.result()

def crack_zip(zip_path, start, end):
    # debug print on celery
    print(f"Trying {start} to {end}")
    for i in range(start, end):
        with zipfile.ZipFile(zip_path) as zf:
            try:
                zf.extractall("/tmp", pwd = passwords[i])
                return passwords[i]
            except Exception as e:
                pass
    
    
