import networkx as nx
import matplotlib.pyplot as plt


class ResourceAllocationGraph:
    def __init__(self, processes, resources):
        # initialize empty graph
        self.graph = nx.DiGraph()

        # store lists of processes and resources
        self.processes = processes
        self.resources = resources

    def add_edge(self, process, resource):
        # add directional edge between process and resource
        self.graph.add_edge(process, resource)

    def visualize(self):
        # generate layout postions of the nodes
        position = nx.spring_layout(self.graph)

        # draw the graph
        nx.draw(
            self.graph,
            node_size=2000,
            node_color="skyblue",
            font_size=10,
            with_labels=True,
        )
        plt.title("Resource Allocation Graph")
        plt.show()

    def check_deadlock(self):
        # check if there is a cycle in the graph
        cycles = list(nx.simple_cycles(self.graph))
        if cycles:
            print("Deadlock detected")
            print("Processes involved in the deadlock:")
            print(cycles)
        else:
            print("No deadlock detected")


def main():
    processes = ["P1"]
    resources = ["R1"]

    # rag1 = ResourceAllocationGraph(processes, resources)
    # rag1.add_edge("P1", "R1")
    # rag1.add_edge("R1", "P2")
    # rag1.add_edge("P2", "R3")
    # rag1.add_edge("R3", "P3")
    # rag1.add_edge("R2", "P1")
    # rag1.add_edge("R2", "P2")

    # rag1.visualize()
    # rag1.check_deadlock()

    # rag2= ResourceAllocationGraph(processes, resources)
    # rag2.add_edge("P1", "R1")
    # rag2.add_edge("R1", "P2")
    # rag2.add_edge("P2", "R3")
    # rag2.add_edge("R3", "P3")
    # rag2.add_edge("R2", "P1")
    # rag2.add_edge("R2", "P2")
    # rag2.add_edge("P3", "R2")

    # rag2.visualize()
    # rag2.check_deadlock()

    rag3 = ResourceAllocationGraph(processes, resources)
    rag3.add_edge("P1", "R1")
    rag3.add_edge("R1", "P2")
    rag3.add_edge("P2", "R2")
    rag3.add_edge("R2", "P3")
    rag3.add_edge("P3", "R3")
    rag3.add_edge("R3", "P1")
    rag3.add_edge("P4", "R1")
    rag3.add_edge("P4", "R2")
    rag3.add_edge("P4", "R3")

    rag3.visualize()
    rag3.check_deadlock()


if __name__ == "__main__":
    main()
