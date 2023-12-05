#!/usr/bin/python3

from celery import Celery, shared_task
from core.zipcracker import ZipCracker
import os

# 200000 first passwords from rockyou.txt
ROCKYOU_PATH = "wordlists/rockyou_chunks/rockyou_aa"

# split -l 200000 rockyou.txt wordlists/rockyou_chunks/rockyou_
WORDLIST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                             ROCKYOU_PATH)

BROKER_URL = os.getenv("REDIS_URL")
BACKEND_URL = os.getenv("BACKEND_URL")

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

passwords = []
with open(WORDLIST_PATH, "rb") as f:
    passwords = f.read().splitlines()

@shared_task(name="bruteforce")
def bruteforce(zip_path):        
    cracker = ZipCracker(zip_path, passwords)
    result = cracker.concurrent_crack()
    
    return result