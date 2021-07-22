name = input("Enter the name of your Combos :")

try:
    with open(name, errors="ignore", encoding="utf-8") as file:
        combolist = file.readlines()

        if len(combolist) > 0:
            savefile =open("userpass.txt", "a")


            for combo in combolist:
                try:
                    user = combo.split("\n")[0].split(":")[0].split("@")[0]
                    password = combo.split("\n")[0].split(":")[1]
                    savefile.write(f"{user}: {password}\n")
                except Exception:
                    pass
        else:
            input("Empty File..")
except Exception:
     input("No Such File Exist..")  


#Coded By T.me/YashvirGamingIsBack