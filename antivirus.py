import os
import hashlib

db = ['e7ae40d25a6da15cdd3712f4f55153ac'    #virus signature datasets
'8fc63e8c5de9e771badefaa50cc2f7a0'
'c625ff97e147e897468204e0e6ccd1aa'
'938079b196c598bc43f97e0ecf128e77'
'854c46dc5add43e52fce685c7bd4cde7'
'3e301fc7ed1e1dc7793c61ccf23d720f'
'3ff4fb0f3d4e399417a30f2c186d60e5'
'764c4787a81f6eb9810ffe976c30bd05'
'842caf6a2541711be2ff90166a995c7b'
'f5ebbde3539c7816f737bf77dbaa0cab'
'b83a737a65d618962cd2f5d90bc06285'
'99e191582f572af612528391d4f56632'
'3754c65c00ba0344aded36af9607cac3'
'49fde32bc6d109b5b655e718e11d75e1'
'9fa2073564eb7a683a1afe712e304427'
'b08029b47a99f94e7a36224039cb2830'
'505e823c3415e8b4913447a579b58c6e'
'e4bbb4896dbaeb5aa22c93c5a0e78c84'
'21b70adc38e76624144eb632934bfa39'
'5eba35029b917df9b8190fc15837beb0'
'9e1c2f8106b932896bd4970520a884e6'
'c2da68e46e75d3b75d19e9335ef69a67'
'6ba67748aabea0b0623013bca2046d4d'
'f4e87a55c0e9664833f6e86b1a0af4e6'
'7045b8a99587d53b479d23793be219cd'
'e52918d04156e708658590dd0f2c8f81']

def check(signature, efile):    #Defining a function to verify the signatures.
    print(f" {signature} ")
    if signature in db:
        print(f'Malicious {efile}')

file_list = os.listdir(".") #Directory direction
for efile in file_list:
    if ".exe" in efile:
        print(efile)
        result = hashlib.md5(efile.encode())
        print(result.hexdigest())