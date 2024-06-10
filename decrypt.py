import base64

message = 'EUgAEBMLEhoXTUFQQRZXQg8OB0JcSFAKCwYNDwBWRVVNT0lFVw0EHQEPDA8FFhwQTQoVAx8aAxpD\nSltKRlheUxgKFwwSBBJOSEpGCwJZWVUcCh4AHhxQSV5KRh8PXV9TAQoXQlxIUBsFCAMDFUIXEFBP\nVBYRDhJOSEpGDA5eFxBQT1QSGQZWThk='
key = 'josephwidjaja100'

print(''.join(map(lambda x: chr(x[1] ^ ord(key[x[0] % len(key)])), enumerate(base64.b64decode(message)))))
