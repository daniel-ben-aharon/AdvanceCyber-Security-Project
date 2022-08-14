import hashlib
import os
from tkinter import *
from faker import Faker
import requests
from cryptography.fernet import Fernet
import socket
import sys
import threading
from threading import *

'''
Written By:
# Moscovitz Ori
# Spector Shaked
# Moallim John
# Ben Aharon Daniel
'''
names = 'Project By:\n Moscovitz Ori, Spector Shaked, Moallim John and Ben Aharon Daniel'


# returns long string as a readable string
def OrganizeLongString(s):
    split_strings = []
    n = 30
    for index in range(0, len(s), n):
        split_strings.append(s[index: index + n])
    final_text = ""
    for elm in split_strings:
        final_text += f'{elm}\n'
    return final_text


# slice a long list to sub-lists containing n elements
def SliceList(l, n):
    if len(l) // n != 0:
        return [l[i::n] for i in range(n)]
    return [l]


###############################
#      MAIN FUNCTIONS         #
###############################
# destroy a window
def ClearFrame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


# Adds menu options
def AddMainButtons(frame):
    Button(frame, text='Gen Fake', command=lambda: GenFakeWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=0)
    Button(frame, text='URL Requests', command=lambda: GenUrlReqWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=1)
    Button(frame, text='Encrypt String', command=lambda: HashEncryptWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=2)
    Button(frame, text='Caesar Encrypt', command=lambda: CaesarEncryptWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=3)
    Button(frame, text='Vigenere Encrypt', command=lambda: VigenereEncryptWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=4)
    Button(frame, text='MSSP', command=lambda: MSSPWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=5)
    Button(frame, text='DDOS', command=lambda: DDOSWin(root, frame),
           activebackground='steelblue', activeforeground="white").grid(row=1, column=6)


# initialize main window
def InitMainWin(root):
    ClearFrame(root)
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')

    mainFrame = Frame(root, bd=10)
    mainFrame.grid()
    upperFrame = Frame(root, bd=10)
    upperFrame.grid(row=0, column=0)

    # Label of project collaborators
    Label(upperFrame, text=names, font=("Gisha bold", 12), bg='steelblue').grid(row=0, column=0)
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    # Adding all options to menu
    AddMainButtons(lowerFrame)

    root.title('Final Project in Advanced Security')
    root.mainloop()


###############################
#      FAKE DATA FUNCTIONS    #
###############################
# prints the generated fake name in a certain language to a label
def FakeName(lan_var, fake_name_label, fake_address_label):
    # maps each value of lan_var to a corresponding lan option
    lan_dict = {
        0: "en",
        1: "it",
        2: "he",
        3: "ja"
    }

    # resets fake address label
    fake_address_label.config(text="")

    # generates new fake name
    fake = Faker(lan_dict[lan_var.get()])
    fake_name = fake.name()
    fake_name_label.config(text=fake_name)


# prints the generated fake name in a certain language to a label
def FakeAddress(lan_var, fake_address_label, fake_name_label):
    # maps each value of lan_var to a corresponding lan option
    lan_dict = {
        0: "en",
        1: "it",
        2: "he",
        3: "ja"
    }

    # resets fake name label
    fake_name_label.config(text="")

    # generates new fake address
    fake = Faker(lan_dict[lan_var.get()])
    fake_address = fake.address()
    fake_address_label.config(text=fake_address)


def AddLanguageRadioBtn(lowerFrame, lan_var):
    b1 = Radiobutton(lowerFrame, text="English", variable=lan_var, value=0, font=("Gisha bold", 12), pady=5)
    b1.grid(row=2, column=0)

    b2 = Radiobutton(lowerFrame, text="Italian", variable=lan_var, value=1, font=("Gisha bold", 12), pady=5)
    b2.grid(row=2, column=1)

    b3 = Radiobutton(lowerFrame, text="Hebrew", variable=lan_var, value=2, font=("Gisha bold", 12), pady=5)
    b3.grid(row=2, column=2)

    b4 = Radiobutton(lowerFrame, text="Japanese", variable=lan_var, value=3, font=("Gisha bold", 12), pady=5)
    b4.grid(row=2, column=3)


# creates fake data using Faker Library
def GenFakeWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    topFrame = Frame(lowerFrame, bd=10)
    topFrame.grid(row=0)
    bottomFrame = Frame(lowerFrame, bd=10)
    bottomFrame.grid(row=1)

    backBtn = Button(topFrame, text="\u27F5", font=("Gisha bold", 10), width=10, command=lambda: InitMainWin(root))
    backBtn.grid(row=0, column=0, columnspan=4)

    Label(topFrame, text='Choose Language For The Generated Data').grid(row=1, column=0, columnspan=4)

    fake_name_label = Label(bottomFrame)
    fake_name_label.grid(row=4, column=0, columnspan=2)
    fake_address_label = Label(bottomFrame)
    fake_address_label.grid(row=4, column=2, columnspan=2)

    # 0,1,2,3 for English, Italian, Hebrew, Japanese
    lan_var = IntVar()

    AddLanguageRadioBtn(topFrame, lan_var)
    # English set as default
    lan_var.set(0)

    # buttons that'll generate the fake name or fake address of a given language set by lan_var
    b1 = Button(topFrame, text='Fake Name', activebackground='steelblue', command=lambda: FakeName(lan_var, fake_name_label, fake_address_label))
    b1.grid(row=3, column=0, columnspan=2)
    b2 = Button(topFrame, text='Fake Address', activebackground='steelblue', command=lambda: FakeAddress(lan_var, fake_address_label, fake_name_label))
    b2.grid(row=3, column=2, columnspan=2)


###############################
#    URL REQUESTS FUNCTIONS   #
###############################
# if exists, returns the content of valid url, ow returns -1
def ValidateURL(url):
    try:
        req = requests.get(url)
        return req.text
    except requests.exceptions.MissingSchema:
        return -1


# displays content of url given from user, and occurrences of a given word in that content
def DisplayResults(root, frame, url_text, occur_arr, word):
    backBtn = Button(frame, text="Back", justify="left", width=20, command=lambda: GenUrlReqWin(root, frame))
    backBtn.grid(row=1, column=0, columnspan=2)
    if len(occur_arr) != 0:
        occur_arr = SliceList(occur_arr, 10)

    occur_str = []

    # converts occur_arr from list of int to a list of str
    for sublist in occur_arr:
        occur_str.append("\n")
        for elm in sublist:
            occur_str.append(f'{str(elm)},')

    # creates string of search word locations in the source code
    occur_str = "".join(occur_str)

    if occur_str != "" and len(occur_arr) != 0:
        results = Label(frame, text=f"\"{word}\" has been found in position: {occur_str}", font=('Gisha', 10, 'bold'))
    else:
        results = Label(frame, text=f"\"{word}\" has not been found in doc.", font=('Gisha', 10, 'bold'),
                        foreground="red")
    results.grid(row=5, column=0, columnspan=2)

    Label(frame, text="<Scroll for viewing>", foreground="#4d4d4d", font=('Gisha', 10, 'bold')).grid(row=6, column=0,
                                                                                                     columnspan=2)
    text = Text(frame, width=52)
    text.insert(END, url_text)
    text.grid(row=7, column=0, columnspan=2)
    text.configure(state='disabled')


# validates and presents source code and word locations in the code for url, word given from user
def URL_Requests(root, lowerFrame, url, word, err_label):
    if url == "" or word == "":
        err_label.config(text="All fields must be filled")
    else:
        url_text = ValidateURL(url)
        # url is valid
        if url_text != -1:
            occurrences = []
            for i in range(0, len(url_text)):
                w_occur = url_text.find(word, i, i + len(word))
                if w_occur != -1:
                    occurrences.append(w_occur)
                    i += len(word)
            ClearFrame(lowerFrame)
            # print it in a scroll bar view
            DisplayResults(root, lowerFrame, url_text, occurrences, word)


# the creation of URL requests window
def GenUrlReqWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=2, column=0)

    # getting url from user
    Label(lowerFrame, text="Enter a valid URL", font=("Gisha bold", 12)).grid(row=2, column=0)
    eURL = Entry(lowerFrame, bd=2)
    eURL.grid(row=2, column=1)

    # getting a search work from user
    Label(lowerFrame, text="Enter a search word", font=("Gisha bold", 12)).grid(row=3, column=0)
    wURL = Entry(lowerFrame, bd=2)
    wURL.grid(row=3, column=1)

    # validates and presents source code and word locations in the code for url, word given from user
    goBtn = Button(lowerFrame, text="Go", borderwidth=2, width=5, activebackground="black", activeforeground="white",
                   command=lambda: URL_Requests(root, lowerFrame, eURL.get(), wURL.get(), err_label))
    goBtn.grid(row=1, column=1, columnspan=1)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: InitMainWin(root))
    backBtn.grid(row=1, column=0, columnspan=1)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")
    err_label.grid(row=4, column=0, columnspan=2)


###############################
# Encrypting String FUNCTIONS #
###############################
# if mode is 0, no mode was set, 1 is sha256, 2 fernet
def HashEncrypt(mode, text, err_label, cipher_label):
    if mode == "0":
        err_label.config(text="Mode of encryption wasn't set")

    elif text == "":
        err_label.config(text="No text was entered")
        cipher_label.config(text="")

    else:
        err_label.config(text="")
        # SHA-256 bit encryption
        if mode == "1":
            cipher_text = hashlib.sha256(text.encode()).hexdigest()
            cipher_text = OrganizeLongString(cipher_text)
            cipher_label.config(text=f'The encrypted text:\n{cipher_text}')
        else:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            cipher_text = cipher_suite.encrypt(text.encode())
            cipher_text = OrganizeLongString(cipher_text)
            cipher_label.config(text=f'The encrypted text:\n{cipher_text}')


# the creation of URL requests window
def HashEncryptWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    # 0 when not set, 1 for sha256, 2 for fernet
    mode_var = IntVar()

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: InitMainWin(root))
    backBtn.grid(row=2, column=0, columnspan=1)

    # getting url from user
    Label(lowerFrame, text="Enter a string to encrypt", font=("Gisha bold", 12)) \
        .grid(row=3, column=0)

    str_to_encrypt = Entry(lowerFrame, bd=2)
    str_to_encrypt.grid(row=3, column=1)

    Label(lowerFrame, text="Choose mode of encryption", font=("Gisha bold", 12), pady=5) \
        .grid(row=4, column=0, columnspan=2)

    Radiobutton(lowerFrame, text="SHA-256", variable=mode_var, value=1, font=("Gisha bold", 12), pady=5) \
        .grid(row=5, column=0, columnspan=2)

    Radiobutton(lowerFrame, text="Fernet", variable=mode_var, value=2, font=("Gisha bold", 12)) \
        .grid(row=6, column=0, columnspan=2)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")
    err_label.grid(row=7, column=0, columnspan=2)

    cipher_label = Label(lowerFrame, font=("Gisha bold", 12))
    cipher_label.grid(row=8, column=0, columnspan=2)

    goBtn = Button(lowerFrame, text="Go", borderwidth=2, width=5, activebackground="black", activeforeground="white",
                   command=lambda: HashEncrypt(str(mode_var.get()), str_to_encrypt.get(), err_label, cipher_label))
    goBtn.grid(row=2, column=1, columnspan=1)


###############################
# Caesar Encryption FUNCTIONS #
###############################
def AttackCaesarEncrypt(cipher):
    key = 0
    results = []
    for i in range(26):
        results.append(CaesarDecrypt(cipher, key))
        key += 1
    return results


def AttackCaesarEncryptWin(root, lowerFrame, cipher):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    results_table = AttackCaesarEncrypt(cipher)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: CaesarEncryptWin(root, lowerFrame))
    backBtn.grid(row=1, column=0, columnspan=2)

    Label(lowerFrame, width=20, text="Text", fg='blue', font=('Gisha', 12, 'bold')).grid(row=2, column=0)
    Label(lowerFrame, width=20, text="Offset", fg='blue', font=('Gisha', 12, 'bold')).grid(row=2, column=1)

    for i in range(len(results_table)):
        Label(lowerFrame, width=20, text=f'{results_table[i]}').grid(row=i + 3, column=0)
        Label(lowerFrame, width=20, text=f'{i}').grid(row=i + 3, column=1)


def CaesarDecrypt(text, key):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            # chr is to turn int to char by ASCII table; ord is to do the opposite
            # 26- letters in English alphabet; 65- ASCII value of 'A', 97 -ASCII value of 'a'
            result += chr((ord(char) - key - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result


def CaesarEncrypt(root, lowerFrame, text, key, err_label, cipher_label):
    if text == "" or key == "":
        err_label.config(text="Must enter text to encrypt & and a key")
        cipher_label.config(text="")
    elif not key.isnumeric():
        err_label.config(text="Key must be numeric")
        cipher_label.config(text="")
    else:
        err_label.config(text="")
        cipher_text = ""
        # traverse text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters
            if char.isupper():
                cipher_text += chr((ord(char) + int(key) - 65) % 26 + 65)
            # Encrypt lowercase characters
            else:
                cipher_text += chr((ord(char) + int(key) - 97) % 26 + 97)
        cipher_text_org = OrganizeLongString(cipher_text)
        cipher_label.config(text=f'The encrypted text:\n{cipher_text_org}')

        attackCipherBtn = Button(lowerFrame, text="Show Offset Table", borderwidth=2, width=20,
                                 activebackground="black", activeforeground="white",
                                 command=lambda: AttackCaesarEncryptWin(root, lowerFrame, cipher_text))
        attackCipherBtn.grid(row=9, column=0, columnspan=2)


def CaesarEncryptWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: InitMainWin(root))
    backBtn.grid(row=2, column=0, columnspan=1)

    # getting url from user
    Label(lowerFrame, text="Enter a string to encrypt", font=("Gisha bold", 12)) \
        .grid(row=3, column=0)

    str_to_encrypt = Entry(lowerFrame, bd=2)
    str_to_encrypt.grid(row=3, column=1)

    # getting url from user
    Label(lowerFrame, text="Enter a key for encryption", font=("Gisha bold", 12)) \
        .grid(row=4, column=0)

    key = Entry(lowerFrame, bd=2)
    key.grid(row=4, column=1)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")
    err_label.grid(row=7, column=0, columnspan=2)

    cipher_label = Label(lowerFrame, font=("Gisha bold", 12))
    cipher_label.grid(row=8, column=0, columnspan=2)

    goBtn = Button(lowerFrame, text="Go", borderwidth=2, width=5, activebackground="black", activeforeground="white",
                   command=lambda: CaesarEncrypt(root, lowerFrame, str_to_encrypt.get(), key.get(), err_label,
                                                 cipher_label))
    goBtn.grid(row=2, column=1, columnspan=1)


#################################
# Vigenere Encryption FUNCTIONS #
#################################

def AttackVigenereEncrypt(cipher):
    key = 0
    jump = 0
    results = []
    offset_res = []

    # for each offset
    for i in range(26):
        # for current offset and each jump
        for j in range(26):
            results.append(VigenereDecrypt(cipher, i, j))
            jump += 1
        key += 1
    for i in range(0, len(results), 26):
        offset_res.append(results[i:i + 26])
    print(f'offset_res:     {offset_res}')
    return offset_res


def AttackVigenereEncryptWin(root, lowerFrame, cipher):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    results_table = AttackVigenereEncrypt(cipher)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: VigenereEncryptWin(root, lowerFrame))
    backBtn.grid(row=1, column=0, columnspan=2)

    final_text = f"Text\t\t\tOffset\t\t   Jump\n"

    # build output string to present
    # i is for each offset
    for i in range(26):
        # j for each jump
        for j in range(26):
            final_text = final_text + f'{results_table[i][j]}\t\t\t  {i}\t\t    {j}\n'

    text = Text(lowerFrame, width=52)
    text.insert(END, final_text)

    text.grid(row=2, column=0, columnspan=2)
    text.configure(state='disabled')


def VigenereEncrypt(root, lowerFrame, text, key, jump, err_label, cipher_label):
    if text == "" or key == "":
        err_label.config(text="Must enter text to encrypt & and a key")
        cipher_label.config(text="")
    elif not key.isnumeric() or not jump.isnumeric():
        err_label.config(text="Key and jump must be numeric")
        cipher_label.config(text="")
    else:
        err_label.config(text="")
        cipher_text = ""
        # traverse text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters
            if char.isupper():
                cipher_text += chr((ord(char) + int(key) + (int(jump) * i) - 65) % 26 + 65)
            # Encrypt lowercase characters
            else:
                cipher_text += chr((ord(char) + int(key) + (int(jump) * i) - 97) % 26 + 97)

        cipher_text_org = OrganizeLongString(cipher_text)

        cipher_label.config(text=f'The encrypted text:\n{cipher_text_org}')

        attackVigenereBtn = Button(lowerFrame, text="Show Offset Table", borderwidth=2, width=20,
                                   activebackground="black", activeforeground="white",
                                   command=lambda: AttackVigenereEncryptWin(root, lowerFrame, cipher_text))
        attackVigenereBtn.grid(row=9, column=0, columnspan=2)


# The only difference in decrypt is - (minus) instead of + (plus) of the key
def VigenereDecrypt(text, key, jump):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - key - (jump * i) - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - key - (jump * i) - 97) % 26 + 97)
    return result


def VigenereEncryptWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: InitMainWin(root))
    backBtn.grid(row=2, column=0, columnspan=1)

    # getting url from user
    Label(lowerFrame, text="Enter a string to encrypt", font=("Gisha bold", 12)) \
        .grid(row=3, column=0)

    str_to_encrypt = Entry(lowerFrame, bd=2)
    str_to_encrypt.grid(row=3, column=1)

    # getting url from user
    Label(lowerFrame, text="Enter a key for encryption", font=("Gisha bold", 12)) \
        .grid(row=4, column=0)

    key = Entry(lowerFrame, bd=2)
    key.grid(row=4, column=1)

    # getting url from user
    Label(lowerFrame, text="Enter a jump number", font=("Gisha bold", 12)) \
        .grid(row=5, column=0)

    jump = Entry(lowerFrame, bd=2)
    jump.grid(row=5, column=1)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")
    err_label.grid(row=7, column=0, columnspan=2)

    cipher_label = Label(lowerFrame, font=("Gisha bold", 12))
    cipher_label.grid(row=8, column=0, columnspan=2)

    goBtn = Button(lowerFrame, text="Go", borderwidth=2, width=5, activebackground="black", activeforeground="white",
                   command=lambda: VigenereEncrypt(root, lowerFrame, str_to_encrypt.get(), key.get(), jump.get(),
                                                   err_label,
                                                   cipher_label))
    goBtn.grid(row=2, column=1, columnspan=1)


#################################
#       MSSP FUNCTIONS          #
#################################
#     strArr -
def CalcSubsetSum(nums, i, sum, strArr):
    res = False
    if sum == 0:
        res = True
    elif i >= len(nums):
        res = False
    else:
        res = CalcSubsetSum(nums, i + 1, sum - nums[i], strArr + str(nums[i]) + " ") or CalcSubsetSum(nums, i + 1, sum,
                                                                                                      strArr)
    return res


# surface function for i=0  (i is not input of the problem)
# parameters:
#     nums - array elements
#     sum  - require sum to create from nums
def CalcSubsetSumOver(nums, sum):
    return CalcSubsetSum(nums, 0, sum, "")


# The actual operation of MSSP
def MSSPFunction(text, n, m, d):
    # separate text into groups of strings (concat array elements)
    chunks = [text[(i * m * d):(m * d * (i + 1))] for i in range(0, n)]
    # create arrays with elements
    arrays = [[int(x[i:i + d]) for i in range(0, len(x), d)] for x in chunks]
    # array elements are sums of each array in arrays
    sums = [sum(arr) for arr in arrays]
    # array of minimum arrays elements
    minimum = [min(val) for val in arrays]
    s_start = max(minimum)
    s_max = min(sums)

    #  finding the cipher_text  (common sum)
    for i in range(s_start, s_max):
        ans = [CalcSubsetSumOver(x, i) for x in arrays]
        if all(ans):
            # return cipher_text - common sum in arrays
            return s_start
        else:
            s_start += 1


# Updating results in MSSP win according to current parameters
def MSSP(input_str, n, d, m, err_label, result_label):
    # validate all parameters {input_str, n, d, m} are numeric
    if input_str == "" or n == "" or d == "" or m == "":
        result_label.config(text='')
        err_label.config(text="all inputs must be entered")

    # validate all parameters {input_str, n, d, m} are numeric
    elif not input_str.isnumeric() or not n.isnumeric() or not d.isnumeric() or not m.isnumeric():
        result_label.config(text='')
        err_label.config(text="all inputs must be numeric")

    else:
        n = int(n)
        d = int(d)
        m = (len(input_str) // n) // d
        result = MSSPFunction(input_str, n, m, d)
        if result is None:
            result_label.config(text=f'Cannot compute result from parameters')
        else:
            result_label.config(text=f'Result is: {result}')


def MSSPWin(root, lowerFrame):
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14), width=10,
                     command=lambda: InitMainWin(root))
    backBtn.grid(row=2, column=0, columnspan=1)

    # getting string from user
    Label(lowerFrame, text="Enter a string of digits", font=("Gisha bold", 12)) \
        .grid(row=3, column=0)

    input_str = Entry(lowerFrame, bd=2)
    input_str.grid(row=3, column=1)

    # getting parameters from user
    Label(lowerFrame, text="Enter amount sub arrays {N}", font=("Gisha bold", 12)) \
        .grid(row=4, column=0)

    n = Entry(lowerFrame, bd=2)
    n.grid(row=4, column=1)

    Label(lowerFrame, text="Enter amount of items in each array {D}", font=("Gisha bold", 12)) \
        .grid(row=5, column=0)

    d = Entry(lowerFrame, bd=2)
    d.grid(row=5, column=1)

    Label(lowerFrame, text="Enter amount of digits for each item {M}", font=("Gisha bold", 12)) \
        .grid(row=6, column=0)

    m = Entry(lowerFrame, bd=2)
    m.grid(row=6, column=1)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")
    err_label.grid(row=7, column=0, columnspan=2)

    result_label = Label(lowerFrame, font=("Gisha bold", 12))
    result_label.grid(row=8, column=0, columnspan=2)

    goBtn = Button(lowerFrame, text="Go", borderwidth=2, width=5, activebackground="black", activeforeground="white",
                   command=lambda: MSSP(input_str.get(), n.get(), d.get(), m.get(), err_label, result_label))
    goBtn.grid(row=2, column=1, columnspan=1)


#################################
#       DDOS FUNCTIONS          #
#################################
def Reset_Winsock():
    os.system('cmd /k "netsh winsock reset"')
    path = r'c:\resetlog.txt'
    cmd = f'netsh int ip reset {path}'
    os.system(f'cmd /k {cmd}')


# for it to work, run PYCHARM in ADMINISTRATOR mode
def RestartDDOS(root, lowerFrame):
    # Clear sockets in use for new session
    winsock_thread = Thread(target=Reset_Winsock)
    winsock_thread.start()
    # rerun the ddos window
    DDOSWin(root, lowerFrame)


def AttackServer(ip, port, msg, thread_id, output):
    # Create a TCP/IP socket
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Connect the socket to the port where the server is listening
    server_address = (ip, port)

    text = f'{sys.stderr} connecting to {server_address[0]} port {server_address[1]} \n'
    output.insert(END, text)

    sock.connect(server_address)

    try:
        # Send data
        threadmsg = 'Thread-', thread_id, ':', msg
        message = str.encode(str(threadmsg))

        text = sys.stderr, 'thread-', thread_id, 'sending "%s"' % message, '\n'
        output.insert(END, text)

        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)

            text = sys.stderr, 'received "%s"' % data, '\n'
            output.insert(END, text)

        # output.configure(state='disabled')

    finally:
        output.insert(END, f'{sys.stderr} closing socket\n')
        sock.close()


def Client(threads_amount, attack_interval, ip, port, msg, output):
    class th(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            output.insert(END, f'Starting {self.name}\n')
            AttackServer(ip, port, msg, self.threadID, output)
            output.insert(END, f'Exiting {self.name}\n')

    threads = []
    # Create new threads
    for i in range(threads_amount):
        threads.append(th(i, f'Thread-{i}', i))

    threads = tuple(threads)

    # Start each thread
    for i in range(threads_amount):
        threads[i].start()

    # Run each threads infinite times
    for j in range(len(threads)):
        for i in range(attack_interval):
            threads[j].run()

    output.insert(END, f'Exiting Main Thread\n')


# Starts client ddos attack on server
def StartClientProcess(root, lowerFrame, client_thread, btn):
    # Create a TCP/IP socket
    client_thread.start()

    btn.configure(text="Restart", background="red", foreground="white",
                  command=lambda: RestartDDOS(root, lowerFrame))


def PrintConnectionMsg(output, text):
    output.insert(END, text)


def ConnectServer(sock):
    while True:
        # Wait for a connection
        print(f'{sys.stderr} waiting for a connection \n')
        connection, client_address = sock.accept()
        try:
            print(sys.stderr, 'connection from', client_address, '\n')
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print(sys.stderr, 'received "%s"' % data, '\n')
                if data:
                    print(sys.stderr, 'sending data back to the client', '\n')
                    connection.sendall(data)
                else:
                    print(sys.stderr, 'no more data from', client_address, '\n')
                    break
        finally:
            # Clean up the connection
            connection.close()


def InitSocket(ip, port, output):
    # Create a TCP/IP socket
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = (ip, port)

    text = sys.stderr, 'starting up on %s port %s' % server_address, '\n'
    output.insert(END, text)

    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    return sock


# Starts the server listening process after validating inputs
def InitSubProcesses(lowerFrame, ip, port, msg, th_amount, attack_interval, err_label, output):
    if ip == "" or port == "" or msg == "" or not port.isnumeric() or attack_interval == "":
        output.delete("1.0", "end")
        err_label.config(text="all inputs must be entered, port must be numeric")

    else:
        port = int(port)
        th_amount = int(th_amount)
        attack_interval = int(attack_interval)

        sock = InitSocket(ip, port, output)
        if sock:
            serverThread = Thread(target=ConnectServer,
                                  args=(sock,))
            clientThread = Thread(target=Client,
                                  args=(th_amount, attack_interval, ip, port, msg, output))
            attackBtn = Button(lowerFrame, text="Attack", font=("Gisha bold", 14), width=10,
                               command=lambda: StartClientProcess(root, lowerFrame, clientThread, attackBtn))
            attackBtn.grid(row=11, column=0, columnspan=2)
            serverThread.start()


# The creation of tkinter elements for the ddos window
def CreateElements(lowerFrame):
    # getting parameters from user
    Label(lowerFrame, text="Enter an ip address or 'localhost'", font=("Gisha bold", 12)) \
        .grid(row=3, column=0)
    ip = Entry(lowerFrame, bd=2)

    # getting parameters from user
    Label(lowerFrame, text="Enter a port number", font=("Gisha bold", 12)) \
        .grid(row=4, column=0)
    port = Entry(lowerFrame, bd=2)

    # getting parameters from user
    Label(lowerFrame, text="Enter a message to send", font=("Gisha bold", 12)) \
        .grid(row=5, column=0)

    msg = Entry(lowerFrame, bd=2)

    # getting parameters from user
    Label(lowerFrame, text="Enter amount of threads", font=("Gisha bold", 12)) \
        .grid(row=6, column=0)

    th_amount = Entry(lowerFrame, bd=2)

    # getting parameters from user
    Label(lowerFrame, text="Enter how many times to run threads", font=("Gisha bold", 12)) \
        .grid(row=7, column=0)

    attack_interval = Entry(lowerFrame, bd=2)

    err_label = Label(lowerFrame, font=("Gisha bold", 12), foreground="#4d4d4d")

    output = Text(lowerFrame, width=60, height=20)
    # output.configure(state='disabled')

    connect = Button(lowerFrame, text="Connect Server", borderwidth=2, width=20, activebackground="black",
                     activeforeground="white",
                     command=lambda: InitSubProcesses(lowerFrame, ip.get(),
                                                      port.get(), msg.get(), th_amount.get(),
                                                      attack_interval.get(), err_label, output))

    backBtn = Button(lowerFrame, text="\u27F5", font=("Gisha bold", 14),
                     width=10, command=lambda: InitMainWin(root))

    return ip, port, msg, th_amount, attack_interval, err_label, output, connect, backBtn


# The placement of tkinter widget on a grid for ddos window
def AddDDOSWinElements(lowerFrame):
    ip, port, msg, th_amount, attack_interval, err_label, output, connect, backBtn = CreateElements(lowerFrame)

    ip.grid(row=3, column=1)
    port.grid(row=4, column=1)
    msg.grid(row=5, column=1)
    th_amount.grid(row=6, column=1)
    attack_interval.grid(row=7, column=1)
    err_label.grid(row=8, column=0, columnspan=2)
    Label(lowerFrame, text="<Scroll for viewing>", foreground="#4d4d4d", font=('Gisha', 10, 'bold')).grid(row=9,
                                                                                                          column=0,
                                                                                                          columnspan=2)
    output.grid(row=10, column=0, columnspan=2)
    backBtn.grid(row=2, column=0, columnspan=1)
    connect.grid(row=2, column=1, columnspan=1)


def DDOSWin(root, lowerFrame):
    # initialize window
    lowerFrame.destroy()
    lowerFrame = Frame(root, bd=10)
    lowerFrame.grid(row=1, column=0)

    AddDDOSWinElements(lowerFrame)


# creating main window
root = Tk()
InitMainWin(root)
