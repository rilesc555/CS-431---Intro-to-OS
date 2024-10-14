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


def main():
    processes = ["P1"]
    resources = ["R1"]

    rag = ResourceAllocationGraph(processes, resources)
    rag.add_edge("P1", "R1")
    rag.add_edge("R1", "P2")
    rag.add_edge("P2", "R3")
    rag.add_edge("R3", "P3")
    rag.add_edge("R2", "P1")
    rag.add_edge("R2", "P2")

    rag.visualize()


if __name__ == "__main__":
    main()
