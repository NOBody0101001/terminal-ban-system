import os
import shutil

home_dir = os.path.expanduser("~")
ban_file_path = os.path.join(home_dir, "ban_list.txt")

ban_list_memory = {}

def load_ban_list():
    global ban_list_memory
    if not os.path.exists(ban_file_path):
        ban_list_memory = {}
        return
    with open(ban_file_path, "r") as file:
        lines = file.readlines()
    ban_list_memory = {}
    for line in lines:
        user_id, user_name, user_surname = line.strip().split(",")
        ban_list_memory[user_id] = (user_name, user_surname)

def save_ban_list():
    global ban_list_memory
    with open(ban_file_path, "w") as file:
        for user_id, (user_name, user_surname) in ban_list_memory.items():
            file.write(f"{user_id},{user_name},{user_surname}\n")

def ban_user(user_id, user_name, user_surname):
    global ban_list_memory
    ban_list_memory[user_id] = (user_name, user_surname)
    save_ban_list()
    print(f"Kullanıcı {user_name} {user_surname} (ID: {user_id}) yasaklandı.")

def check_ban_by_name(user_name):
    global ban_list_memory
    for uid, (uname, usurname) in ban_list_memory.items():
        if uname == user_name:
            print("\033[91mYasaklandı\033[0m")
            return
    print("\033[92mYasaklı değil\033[0m")

def check_ban_by_surname(user_surname):
    global ban_list_memory
    for uid, (uname, usurname) in ban_list_memory.items():
        if usurname == user_surname:
            print("\033[91mYasaklandı\033[0m")
            return
    print("\033[92mYasaklı değil\033[0m")

def check_ban_by_id(user_id):
    global ban_list_memory
    if user_id in ban_list_memory:
        print("\033[91mYasaklandı\033[0m")
    else:
        print("\033[92mYasaklı değil\033[0m")

def unban_user(user_id=None, user_name=None, user_surname=None):
    global ban_list_memory
    removed = False
    if user_id and user_id in ban_list_memory:
        del ban_list_memory[user_id]
        removed = True
    elif user_name:
        for uid, (uname, usurname) in list(ban_list_memory.items()):
            if uname == user_name:
                del ban_list_memory[uid]
                removed = True
                break
    elif user_surname:
        for uid, (uname, usurname) in list(ban_list_memory.items()):
            if usurname == user_surname:
                del ban_list_memory[uid]
                removed = True
                break
    if removed:
        save_ban_list()
        print("\033[92mYasak kaldırıldı\033[0m")
    else:
        print("\033[91mKullanıcı bulunamadı\033[0m")

def display_advertisement():
    text_art = """
     ⠀⠀⠀⠀⠀⠀⠸⣶⣦⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢀⠀⢹⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣷⣄⠨⣿⣿⣿⡌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣷⣿⣿⣿⣿⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⣾⣿⣮⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⠟⣹⣿⡿⢿⣿⣿⣬⣶⣶⡶⠦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣢⣙⣻⢿⣿⣿⣿⠎⢸⣿⠕⢹⣿⣿⡿⣛⣥⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⡏⣿⡏⠿⢄⣜⣡⠞⠛⡽⣸⡿⣟⡋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠾⠿⣿⠁⠀⡄⠀⠀⠰⠾⠿⠛⠓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⢐⢉⢷⣀⠛⠠⠐⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⣴⣶⣿⣧⣾⠡⠼⠎⢎⣋⡄⠆⠀⠱⡄⢉⠃⣦⡤⡀⠀⠀⠀⠀
⠀⠀⠐⠙⠻⢿⣿⣿⣿⣿⣿⣿⣄⡀⠀⢩⠀⢀⠠⠂⢀⡌⠀⣿⡇⠟⠀⠀⢄⠀
⠀⣴⣇⠀⡇⠀⠸⣿⣿⣿⣿⣽⣟⣲⡤⠀⣀⣠⣴⡾⠟⠀⠀⠟⠀⠀⠀⠀⡰⡀
⣼⣿⠋⢀⣇⢸⡄⢻⣟⠻⣿⣿⣿⣿⣿⣿⠿⡿⠟⢁⠀⠀⠀⠀⠀⢰⠀⣠⠀⠰
⢸⣿⡣⣜⣿⣼⣿⣄⠻⡄⡀⠉⠛⠿⠿⠛⣉⡤⠖⣡⣶⠁⠀⠀⠀⣾⣶⣿⠐⡀
⣾⡇⠈⠛⠛⠿⣿⣿⣦⠁⠘⢷⣶⣶⡶⠟⢋⣠⣾⡿⠃⠀⠀⠀⠰⠛⠉⠉⠀⠀ 
    """
    print(text_art)
    print("\033[91m made by protocolhere 😈\033[0m")

def main():
    load_ban_list()
    while True:
        display_advertisement()
        print("\n1. Name Check\n2. Surname Check\n3. ID Check\n4. Add Ban\n5. Remove Ban\n6. Exit")
        choice = input("Bir seçenek seçin: ")
        
        if choice == "1":
            user_name = input("Kullanıcı adını girin (Opsiyonel): ")
            if user_name:
                check_ban_by_name(user_name)
            else:
                print("Kullanıcı adı girilmedi.")
        elif choice == "2":
            user_surname = input("Kullanıcı soyadını girin (Opsiyonel): ")
            if user_surname:
                check_ban_by_surname(user_surname)
            else:
                print("Kullanıcı soyadı girilmedi.")
        elif choice == "3":
            user_id = input("Kullanıcı ID'sini girin (Opsiyonel): ")
            if user_id:
                check_ban_by_id(user_id)
            else:
                print("Kullanıcı ID'si girilmedi.")
        elif choice == "4":
            user_id = input("Yasaklamak istediğiniz kullanıcının ID'sini girin: ")
            user_name = input("Yasaklamak istediğiniz kullanıcının adını girin: ")
            user_surname = input("Yasaklamak istediğiniz kullanıcının soyadını girin: ")
            ban_user(user_id, user_name, user_surname)
        elif choice == "5":
            user_id = input("Banını kaldırmak istediğiniz kullanıcının ID'sini girin (Opsiyonel): ")
            user_name = input("Banını kaldırmak istediğiniz kullanıcının adını girin (Opsiyonel): ")
            user_surname = input("Banını kaldırmak istediğiniz kullanıcının soyadını girin (Opsiyonel): ")
            unban_user(user_id or None, user_name or None, user_surname or None)
        elif choice == "6":
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    if not os.path.exists(ban_file_path):
        open(ban_file_path, 'w').close()
    
    main()
