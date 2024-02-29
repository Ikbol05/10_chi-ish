
# 1 chi masala

# def file_suz(file_name, suz):
#     with  open(file_name.txt, mode="r") as new_file:
#         natija = new_file.read().split()
#         natija2 = natija.count(suz)
#         return "Takrorlash soni", natija2

#=----------------------------------------------------------------------------------------------------------------

# 2 chi masala

# def dasturni_bajar(fayl_nomi):
#     try:
#         with open(fayl_nomi, 'r') as fayl:
#             matn = fayl.read()
#             harflar_soni = sum(1 for harf in matn if harf.isalpha())
#             sozlar_soni = len(matn.split())
#             qatorlar_soni = len(matn.splitlines())
#
#             return harflar_soni, sozlar_soni, qatorlar_soni
#     except FileNotFoundError:
#         return 0, 0, 0
#

# fayl_nomi = "matn_fayli.txt"
#
#
# harflar, sozlar, qatorlar = dasturni_bajar(fayl_nomi)
#
# # Natijalarni chiqarish
# print(f"Lotin harflari soni: {harflar}")
# print(f"Fayldagi so'zlar soni: {sozlar}")
# print(f"Fayldagi gatorlar soni: {qatorlar}")

#=----------------------------------------------------------------------------------------------------------------

# 3 chi masala

# def sortirovka_va_chiqarish(fayl_nomi):
#     try:
#         with open(fayl_nomi, 'r') as fayl:
#             gatorlar = fayl.readlines()
#             sozlar = []
#
#             for gator in gatorlar:
#                 sozlar.extend(gator.split())
#
#             sozlar = list(set(sozlar))
#             sozlar.sort()
#
#             for soz in sozlar:
#                 print(soz)
#
#     except FileNotFoundError:
#         print("Fayl topilmadi.")
#
# fayl_nomi = "bobur.txt"
#
# sortirovka_va_chiqarish(fayl_nomi)

#=----------------------------------------------------------------------------------------------------------------

# 4 chi misol

def read_lines(line, file):
    if not isinstance(line, int) or line <= 0:
        return "Musbat butun son kiritilishi kerak."

    try:
        with open(file, 'r') as fayl:
            gatorlar = fayl.readlines()

            if line <= len(gatorlar):
                return gatorlar[line - 1]
            else:
                return f"{line}-chi gator mavjud emas. Faylda {len(gatorlar)} gator mavjud."
    except FileNotFoundError:
        return "Fayl topilmadi."


gator_raqami = 3
fayl_nomi = "matn_fayli.txt"
natija = read_lines(gator_raqami, fayl_nomi)
print(f"{gator_raqami}-chi gator:\n{natija}")

#=----------------------------------------------------------------------------------------------------------------

# 5 chi misol























