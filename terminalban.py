import os

# Yasaklı kullanıcıların listesini dosyada saklayacağız
ban_file = "ban_list.txt"

def load_ban_list():
    if not os.path.exists(ban_file):
        return {}
    with open(ban_file, "r") as file:
        lines = file.readlines()
    ban_list = {}
    for line in lines:
        user_id, user_name = line.strip().split(",")
        ban_list[user_id] = user_name
    return ban_list

def save_ban_list(ban_list):
    with open(ban_file, "w") as file:
        for user_id, user_name in ban_list.items():
            file.write(f"{user_id},{user_name}\n")

def ban_user(user_id, user_name):
    ban_list = load_ban_list()
    ban_list[user_id] = user_name
    save_ban_list(ban_list)

def check_ban_by_name(user_name):
    ban_list = load_ban_list()
    for uid, uname in ban_list.items():
        if uname == user_name:
            print("\033[91mYasaklandı\033[0m")
            return
    print("Yasaklı değil")

def check_ban_by_id(user_id):
    ban_list = load_ban_list()
    if user_id in ban_list:
        print("\033[91mYasaklandı\033[0m")
    else:
        print("Yasaklı değil")

def main():
    while True:
        print("\n1. Name Check\n2. ID Check\n3. Exit")
        choice = input("Bir seçenek seçin: ")
        
        if choice == "1":
            user_name = input("Kullanıcı adını girin: ")
            check_ban_by_name(user_name)
        elif choice == "2":
            user_id = input("Kullanıcı ID'sini girin: ")
            check_ban_by_id(user_id)
        elif choice == "3":
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
