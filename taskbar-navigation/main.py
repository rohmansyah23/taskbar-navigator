import time
import keyboard
import pyautogui
import pygetwindow as gw

# MAP TOMBOL: Alt + Angka akan meniru posisi ke-X di taskbar
# Berdasarkan gambar image_c16198.png:
# 1 = Chrome, 2 = Kotak Ungu 1, 3 = Kotak Ungu 2, dst.
TASKBAR_MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def navigasi_berdasarkan_urutan(posisi_taskbar):
    print(f"Menavigasi ke aplikasi urutan ke-{posisi_taskbar}...")

    # Ambil jendela yang sedang aktif saat ini sebelum tombol ditekan
    jendela_sebelum = gw.getActiveWindow()

    # Lepas tombol alt agar tidak mengganggu shortcut Windows
    keyboard.release("alt")
    time.sleep(0.05)

    # Tekan kombinasi bawaan Windows untuk urutan taskbar
    pyautogui.hotkey("win", str(posisi_taskbar))
    time.sleep(0.2)  # Beri jeda sistem untuk merespons

    # Cek jendela aktif setelah tombol ditekan
    jendela_sesudah = gw.getActiveWindow()

    # LOGIKA ANTI-MENUTUP:
    # Jika jendela sesudah sama dengan sebelum, atau justru jendela aktifnya hilang (jadi desktop/kosong),
    # itu tanda bahwa aplikasi tersebut malah ter-minimize (menutup).
    if (
        jendela_sesudah == jendela_sebelum
        or jendela_sesudah is None
        or jendela_sesudah.title == ""
    ):
        print("Aplikasi terdeteksi meminimalkan diri, membuka kembali...")
        # Tekan sekali lagi untuk memaksanya terbuka di layar utama
        pyautogui.hotkey("win", str(posisi_taskbar))


def buat_hotkey(angka_tombol, posisi_taskbar):
    return lambda: navigasi_berdasarkan_urutan(posisi_taskbar)


# Daftarkan shortcut Alt + 1 sampai Alt + 9
for tombol, posisi in TASKBAR_MAPPING.items():
    keyboard.add_hotkey(f"alt+{tombol}", buat_hotkey(tombol, posisi))

print("=" * 60)
print("Script Urutan Taskbar Otomatis Berjalan (Anti-Minimize)!")
print("Alt+1 = Chrome (Aplikasi pertama setelah folder)")
print("Alt+2 = Aplikasi kedua, dst.")
print("=" * 60)

keyboard.wait()