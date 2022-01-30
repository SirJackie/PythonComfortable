class BinaryCoding:
    @staticmethod
    def EncodeToHex(s):
        return ' '.join([hex(ord(c)).replace('0x', '') for c in s])

    @staticmethod
    def DecodeFromHex(s):
        return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

    @staticmethod
    def EncodeToBin(s):
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

    @staticmethod
    def DecodeFromBin(s):
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
