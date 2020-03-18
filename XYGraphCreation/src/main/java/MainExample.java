import graph.Graph;
import graph.GraphPoint;

import java.io.IOException;

import static graph.GraphDrawer.draw;

public class MainExample {
    public static void main(String[] args) throws IOException {
        String jsonFilePath = "examplejsonfiles\\json.txt";
        Graph graph = new Graph(new GraphPoint[]{
                new GraphPoint(-150, 0.02),
                new GraphPoint(0, 500),
                new GraphPoint(1, -100),
                new GraphPoint(100, 0.05),
                new GraphPoint(500, -1000)});
        draw(graph, jsonFilePath);
    }
}
