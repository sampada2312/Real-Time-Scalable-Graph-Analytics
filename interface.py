from neo4j import GraphDatabase


class Interface:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        self._driver.verify_connectivity()

    def close(self):
        self._driver.close()

    def _check_and_create_graph(self, session, graph_name):
        result = session.run("CALL gds.graph.exists($name)", name=graph_name)
        if not result.single()["exists"]:
            session.run(
                """
            CALL gds.graph.project(
                $graph_name,
                'Location',
                'TRIP',
                {
                    nodeProperties: ['name'],
                    relationshipProperties: ['distance']
                }
            )
            """,
                graph_name=graph_name,
            )

    def bfs(self, start_node, last_node):
        with self._driver.session() as session:
            self._check_and_create_graph(session, "nyc-taxi-graph")

            # Execute BFS with proper node ID handling
            query = """
            MATCH (source:Location {name: $start}), (target:Location {name: $end})
            CALL gds.bfs.stream('nyc-taxi-graph', {
                sourceNode: source,
                targetNodes: [target]
            })
            YIELD path
            RETURN [node in nodes(path) | {name: node.name}] as path
            """

            result = session.run(query, start=start_node, end=last_node)
            paths = [{"path": record["path"]} for record in result]

            return paths

    def pagerank(self, max_iterations, weight_property):
        with self._driver.session() as session:
            self._check_and_create_graph(session, "nyc-taxi-graph")

            result = session.run(
                """
            CALL gds.pageRank.stream('nyc-taxi-graph', {
                maxIterations: $max_iterations,
                relationshipWeightProperty: $weight_property,
                dampingFactor: 0.85
            })
            YIELD nodeId, score
            WITH gds.util.asNode(nodeId) AS node, score
            RETURN node.name AS node_id, score
            ORDER BY score DESC
            """,
                max_iterations=max_iterations,
                weight_property=weight_property,
            )

            nodes = list(result)
            if not nodes:
                return None, None

            max_node = {"name": int(nodes[0]["node_id"]), "score": nodes[0]["score"]}
            min_node = {"name": int(nodes[-1]["node_id"]), "score": nodes[-1]["score"]}

            return max_node, min_node
