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
        print("....")
        print(tabulate(self.table, self.headers)) 
    
    def check_user_plan(self):
        '''
        untuk menampilkan user plan dan benefitnya current user
        
        parameters:
            none
        '''
        if(self.current_plan):
            print(f"{self.username} sedang berlangganan {self.current_plan}")
            print("Benefit")

            #mencari indek current plan pada list data
            idx_current_plan = self.list_plan.index(self.current_plan)
            #menampilkan header current plan dan servisnya
            headers_user = [self.headers[idx_current_plan], self.headers[-1]]
            #menampilkan data tablenya berdasarkan current user
            benefit_user = [[row[idx_current_plan], row[-1]] for row in self.table]

            print(tabulate(benefit_user, headers_user))
        else:
            print("Anda belum berlangganan")

    def upgrade_plan(self, new_plan):
        '''
        untuk melakukan upgrade plan

        parameter:
            new_plan (str)
        '''
        #mengecek apakah user sudah berlangganan dan new plan ada di list plan
        if self.current_plan is not None and new_plan in self.list_plan:
            idx_current_plan = self.list_plan.index(self.current_plan)
            idx_new_plan = self.list_plan.index(new_plan)

            #kondisi dimana syarat upgrade plan
            if idx_new_plan > idx_current_plan:
                #do upgrade
                if self.duration_plan > 12:
                    #mendapat diskon
                    total = self.table[-1][idx_new_plan] - (self.table[-1][idx_new_plan] * 0.05)
                else:
                    #harga normal
                    total = self.table[-1][idx_new_plan]

                print(f'Harga upgrade ke {new_plan} adalah Rp. {total}')

            elif idx_new_plan == idx_current_plan:
                print(f'Anda sedang berlangganan {new_plan}')
            else:
                print(f'Anda tidak bisa downgrade ke {new_plan}')
            
            #Update data user new plan
            self.current_plan = new_plan
            for key, value in self.data_user.items():
                if self.username == value[0]:
                    self.data_user[key][1] = new_plan
                    break


        elif new_plan not in self.list_plan:
            print("New Plan tidak tersedia")
        elif self.current_plan is None:
            print("Silahkan berlangganan terlebih dahulu")

    def subs_plan(self, new_plan, kode_referral):
        '''
        untuk subscribe unutk user baru

        parameters:
            -new_plan (str)
            -kode_referral (str)
        '''

        list_code = [row[-1]for row in self.data_user.values()]

        if self.current_plan is None:

            if new_plan in self.list_plan:
                #do subscribre
                self.current_plan = new_plan
                self.duration_plan = 1
                self.kode_refferal = f"{self.username}-123"

                idx_new_plan = self.list_plan.index(new_plan)
                #menampilkan harga
                if kode_referral in list_code:
                    #dapat diskon
                    total = self.table[-1][idx_new_plan] - (self.table[-1][idx_new_plan] * 0.04)
                else:
                    total = self.table[-1][idx_new_plan]
                print(f'Harga yang harus dibayar untuk subs {new_plan} adalah Rp. {total}')

                #tambahan user baru
                last_key = max(self.data_user.keys())
                self.data_user[last_key+1] = [self.username, self.current_plan, self.duration_plan, self.kode_refferal]


            else:
                print("Plan tidak tersedia")
        else:
            print("Anda sudah berlangganan")

