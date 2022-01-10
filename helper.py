def header(title):
    print("-" * 45)
    print("\t\t", title)
    print("-" * 45)

def ubahRamKeMbps(ramInGbps):
    return ramInGbps * 1024

def hitungPetaBit(ram, blok):
    return ram / blok