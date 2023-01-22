from Lib.Logo.logo import *
fs = FSLogo('./Test/test.png')

if __name__ == '__main__':
    while True:
        fs.pack()
        fs.update()