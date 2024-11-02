from tabulate import tabulate

class User:
    #data user
    data_user = {
        1: ["Rosy", "Basic Plan", 12, "rosy-123"],
        2: ["Anton", "Standard Plan", 9, "anton-123"],
        3: ["Agus", "Basic Plan", 1, "agus-123"],
        4: ["Budi", "Premium Plan", 5, "budi-123"],
        5: ["Shania", "Basic Plan", 6, "shania-123"],
    }
    
    #data list plan
    list_plan = ["Basic Plan", "Standard Plan", "Premium Plan"]
    table = [[True, True, True, "Bisa Stream"],
             [True, True, True, "Bisa Download"],
             [True, True, True, "Kualitas SD"],
             [False, True, True, "Kualitas HD"],
             [False, False, True, "Kualitas UHD"],
             [1, 2, 4, "Number of Devices"],
             ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
             [120_000, 160_000, 200_000, "Harga"]]

    headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

    def __init__(self, username):
        '''
        fungsi untuk menginisialisasi objek user

        parameters:
            username (str)
        '''
        self.username = username
        self.current_plan = None
        self.duration_plan = None
        self.kode_refferal = None

        #mengecek apakah username ada di data_user
        for key, value in self.data_user.items():
            if value[0] == self.username:
                #jika ada maka akan menampilkan current plan, duration plan dan kode refferal
                self.current_plan = value[1]
                self.duration_plan = value[2]
                self.kode_refferal = value[3]
                break
    
    def check_all_plan(self):
        '''
        untuk menampilkan semua plan dan benefitnya

        parameters:
            none
        '''
        print("List Benefit and Plan From Pacflix")
        print(tabulate(self.table, self.headers)) 