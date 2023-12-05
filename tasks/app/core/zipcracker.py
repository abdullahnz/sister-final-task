#!/usr/bin/python3

import zipfile
import concurrent.futures

TMP_PATH = "/tmp"

class ZipCracker:
    def __init__(self, zip_path, passwords, n_cores=8):
        self.zip_path = zip_path
        self.passwords = passwords
        self.n_cores = n_cores
        self.is_found = False
    
    def concurrent_crack(self):
        n_passwords = len(self.passwords)
        n_per_core = n_passwords // self.n_cores
        
        result = None
        
        with concurrent.futures.ThreadPoolExecutor() as executor:    
            futures = [
                executor.submit(self.crack_zip_range, i, i + n_per_core)
                for i in range(0, n_passwords, n_per_core)
            ]
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.is_found = True
                    break
            
        return result

    def crack_zip_range(self, start, end):
        # log info in celery logs
        print(f"Distributing {start} - {end} to a core")
    
        zf = zipfile.ZipFile(self.zip_path)
        while not self.is_found and start < end:
            try:
                zf.extractall(TMP_PATH, pwd=self.passwords[start])
                return self.passwords[start]
            except Exception:
                pass
            start += 1
        
        return None