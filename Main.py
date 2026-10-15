import Node
import QueueFrontier
import StackFrontier

def graph_search(graph, start, goal, frontier):
    start_node = Node.Node(start, None)
    frontier.add(start_node)
    explored = set()
    # explored_list = []

    while not frontier.empty():
        node = frontier.remove()
        if node.state == goal:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1], explored
        explored.add(node.state)

        for neighbor in graph[node.state]:
            if neighbor not in explored and not frontier.contains_state(neighbor):
                child_node = Node.Node(neighbor, node)
                frontier.add(child_node)

    return None, explored

def main():
    road_dictionary = {
        "Jalan Dakota": ["Jalan Tol Insinyur Sutami", "Jalan Poros Makassar-Maros"],
        "Jalan Tol Insinyur Sutami": ["Jalan Tol Reformasi"],
        "Jalan Tol Reformasi": ["Jalan Nusantara"],
        "Jalan Nusantara": ["Jalan Ahmad Yani", "Jalan Ujung Pandang"],
        "Jalan Ahmad Yani": ["Jalan Kajaolalido"],
        "Jalan Kajaolalido": ["Jalan Botolempangan"],
        "Jalan Botolempangan": ["Jalan Arief Rate"],
        "Jalan Arief Rate": ["Jalan Haji Bau"],
        "Jalan Haji Bau": ["Jalan Metro Tanjung Bunga"],
        "Jalan Metro Tanjung Bunga": ["Universitas Ciputra Makassar"],
        "Jalan Ujung Pandang": ["Jalan Pattimura"],
        "Jalan Pattimura": ["Jalan Somba Opu"],
        "Jalan Somba Opu": ["Jalan Datu Museng"],
        "Jalan Datu Museng": ["Jalan Lamadukelleng"],
        "Jalan Lamadukelleng": ["Jalan Haji Bau"],
        "Jalan Poros Makassar-Maros": ["Jalan Perintis Kemerdekaan"],
        "Jalan Perintis Kemerdekaan": ["Jalan Urip Sumoharjo"],
        "Jalan Urip Sumoharjo": ["Jalan G. Bawakaraeng"],
        "Jalan G. Bawakaraeng": ["Jalan Jendral Sudirman"],
        "Jalan Jendral Sudirman": ["Jalan Haji Bau"],
        "Universitas Ciputra Makassar": [],
    }
    
    bfs_path, bfs_explored = graph_search(road_dictionary, "Jalan Dakota", "Universitas Ciputra Makassar", QueueFrontier.QueueFrontier())
    dfs_path, dfs_explored = graph_search(road_dictionary, "Jalan Dakota", "Universitas Ciputra Makassar", StackFrontier.StackFrontier())
    print("========== BFS RESULTS ==========")
    print("BFS Path      :", bfs_path)
    print("BFS Explored  :", bfs_explored)
    print("========== DFS RESULTS ==========")
    print("DFS Path      :", dfs_path)
    print("DFS Explored  :", dfs_explored)
    
main()
