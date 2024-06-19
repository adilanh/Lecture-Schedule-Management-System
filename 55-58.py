

class JadwalKuliahApp:
    def __init__(self, root, manajemen_jadwal):
        self.root = root
        self.manajemen_jadwal = manajemen_jadwal
        self.root.title("Sistem Manajemen Jadwal Kuliah")

        # Set window background color to gray
        self.root.configure(bg="#E0E0E0")

        # Create a style
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#E0E0E0", foreground="black", font=("Arial", 12, "bold"))
        self.style.configure("TEntry", fieldbackground="#FFFFFF", font=("Arial", 12))
        self.style.configure("TButton", background="#BDBDBD", foreground="black", font=("Arial", 12, "normal"))

        # Main frame to hold all widgets
        self.main_frame = ttk.Frame(root, padding=20, style="TFrame", relief=tk.RIDGE)
        self.main_frame.pack()

        # Title label
        self.title_label = ttk.Label(self.main_frame, text="Sistem Manajemen Jadwal Kuliah", style="TLabel")
        self.title_label.pack(pady=10)

        # Frame for input fields
        self.input_frame = ttk.Frame(self.main_frame, padding=10, style="TFrame", relief=tk.RIDGE)
        self.input_frame.pack(side=tk.LEFT, padx=10)

        self.nama_matkul_label = ttk.Label(self.input_frame, text="Nama Mata Kuliah", style="TLabel")
        self.nama_matkul_label.pack(pady=5)
        self.nama_matkul_entry = ttk.Entry(self.input_frame, width=30, style="TEntry")
        self.nama_matkul_entry.pack(pady=5)

        self.hari_label = ttk.Label(self.input_frame, text="Hari", style="TLabel")
        self.hari_label.pack(pady=5)
        self.hari_entry = ttk.Entry(self.input_frame, width=30, style="TEntry")
        self.hari_entry.pack(pady=5)

        self.jam_label = ttk.Label(self.input_frame, text="Jam", style="TLabel")
        self.jam_label.pack(pady=5)
        self.jam_entry = ttk.Entry(self.input_frame, width=30, style="TEntry")
        self.jam_entry.pack(pady=5)

        self.ruang_label = ttk.Label(self.input_frame, text="Ruang", style="TLabel")
        self.ruang_label.pack(pady=5)
        self.ruang_entry = ttk.Entry(self.input_frame, width=30, style="TEntry")
        self.ruang_entry.pack(pady=5)

        self.nama_dosen_label = ttk.Label(self.input_frame, text="Nama Dosen", style="TLabel")
        self.nama_dosen_label.pack(pady=5)
        self.nama_dosen_entry = ttk.Entry(self.input_frame, width=30, style="TEntry")
        self.nama_dosen_entry.pack(pady=5)

        # Frame for buttons
        self.button_frame = ttk.Frame(self.main_frame, padding=10, style="TFrame", relief=tk.RIDGE)
        self.button_frame.pack(side=tk.LEFT, padx=10)

        self.tambah_button = ttk.Button(self.button_frame, text="Tambah Jadwal", command=self.tambah_jadwal, style="TButton")
        self.tambah_button.pack(fill=tk.X, pady=5)

        self.lihat_button = ttk.Button(self.button_frame, text="Lihat Jadwal", command=self.lihat_jadwal, style="TButton")
        self.lihat_button.pack(fill=tk.X, pady=5)

        self.ubah_button = ttk.Button(self.button_frame, text="Ubah Jadwal", command=self.ubah_jadwal, style="TButton")
        self.ubah_button.pack(fill=tk.X, pady=5)

        self.hapus_button = ttk.Button(self.button_frame, text="Hapus Jadwal", command=self.hapus_jadwal, style="TButton")
        self.hapus_button.pack(fill=tk.X, pady=5)

        self.sort_button = ttk.Button(self.button_frame, text="Urutkan Jadwal Berdasarkan Hari", command=self.urutkan_jadwal, style="TButton")
        self.sort_button.pack(fill=tk.X, pady=5)

        self.cari_button = ttk.Button(self.button_frame, text="Cari Jadwal Berdasarkan Nama Matkul", command=self.cari_jadwal, style="TButton")
        self.cari_button.pack(fill=tk.X, pady=5)

        self.import_button = ttk.Button(self.button_frame, text="Import Jadwal dari CSV", command=self.import_jadwal, style="TButton")
        self.import_button.pack(fill=tk.X, pady=5)

    