{
    'name': 'Apo',  #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Ivonne',
    'summary': 'Modul Apo SIB UK Petra', #deskripsi singkat dari modul
    'description': 'Apo management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di idea/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team', 'sale'],  # list of dependencies, conditioning startup order
    'data': [
        'security/ir.model.access.csv',
        'views/kategori_views.xml',
        'views/obat_views.xml',
        'views/cus_views.xml',
        'views/transaksi_views.xml',
        'views/supplier2_views.xml',
        # 'views/sup_views.xml',
        'data/ir_sequence_data.xml',
        'wizard/wiz_apo_transaksi_views.xml',

    ],
    'qweb':[],  #untuk memberi tahu static file, misal CSS
    'demo': [], #demo data (for unit tests)
    'installable': True,
    'auto_install': False,  # indikasi install, saat buat database baru
}