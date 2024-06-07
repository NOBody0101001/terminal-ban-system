import os

def protocol_here(message, color=None):
    if color == 'red':
        print("\033[91m" + message + "\033[0m")
    elif color == 'green':
        print("\033[92m" + message + "\033[0m")
    else:
        print(message)

def search_in_file(keyword, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if keyword in line:
                return True
    return False

def add_to_blacklist(name, surname, player_id):
    with open("black_list.txt", 'a') as file:
        file.write(f"isim; {name}\nsoyisim; {surname}\nid; {player_id}\n")

def remove_from_blacklist(name, surname, player_id):
    temp_file = "temp_black_list.txt"
    with open("black_list.txt", 'r') as file, open(temp_file, 'w') as temp:
        lines = file.readlines()
        for line in lines:
            if name in line and surname in line and player_id in line:
                continue
            temp.write(line)
    os.remove("black_list.txt")
    os.rename(temp_file, "black_list.txt")

def list_blacklist():
    with open("black_list.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def main_menu():
    text_art = """
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
                       
    """
    print(text_art)

    protocol_here("made by protocolhere", 'green')
    while True:
        print("\n")
        print("1. İsim ile arama")
        print("2. Soyisim ile arama")
        print("3. ID ile arama")
        print("4. Ban ekleme")
        print("5. Ban kaldırma")
        print("6. Yasaklıların tam listesi")
        print("7. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            name = input("Aranacak ismi girin: ")
            if search_in_file(name, "black_list.txt"):
                protocol_here("Yasaklı", 'red')
            else:
                protocol_here("Yasaklı değil", 'green')
        elif choice == '2':
            surname = input("Aranacak soyismi girin: ")
            if search_in_file(surname, "black_list.txt"):
                protocol_here("Yasaklı", 'red')
            else:
                protocol_here("Yasaklı değil", 'green')
        elif choice == '3':
            player_id = input("Aranacak ID'yi girin: ")
            if search_in_file(player_id, "black_list.txt"):
                protocol_here("Yasaklı", 'red')
            else:
                protocol_here("Yasaklı değil", 'green')
        elif choice == '4':
            name = input("İsim: ")
            surname = input("Soyisim: ")
            player_id = input("ID: ")
            add_to_blacklist(name, surname, player_id)
            protocol_here("Oyuncu başarıyla yasaklandı.")
        elif choice == '5':
            name = input("İsim: ")
            surname = input("Soyisim: ")
            player_id = input("ID: ")
            remove_from_blacklist(name, surname, player_id)
            protocol_here("Oyuncunun yasağı kaldırıldı.")
        elif choice == '6':
            list_blacklist()
        elif choice == '7':
            break
        else:
            protocol_here("Geçersiz seçim!")

if __name__ == "__main__":
    main_menu()
