import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'???' # Haha, you really thought I was gonna give you the key??
iv = hashlib.md5(b"dvCTF").digest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--output-file', type=str)
    args = parser.parse_args()

    print(vars(args))

    with open(args.input_file, 'rb') as input_file:
        contents = input_file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ct = cipher.encrypt(pad(contents, 16))

    if args.output_file is not None:
        with open(args.output_file, 'wb') as output_file:
            output_file.write(ct)
    else:
        with open(args.input_file+'.enc', 'wb') as output_file:
            output_file.write(ct)

if __name__ == '__main__':
    main()
