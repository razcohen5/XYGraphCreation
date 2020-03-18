package graph;

public class Graph {
    private final GraphPoint[] points;

    public Graph(GraphPoint[] points) {
        this.points = points;
    }

    public GraphPoint[] getPoints() {
        return points;
    }
}
