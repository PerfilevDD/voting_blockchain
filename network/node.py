from blockchain import Blockchain

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = Blockchain()
        self.peers = []

    def add_peer(self, peer):
        if peer not in self.peers:
            self.peers.append(peer)

    def broadcast_block(self, block):
        self.blockchain.chain.append(block)
        for peer in self.peers:
            peer.blockchain.chain.append(block)