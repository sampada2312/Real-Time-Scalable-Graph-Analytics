# Real-Time-Scalable-Graph-Analytics

# Overview
This project builds a real-time, scalable graph analytics pipeline using Neo4j, Docker, Kubernetes, and Kafka. It processes the NYC Yellow Taxi Trip dataset, applying graph algorithms like PageRank and Breadth-First Search (BFS) to extract insights from interconnected data.

# Tech Stack
1. Neo4j – Graph database for efficient relationship-based queries
2. Docker – Containerization for environment consistency
3. Kubernetes – Orchestration for scalability and fault tolerance
4. Kafka – Real-time data streaming for automated graph updates
5. Helm & Minikube – Simplified Kubernetes deployments

# How It Works
1. Data Ingestion: The NYC taxi dataset is preprocessed and streamed via Kafka producers.
2. Real-Time Processing: Kafka topics organize and distribute data to Neo4j, which transforms JSON messages into graph structures.
3. Graph Analytics: PageRank identifies high-demand locations, while BFS maps optimal routes.
4. Scalability & Optimization: Kubernetes ensures fault tolerance, and Kafka partitioning allows parallel processing.

# Results & Insights
1. Identified popular taxi hotspots using PageRank
2. Simulated NYC’s transportation network with BFS
3. Achieved fault-tolerant and scalable data processing with Kubernetes

# Future Enhancements
1. Neo4j clustering for enhanced performance
2. Additional graph algorithms for deeper insights
3. Integration with visualization tools for better data representation

