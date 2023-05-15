import { Queue } from '../queues/queue.js';


class Vertex {
    constructor(value) {
        this.value = value;
        this.adjacentVertices = [];
    }

    addNewConnection(vertex) {
        if (!this.adjacentVertices.includes(vertex)) {
            this.adjacentVertices.push(vertex);
        }
        vertex.addNewConnection(this);
    }
}


class Graph {
    constructor() {

    }

    // O(V + E)
    depthFirstSearch(value, vertex, visitedVertices={}) {
        if (value === vertex.value) {
            return value;
        }
        visitedVertices[vertex.value] = true;
        for (let v of vertex.adjacentVertices) {
            if (visitedVertices[v.value]) {
                continue;
            }
            if (v.value === value) {
                return v;
            }
            let vertexBeingSearched = this.depthFirstSearch(value, v, visitedVertices);
            if (vertexBeingSearched) {
                return vertexBeingSearched;
            }
        }
    }

    // O(V + E)
    depthFirstSearchTraverse(vertex, visitedVertices={}) {
        visitedVertices[vertex.value] = true;

        for (let v of vertex.adjacentVertices) {
            if (visitedVertices[v.value]) {
                continue;
            }
            this.depthFirstSearchTraverse(v, visitedVertices);
        }
    }

    // O(V + E)
    breadthFirstSearchTraverse(StartVertex) {
        let queue = new Queue();
        let visitedVertices = {};
        visitedVertices[StartVertex.value] = true;
        queue.enqueue(StartVertex);

        while (queue.length > 0) {
            let currentVertex = queue.dequeue();
            console.log(currentVertex.value);

            for (let v of currentVertex.adjacentVertices) {
                if (!visitedVertices[v.value]) {
                    visitedVertices[v.value] = true;
                    queue.enqueue(v);
                }
            } 
        }
    }
}