

from Graph import Graph

class GraphJsonConverter:
    GRAPH_POINTS_NAME = 'points'
    X_VALUE_NAME = 'x'
    Y_VALUE_NAME = 'y'
    
    @classmethod
    def convertJsonToGraph(cls,graphAsJson):
        xValues = []
        yValues = []
        for point in graphAsJson[cls.GRAPH_POINTS_NAME]:
            xValues.append(point[cls.X_VALUE_NAME])
            yValues.append(point[cls.Y_VALUE_NAME])
        return Graph(xValues,yValues)