

from JsonIO import JsonIO
from GraphJsonConverter import GraphJsonConverter
from GraphDrawer import GraphDrawer

def MainExample():
    jsonFilePath = "C:\intellij\projects\XYGraphCreation\examplejsonfiles\json.txt"
    graphAsJson = JsonIO.read(jsonFilePath)
    graph = GraphJsonConverter.convertJsonToGraph(graphAsJson)
    GraphDrawer.drawScattered(graph)
    GraphDrawer.drawContinuous(graph)
    
MainExample()