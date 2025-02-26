from blockchain import Blockchain

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = Blockchain()
        self.peers = []

    def add_peer(self, peer):
        if peer not in self.peers:
            self.peers.append(peer)
