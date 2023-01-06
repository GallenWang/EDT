VERSION = '1.4.8'


print('+----------------------------------------------------------------------------------------------------------------+')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE      DDDDDDDDDDDDDDDDDDDDDD            TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDD          TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDDDD        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD             DDDDDDDD      TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEE                               DDDDDDDD               DDDDDDDD                 TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                 DDDDDDDD               TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                  DDDDDDDD              TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                  DDDDDDDD              TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                 DDDDDDDD               TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD               DDDDDDDD                 TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD             DDDDDDDD                   TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDDDD                     TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDD                       TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE      DDDDDDDDDDDDDDDDDDDDDD                         TTTTTTTTT              |')
print('+----------------------------------------------------------------------------------------------------------------+')
print(f'Encrypt & Decrypt Tool    v{VERSION}')
import time
time.sleep(0.9)



##################################################################################################################################



import os
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3
from Cryptodome.Cipher import ChaCha20
from Cryptodome.Cipher import Salsa20


def print_mode(l, da=None):
    if l == 'l1':
        print('\n\n')
        print('[1]: Encrypt')
        print('[2]: Decrypt')
        print('[3]: Help')
        print('[4]: Info')
        print('[5]: Exit')
    elif l == 'l2':
        print('\n')
        print('[1]: DES')
        print('[2]: 3DES')
        print('[3]: AES (not working)')
        print('[4]: ChaCha20')
        print('[5]: Salsa20')
        print('[6]: Blowfish (not working)')
        print('[7]: Help')
        print('[8]: Info')
        print('[9]: Exit')
    elif l == 'l3':
        print('\n')
        print('[1]: CBC')
        print('[2]: CFB')
        print('[3]: CTR')
        print('[4]: EAX')
        print('[5]: ECB')
        print('[6]: OFB')
        if da == 'd':
            print('[7]: Help')
            print('[8]: Info')
            print('[9]: Exit')
        elif da == 'a':
            print('[7]: CCM')
            print('[8]: GCM')
            print('[9]: OCB')
            print('[10]: SIV')
            print('[11]: Help')
            print('[12]: Info')
            print('[13]: Exit')


loop = True


def info():
    print('\n')
    print('Python 3.9.12')
    print('Author: 和泉かやと')
    print('Date: 2023/01/02')
    print(f'Version: {VERSION}')
    print('https://github.com/GallenWang/EDT')
    print('Thanks for using this tool. If it is helpful to you, please give me the star!')

def help():
    print('''
1. Select mode
    e.g. [1]: Encrypt
         [2]: Decrypt
         [3]: Help
         [4]: Info
         [5]: Exit

         For showing this message, you should type "3".

2. Enter path
    If the file not found, return "Wrong path".

3. Enter key
    If the key is illegal, raise error.

4. Enter iv/nonce
    Some mode does not require iv/nonce.
    If the iv/nonce is illegal, raise error.

5. This tools is not a malware, if your antivirus blocks this tool, you should stop your antivirus.

6. Go to https://github.com/GallenWang/EDT for update and more informations.''')


def get_payload(iv: bool):
    if iv:
        path = input('file path?:')
        key = input('key?:').encode()
        iv = input('iv/nonce?:').encode()
        return [path, key, iv]
    else:
        path = input('file path?:')
        key = input('key?:').encode()
        return [path, key]


def check_path(path: str):
    if not os.path.exists(path):
        print('Wrong path')
        return False
    return True


def check_des_key(key: bytes):
    if len(key) != DES.key_size:
        print(f'Incorrect DES key length ({len(key)} bytes)')
        print(f'Should be {DES.key_size} bytes')
        return False
    return True

def check_3des_key(key: bytes):
    if len(key) not in  DES3.key_size:
        print(f'Incorrect DES key length ({len(key)} bytes)')
        print(f'Should be {DES3.key_size[0]} or {DES3.key_size[1]} bytes')
        return False
    return True


def check_payload_cbc_cfb_ofb(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    c = True
    if len(payload[2]) != 8:
        print(f'Incorrect DES iv length ({len(payload[2])} bytes)')
        print('Should be 8 bytes')
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_ctr(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    c = True
    if len(payload[2]) >= 8:
        print(f'Incorrect DES iv length ({len(payload[2])} bytes)')
        print('Should be smaller 8 bytes')
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_eax_ecb(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    if a and b:
        global loop
        loop = False

def check_payload_salsa20(payload):
    a = check_path(payload[0])
    b = len(payload[1]) in Salsa20.key_size
    c = len(payload[2]) == 8
    if a and b and c:
        global loop
        loop = False
    else:
        if not b:
            print(f'Incorrect Salsa20 key length ({len(payload[1])} bytes)')
            print(f'Should be {Salsa20.key_size[0]} or {Salsa20.key_size[1]} bytes')
        if not c:
            print(f'Incorrect Salsa20 iv length ({len(payload[2])} bytes)')
            print('Should be 8 bytes')

def check_payload_chacha20(payload):
    a = check_path(payload[0])
    b = len(payload[1]) == ChaCha20.key_size
    c = len(payload[2]) in [8, 12, 24]
    if a and b and c:
        global loop
        loop = False
    else:
        if not b:
            print(f'Incorrect ChaCha20 key length ({len(payload[1])} bytes)')
            print(f'Should be {ChaCha20.key_size} bytes')
        if not c:
            print(f'Incorrect ChaCha20 iv length ({len(payload[2])} bytes)')
            print('Should be 8, 12 or 24 bytes')    




from Cryptodome.Util.Padding import pad, unpad

class EncDec:
    def __init__(self, path: str, enc: list, padding=None):
        self.path = path
        self.enc = enc
        self.padding = padding


    def loop_control(self):
        global loop
        loop = True
        print('\nDone!')


    def encrypt(self) -> bytes:
        '''
        `enc`: [enc, enc]
        `padding`: [bool, block_size]
        '''
        with open(self.path, 'rb') as file:
            self.plain = file.read()

        if self.padding == None:
            self.cipher = self.enc[0].encrypt(self.plain)
            assert self.plain == self.enc[1].decrypt(self.cipher)
        else:
            self.cipher = self.enc[0].encrypt(pad(self.plain, self.padding))
            assert self.plain == unpad(self.enc[1].decrypt(self.cipher), self.padding)

        with open(f'{self.path}.enc', 'wb') as file:
            file.write(self.cipher)

        self.loop_control()

        return self.cipher

    def decrypt(self) -> bytes:
        '''
        `enc`: [enc, enc]
        `padding`: [bool, block_size]
        '''
        with open(self.path, 'rb') as file:
            self.cipher = file.read()

        if self.padding == None:
            self.plain = self.enc[0].decrypt(self.cipher)
            assert self.cipher == self.enc[1].encrypt(self.plain)

        else:
            self.plain = unpad(self.enc[0].decrypt(self.cipher), self.padding)
            assert self.cipher == self.enc[1].encrypt(pad(self.plain, self.padding))

        if self.path.endswith('.enc'):
            self.path = self.path[:-3]
        with open(self.path, 'wb') as file:
            file.write(self.plain)
        
        self.loop_control()

        return self.plain



##################################################################################################################################



try:
    while True:
        print_mode('l1')
        mode = input('?:')

        if mode == '1':
            enc_or_dec = 'enc'
        elif mode == '2':
            enc_or_dec = 'dec'
        elif mode in ['3', 'help']:
            help()
            continue
        elif mode == '4' or mode == 'info' or mode == 'version':
            print(mode)
            info()
            continue
        elif mode == '5' or mode == 'exit' or mode == 'leave':
            os._exit(0)

        print_mode('l2')
        mode = input('?:')

        if mode == '1':
            print_mode('l3', 'd')
            mode = input('?:')

            if mode == '1':
                mode = '0'
                # des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2])], padding=DES.block_size)
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()
                    

            elif mode == '2':
                mode = '0'
                # des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '3':
                mode = '0'
                # des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_ctr(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '4':
                mode = '0'
                # des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_eax_ecb(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '5':
                mode = '0'
                # des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload_eax_ecb(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_ECB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_ECB)], padding=DES.block_size)
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '6':
                mode = '0'
                # des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'd')
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode in ['7', 'help']:
                help()

            elif mode in ['8', 'info', 'version']:
                info()

            elif mode in ['9', 'exit', 'leave']:
                break

        elif mode == '2':
            print_mode('l3', 'd')
            mode = input('?:')

            if mode == '1':
                mode = '0'
                # 3des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2])], padding=DES3.block_size)
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '2':
                mode = '0'
                # 3des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '3':
                mode = '0'
                # 3des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_ctr(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '4':
                mode = '0'
                # 3des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_eax_ecb(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '5':
                mode = '0'
                # 3des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload_eax_ecb(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_ECB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_ECB)], padding=DES3.block_size)
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode == '6':
                mode = '0'
                # 3des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload, 'ddd')
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2])])
                if enc_or_dec == 'enc':
                    file.encrypt()
                elif enc_or_dec == 'dec':
                    file.decrypt()

            elif mode in ['7', 'help']:
                help()

            elif mode in ['8', 'info', 'version']:
                info()

            elif mode in ['9', 'exit', 'leave']:
                break

        elif mode == '4':
            mode = '0'
            # chacha20
            while loop:
                payload = get_payload(iv=True)
                check_payload_chacha20(payload)
            file = EncDec(payload[0], [ChaCha20.new(key=payload[1], nonce=payload[2]), ChaCha20.new(key=payload[1], nonce=payload[2])])
            if enc_or_dec == 'enc':
                file.encrypt()
            elif enc_or_dec == 'dec':
                file.decrypt()

        elif mode == '5':
            mode = '0'
            # salsa20
            while loop:
                payload = get_payload(iv=True)
                check_payload_salsa20(payload)
            file = EncDec(payload[0], [Salsa20.new(key=payload[1], nonce=payload[2]), Salsa20.new(key=payload[1], nonce=payload[2])])
            if enc_or_dec == 'enc':
                file.encrypt()
            elif enc_or_dec == 'dec':
                file.decrypt()

        elif mode in ['7', 'help']:
            help()

        elif mode in ['8', 'info', 'version']:
            info()

        elif mode in ['9', 'exit', 'leave']:
            break


except Exception as e:
    print(e)