from network.network import Network

network = Network(3)

# Test node creation
print(f"Number of nodes is created - {len(network.nodes)}")
print("First node:", network.nodes[0].node_id)
node_0 = network.get_node("node_0")

# Test peer connection
print("node_0 is connected to", [node.node_id for node in node_0.peers])