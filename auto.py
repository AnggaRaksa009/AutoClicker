import pyautogui
import time
import keyboard

# Fungsi untuk mendapatkan posisi kursor saat ini
def get_cursor_position():
    return pyautogui.position()

# Fungsi untuk mengklik pada posisi yang ditentukan
def click_position(x, y):
    pyautogui.click(x, y)

# Fungsi yang akan dipanggil saat tombol ditekan
def on_key_press(event):
    global is_paused
    global x, y
    global click_points
    global current_point_index

    if event.name == 'insert':
        # Mulai auto clicker saat tombol "insert" ditekan
        print("Auto clicker dimulai.")
        return True  # Mengembalikan True untuk memulai auto clicker

    if event.name == 'delete':
        # Hentikan program saat tombol "delete" ditekan
        print("Auto clicker dihentikan.")
        return False  # Mengembalikan False untuk menghentikan auto clicker

    if event.name == 'space':
        if is_paused:
            # Menghentikan penundaan saat tombol "space" ditekan lagi
            is_paused = False
            print("Auto clicker dilanjutkan.")
        else:
            # Menjeda auto clicker saat tombol "space" ditekan
            is_paused = True
            print("Auto clicker dijeda.")

    if event.name == '0':
        # Tambahkan titik klik saat tombol "0" ditekan
        click_points.append(get_cursor_position())
        print("Titik klik baru ditambahkan.")

# Mendaftarkan fungsi sebagai penangan acara saat tombol ditekan
keyboard.on_press(on_key_press)

# Mendapatkan posisi awal kursor
x, y = get_cursor_position()

is_auto_clicking = False
is_paused = False
click_points = []  # Menyimpan titik-titik klik
current_point_index = 0  # Indeks titik klik saat ini

# Loop tunggu sampai tombol "insert" ditekan
keyboard.wait('insert')
is_auto_clicking = True

# Loop utama untuk melakukan klik berulang kali
while is_auto_clicking:
    if not is_paused:
        # Mendapatkan posisi kursor saat ini
        current_x, current_y = get_cursor_position()

        # Memeriksa apakah posisi kursor berubah
        if current_x != x or current_y != y:
            # Memperbarui posisi auto click
            x, y = current_x, current_y

        # Mendapatkan titik klik saat ini
        current_point = click_points[current_point_index]

        # Melakukan klik pada posisi titik klik saat ini
        click_position(current_point[0], current_point[1])

        # Menambahkan indeks titik saat ini untuk beralih ke titik berikutnya
        current_point_index += 1

        # Jika mencapai indeks terakhir, kembali ke indeks awal
        if current_point_index >= len(click_points):
            current_point_index = 0

    # Jeda antara klik
    time.sleep(0)

    # Cek apakah tombol "delete" ditekan untuk menghentikan auto clicker
    if keyboard.is_pressed('delete'):
        is_auto_clicking = False

print("Program selesai.")
