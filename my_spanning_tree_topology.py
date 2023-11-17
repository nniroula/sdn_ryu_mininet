from mininet.topo import Topo
from mininet.link import TCLink
from mininet.net import Mininet


class MySpanningTreeTopology(Topo):
    def __init__(self):
        "custom topoology"
        Topo.__init__(self)  # initialize Topology

    def create_spanning_tree_topology(self):
        #create hosts
        host_1 = self.addHost('H1')
        host_2 = self.addHost('H2')
        host_3 = self.addHost('H3')
        host_4 = self.addHost('H4')
        host_5 = self.addHost('H5')
        host_6 = self.addHost('H6')

        #create 3 switches
        switch_1 = self.addSwitch('SW1')
        switch_2 = self.addSwitch('SW2')
        switch_3 = self.addSwitch('SW3')

        #add links
        """
        switch_1 to host 1 & 2,  switch_2 to host 3 & 4, switch_3 to host 5 & 6
        switch_1 to switch 2 and 3,  switch_2 to switch 3
        """
        # switch_1 to host 1 & 2
        self.addLink(host_1, switch_1)
        self.addLink(host_2, switch_1)

        # switch_2 to host 3 & 4 
        self.addLink(host_3, switch_2)
        self.addLink(host_4, switch_2)

        # switch_3 to host 5 & 6
        self.addLink(host_5, switch_3)
        self.addLink(host_6, switch_3)

        #  switch_1 to switch 2 and 3
        self.addLink(switch_1, switch_2)
        self.addLink(switch_1, switch_3)

        # switch_2 to switch 3
        self.addLink(switch_2, switch_3)

# create a dictionary to run custom topology in mininet
topology_dictionary = {'spanningTreeTopology': (lambda: MySpanningTreeTopology())}

# invoke topology when this file is run
def topo_invocation():
    topo = MySpanningTreeTopology()
    net = Mininet(controller = None, topo = topo, link = TCLink, cleanup = True)

if __name__ == '__main__':
    topo_invocation()

