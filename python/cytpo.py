from Crypto.Hash import HMAC, SHA256
from Crypto.Hash import SHA1

# 8cb95ac97c1b28a108b8adb017f177134ac208ba
secret = b'735862ad-301d-439a-8a7e-e40919289841'
itemid = b'55de0417-0ef6-488d-92c6-3453bdafbb0e'
h1 = HMAC.new(secret,itemid)

itemid2 = b'fe81c881-19fd-4389-8253-55c3ee2058f4'
h2 = HMAC.new(secret,itemid2)

h3 = SHA1.new()
h3.SHA1_Hash(secret)


print(h1.hexdigest(),h2.hexdigest(),h3)