import multiprocessing
import time

def exec(id):
    time.sleep(0.5)
    print(f"Thread #{id}")

def main():
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(exec, range(1, 6))

if __name__ == "__main__":
    main()
    