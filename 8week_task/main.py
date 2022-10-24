from cryptography.fernet import Fernet
#new key
# key = Fernet.generate_key()

# with open('mykey.key','wb') as mykey:
#     mykey.write(key)
# ----------------------------------------------
# reading key
# with open('mykey.key','rb') as mykey:
#     key = mykey.read()
# f= Fernet(key)
# ----------------------------------------------
# encrypt
# with open('grades.scv','rb') as original_file:
#     original = original_file.read()
#
# encrypted = f.encrypt(original)
#
# with open('enc_grades.scv','wb') as encrypted_file:
#     encrypted_file.write(encrypted)
# ----------------------------------------------
# decrypt
# with open('enc_grades.scv','rb') as encrypted_file:
#     encrypted = encrypted_file.read()
#
# decrypted = f.decrypt(encrypted)
#
# with open('dec_grades.scv','wb') as decrypted_file:
#     decrypted_file.write(decrypted)