class katak_zuma :
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        is_active = True
        pass

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        pass

    def tembak(self, warna_sama):
        if {warna_sama >= 2}:
            self.skor += 50
        pass

    def info_status(self):
        print(f"peluru = {self.warna_peluru}")
        print(f"skor =  {self.skor}")
        print(f"status keaktifan = {self.is_active}")
        pass

katak_player = katak_zuma("Hijau")
print("Kondisi awal katak:")
katak_player.info_status()
katak_player.ganti_warna()
katak_player.tembak()
print("Kondisi akhir katak:")
katak_player.info_status()
