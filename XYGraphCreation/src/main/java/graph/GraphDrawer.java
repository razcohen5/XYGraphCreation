package graph;

import java.io.IOException;

import static json.JsonIO.writeToJsonFile;

public class GraphDrawer {
    public static void draw(Graph graph, String jsonFilePath) throws IOException {
        writeToJsonFile(graph, jsonFilePath);
    }
}
