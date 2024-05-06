from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

if __name__ == '__main__':
    process = Process(target=print_numbers)
    process.start()
    process.join()  # Optionally, wait for the process to complete
