from hashlib import md5
from base64 import b64encode

from file_manager import FileManager


class Authentication:

    """
    Pokúste sa určiť heslá niekoľkých používateľov systému, z ktorého sa podarilo skopírovať tabuľku s prihlasovacími
    údajmi. Tabuľka v textovej podobe obsahuje prihlasovacie meno, soľ a odtlačok hesla (so soľou).
    Odtlačok sa počíta algoritmom MD5, ktorého výsledok je konvertovaný na String pomocou Base64Encoding.
    """
    def __init__(self):
        self.file_manager = FileManager()
        self.salt: str = "3B0hFRav"
        self.result: str = "b'LebLvqRKivyGxyTe/SLJcw=='"
        # "b'MAah8Dfo+h3kUUcMAsiEKA=='"
        # krajciko:3B0hFRav:LebLvqRKivyGxyTe/SLJcw==
        self.alphabet_test: list = ['a', 'b', 'c']
        self.alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                               'p', 'q', 'r', 'd', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.alphabet_big: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                   'p', 'q', 'r', 'd', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                                   'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        # data
        self.shadow: list = self.file_manager.load_file()

    def crypt(self, passwd, salt):
        m = md5()
        m.update((passwd.encode('utf-8')))
        m.update((salt.encode('utf-8')))
        return b64encode(m.digest())

    """
    krstné mená podľa slovenského kalendára alebo ich zdrobneniny, pričom môžu obsahovať najviac jedno veľké písmeno 
    kdekoľvek v slove (napríklad zuzana, Zuzana, zuZana, zUzka, zuzkA, ...),
    """
    def password1(self) -> str:
        names: list = self.file_manager.load_names()

        for name in names:
            for i in range(len(name)):
                name = name[:i] + name[i].upper() + name[i + 1:]
                temp = str(self.crypt(name, self.salt))
                if self.result == temp:
                    print(name)
                    return name
                name = name.lower()

        return None

    """
    heslá s počtom znakov 6 alebo 7, pozostávajúce len z malých písmen (napríklad asdfgh, utywmk, klnrtus, ...),
    """
    def password2(self) -> str:
        password: str = "aaaaaaa"

        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                for k in range(len(self.alphabet)):
                    for l in range(len(self.alphabet)):
                        for m in range(len(self.alphabet)):
                            for n in range(len(self.alphabet)):
                                for o in range(len(self.alphabet)):
                                    temp = str(self.crypt(password, self.salt))
                                    if self.result == temp:
                                        print(password)
                                        return password
                                    temp = str(self.crypt(password[:6], self.salt))
                                    if self.result == temp:
                                        print(password[:6])
                                        return password[:6]
                                    password = password[:0] + self.alphabet[o] + password[1:]
                                    # print(password)
                                if n + 1 < len(self.alphabet):
                                    password = password[:1] + self.alphabet[n + 1] + password[2:]
                                else:
                                    password = password[:1] + self.alphabet[n] + password[2:]

                            if m + 1 < len(self.alphabet):
                                password = password[:2] + self.alphabet[m + 1] + password[3:]
                            else:
                                password = password[:2] + self.alphabet[m] + password[3:]

                        if l + 1 < len(self.alphabet):
                            password = password[:3] + self.alphabet[l + 1] + password[4:]
                        else:
                            password = password[:3] + self.alphabet[l] + password[4:]

                    if k + 1 < len(self.alphabet):
                        password = password[:4] + self.alphabet[k + 1] + password[5:]
                    else:
                        password = password[:4] + self.alphabet[k] + password[5:]

                if j + 1 < len(self.alphabet):
                    password = password[:5] + self.alphabet[j + 1] + password[6:]
                else:
                    password = password[:5] + self.alphabet[j] + password[6:]

            if i + 1 < len(self.alphabet):
                password = password[:6] + self.alphabet[i + 1] + password[7:]
            else:
                password = password[:6] + self.alphabet[i] + password[7:]

        return None

    """
    heslá s malým počtom znakov 4 alebo 5 pozostávajúce z malých a veľkých písmen a číslic (napríklad w7H5, WnU8a, ...)
    """
    def password3(self) -> str:
        password: str = "aaaaa"

        for k in range(len(self.alphabet_big)):
            for l in range(len(self.alphabet_big)):
                for m in range(len(self.alphabet_big)):
                    for n in range(len(self.alphabet_big)):
                        for o in range(len(self.alphabet_big)):
                            temp = str(self.crypt(password, self.salt))
                            if self.result == temp:
                                print(password)
                                return password
                            temp = str(self.crypt(password[:4], self.salt))
                            if self.result == temp:
                                print(password[:4])
                                return password[:4]
                            password = password[:0] + self.alphabet_big[o] + password[1:]
                            # print(password)
                        if n + 1 < len(self.alphabet_big):
                            password = password[:1] + self.alphabet_big[n + 1] + password[2:]
                        else:
                            password = password[:1] + self.alphabet_big[n] + password[2:]

                    if m + 1 < len(self.alphabet_big):
                        password = password[:2] + self.alphabet_big[m + 1] + password[3:]
                    else:
                        password = password[:2] + self.alphabet_big[m] + password[3:]

                if l + 1 < len(self.alphabet_big):
                    password = password[:3] + self.alphabet_big[l + 1] + password[4:]
                else:
                    password = password[:3] + self.alphabet_big[l] + password[4:]

            if k + 1 < len(self.alphabet_big):
                password = password[:4] + self.alphabet_big[k + 1] + password[5:]
            else:
                password = password[:4] + self.alphabet_big[k] + password[5:]

        return None
