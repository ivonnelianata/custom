{
    'name': 'perpustakaan',  #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Ivonne',
    'summary': 'Modul Perpustakaan SIB UK Petra', #deskripsi singkat dari modul
    'description': 'Perpustakaan management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di idea/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'],  # list of dependencies, conditioning startup order
    'data': [
        'security/ir.model.access.csv',
        'views/buku_views.xml',
        'views/anggota_views.xml',
        'views/transaksi_views.xml',
        'views/terpinjam_views.xml',
        'views/kategori_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'qweb':[],  #untuk memberi tahu static file, misal CSS
    'demo': [], #demo data (for unit tests)
    'installable': True,
    'auto_install': False,  # indikasi install, saat buat database baru
}