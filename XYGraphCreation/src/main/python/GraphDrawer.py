

import matplotlib.pyplot as plt

class GraphDrawer:
    
    @staticmethod
    def drawContinuous(graph):
        plt.plot(graph.xValues, graph.yValues)
        plt.show()
        
    @staticmethod
    def drawScattered(graph):
        plt.scatter(graph.xValues, graph.yValues)
        plt.show()

