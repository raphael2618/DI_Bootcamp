def describe_city(city):
    dict = {"Jerusalem",
            "Tel Aviv",
            "West Jerusalem",
            "Haifa",
            "Ashdod",
            "Rishon LeZiyyon",
            "Petah Tiqwa",
            "Beersheba",
            "Netanya",
            "Holon",
            "Bnei Brak",
            "Rehovot",
            "Bat Yam",
            "Ramat Gan",
            "Ashkelon",
            "Jaffa",
            "Modi'in Makkabbim Re'ut",
            "Herzliya",
            "Kfar Saba",
            "Ra'anana",
            "Hadera",
            "Bet Shemesh",
            "Lod",
            "Nazareth",
            "Modiin Ilit",
            "Ramla",
            "Nahariyya",
            "Qiryat Ata",
            "Givatayim",
            "Qiryat Gat",
            "Acre",
            "Eilat",
            "Afula",
            "Karmi'el",
            "Hod HaSharon",
            "Umm el Fahm",
            "Tiberias",
            "Qiryat Mozqin",
            "Qiryat Yam",
            "Rosh Ha'Ayin",
            "Ness Ziona",
            "Qiryat Bialik",
            "Ramat HaSharon",
            "Dimona",
            "Et Taiyiba",
            "Yavne",
            "Or Yehuda",
            "Yehud-Monosson",
            "Safed",
            "Gedera",
            "Tamra",
            "Yehud",
            "Daliyat al Karmel",
            "Migdal Ha`Emeq",
            "Sakhnin",
            "Netivot",
            "Mevasseret Ziyyon",
            "Ofaqim",
            "Arad",
            "Gan Yavne",
            "Qiryat Shemona",
            "Kefar Yona",
            "maalot Tarshiha",
            "Nesher",
            "Tirah",
            "Shoham",
            "Sederot",
            "Rahat",
            "Tirat Karmel",
            "Maghar",
            "Giv'at Shmuel",
            "Ariel",
            "Kafr Kanna",
            "Judeida Makr",
            "Kafr Qasim",
            "Qalansuwa",
            "Bet She'an",
            "Azor",
            "Ganei Tikva",
            "Er Reina",
            "Even Yehuda",
            "Kafr Manda",
            "Iksal",
            "Rekhasim",
            "Nahf",
            "Beit Jann",
            "Herzliya Pituah",
            "El Fureidis",
            "Kfar Yasif",
            "Kabul",
            "Tel Mond",
            "Yeroham",
            "Deir Hanna",
            "Dabburiya",
            "Mazkeret Batya",
            "Bnei Ayish",
            "Bu`eina",
            "Jaljulya",
            "Bir el Maksur",
            "Bet Dagan",
            "Basmat Tab`un",
            "Pardesiyya",
            "Lehavim",
            "Abu Ghaush",
            "Kefar Weradim",
            "Shelomi",
            "Ramat Yishay",
            "Hurfeish",
            "Buqei`a",
            }
    city = input("Enter a city in Israel")

    if city not in dict:
        print("city not in Israel, Goobye")
    else:
        country = "Israel"
        print(f"{city} is in {country}")


describe_city("Tel aviv")
