import hashlib
import datetime
import time
import json

INITIAL_BITS = 0x1e777777
max_32_bit = 0xFFFFFFFF

class Block:
    def __init__(self, index, prev_hash,data,timestamp,bits):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp
        self.data = data
        self.bits = bits
        self.nonce = 0
        self.elapsed_time = ""
        self.bloc_hash = ""

    def __setitem__(self, key, value):
        setattr(self, key, value)
        def to_json(self):
            return {
                "index": self.index,
                "prev_hash": self.prev_hash,
                "storted_data": self.data,
                "timestamp": self.timestamp,
                strftime("%Y/%m/%d %H:%M:%S"),
                "bits"                      :hex(self.bits)[2:].rjust(8, '0'),
                "nonce"                     :hex(self.nonce)[2:].rjust(8, '0'),
            }
        
        