# =========================================
# LATIHAN 1 & 2
# Membuat Class Hero + Interaksi Objek
# =========================================

class Hero:
    # Constructor
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method info
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # Method menyerang
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# -- Main Program --
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)


# =========================================
# LATIHAN 3
# Inheritance (Mage)
# =========================================

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)


# =========================================
# LATIHAN 4
# Encapsulation (Private HP)
# =========================================

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)
hero1.set_hp(-50)
print(hero1.get_hp())

# Percobaan Name Mangling
print(f"Mencoba akses paksa: {hero1._Hero__hp}")


# =========================================
# LATIHAN 5
# Abstraction & Interface
# =========================================

from abc import ABC, abstractmethod

class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()


# =========================================
# LATIHAN 6
# Polymorphism
# =========================================

class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")


print("\n--- PERANG DIMULAI ---")
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Rafaela")
]

for pahlawan in pasukan:
    pahlawan.serang()
