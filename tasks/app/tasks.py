#!/usr/bin/python3

from celery import Celery, shared_task

import zipfile
import concurrent.futures
import os

app = Celery('tasks', broker=os.environ["REDIS_URL"], backend=os.environ["BACKEND_URL"])

passwords = []
with open("/app/wordlists/rockyou.txt", "rb") as f:
    passwords = f.read().splitlines()

@shared_task(name="bruteforce")
def bruteforce(zip_path):
    n_cores = 8
    n_per_core = len(passwords) // n_cores
    
    indexes = [(i, i + n_per_core) for i in range(0, len(passwords), n_per_core)]
    
    zip_path = "/app/" + zip_path

    with concurrent.futures.ProcessPoolExecutor() as executor:
        found = False
        for start, end in indexes:
            if not found:
                future = executor.submit(crack_zip, zip_path, start, end)
                if future.result():
                    found = True
                    return future.result()

def crack_zip(zip_path, start, end):
    print("Trying {} to {}".format(start, end))
    for i in range(start, end):
        with zipfile.ZipFile(zip_path) as zf:
            try:
                zf.extractall("/tmp", pwd = passwords[i])
                return passwords[i]
            except Exception as e:
                pass
    
    
