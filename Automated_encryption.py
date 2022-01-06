from cryptography.fernet import Fernet
import unittest

class Data_Cryptography(unittest.TestCase):

    def test_crypto(self):

        key = b'96383l-ZMT2PBYW0AWTKQMVJpc_-BFwQB4xDvEdvVcg='

        cipher = Fernet(key)

        File_name = input("What is the name of the file: ")

        option = input("Do you want to encrypt or Decrypt? (E/D)")

        with open(File_name,'rb') as ef:
            data = ef.read()
        
        if option == 'E':
            encrypt_data = cipher.encrypt(data)

            with open(File_name + ".encrypted", 'wb') as ef:
                ef.write(encrypt_data)
        
        elif option == 'D':
            decrypt_data = cipher.decrypt(data)

            with open(File_name + ".decrypted", 'wb') as df:
                df.write(decrypt_data)
        
        else:
            print("Invalid input")

if __name__ == '__main__':
    unittest.main()

