import time

def risky_operation():
    return 10 / 0

def retry(func, attempts=3):
    for i in range(attempts):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {i+1} failed")
            time.sleep(1)

    return "Failed after retries"

print(retry(risky_operation))
