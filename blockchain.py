from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0)
    
    def get_latest_block(self):
        return self.chain[-1]