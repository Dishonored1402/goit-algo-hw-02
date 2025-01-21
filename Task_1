import queue
import random
import time

request_queue = queue.Queue()

def generate_request():
    request_id = f"Запит-{random.randint(1000, 9999)}"
    request_queue.put(request_id)
    print(f"Заявку {request_id} додано до черги.")

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}...")
        print(f"Заявку {request_id} успішно оброблено.")
    else:
        print("Черга порожня. Немає заявок для обробки.")

def main():
    print("Сервісна програма для обробки заявок запущена.")
    try:
        while True:
            generate_request()
            time.sleep(1)
            process_request()
    except KeyboardInterrupt:
        print("\nПрограма завершена.")

if __name__ == "__main__":
    main()
