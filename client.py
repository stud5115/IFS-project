import requests

BASE_URL = "http://127.0.0.1:5000"

def check_balance():
    name = input("Enter your name: ")
    response = requests.get(f"{BASE_URL}/leave_balance", params={"name": name})
    print(response.json())

def request_leave():
    name = input("Enter your name: ")
    days = int(input("Enter number of leave days: "))
    response = requests.post(f"{BASE_URL}/apply_leave", json={"name": name, "days": days})
    print(response.json())

if __name__ == "__main__":
    while True:
        print("\n1. Check Leave Balance")
        print("2. Apply for Leave")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            request_leave()
        elif choice == "3":
            break
