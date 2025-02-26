from network.node import Node

class Network:
    def __init__(self, num_nodes):
        self.nodes = [Node(f"node_{i}") for i in range (num_nodes)]

        # connect all nodes to each other
        for node in self.nodes:
            for peer in self.nodes:
                if node != peer:
                    node.add_peer(peer)

    def get_node(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None