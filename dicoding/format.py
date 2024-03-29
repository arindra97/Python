import unittest
 
# class TestStringMethods(unittest.TestCase):
    
#     def test_strip(self):
#         self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
#     def test_isalnum(self):
#         self.assertTrue('c0d1ng'.isalnum())
#         self.assertFalse('c0d!ng'.isalnum())
    
#     def test_index(self):
#         s = 'dicoding'
#         self.assertEqual(s.index('coding'), 2)
#         # cek s.index gagal ketika tidak ditemukan
#         with self.assertRaises(ValueError):
#             s.index('decode')
    
# if __name__ == '__main__':
#     unittest.main()
 
def koneksi_ke_db():
    print('[terhubung ke db]')
def putus_koneksi_db(db):
    print('[tidak terhubung ke db {}]'.format(db))
 
class User:
    username = ''
    aktif = False
    def __init__(self, db, username):  # using db sample
        self.username = username
    def set_aktif(self):
        self.aktif = True
 
# class TestUser(unittest.TestCase):
#     def test_user_default_not_active(self):
#         db = koneksi_ke_db()
#         dicoding = User(db, 'dicoding')
#         self.assertFalse(dicoding.aktif)  # tidak aktif secara default
#         putus_koneksi_db(db)
 
#     def test_user_is_active(self):
#         db = koneksi_ke_db()
#         dicoding = User(db, 'dicoding')
#         dicoding.set_aktif()  # aktifkan user baru
#         self.assertTrue(dicoding.aktif)
#         putus_koneksi_db(db)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, 'dicoding')
 
    def tearDown(self):
        putus_koneksi_db(self.db)
    
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif)  # tidak aktif secara default
 
    def test_user_is_active(self):
        self.dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(self.dicoding.aktif)
 
if __name__ == '__main__':
    unittest.main()