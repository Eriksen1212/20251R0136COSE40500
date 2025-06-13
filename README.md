# 20251R0136COSE40500

This repository collects concise overviews and code examples covering core computer science and machine learning topics. It is organized into two main folders:

- **docs/**: Human-readable explanations and summaries of key concepts  
- **examples/**: Ready-to-run Python scripts illustrating algorithms and workflows  

---

## 📂 Repository Structure

20251R0136COSE40500/
├── README.md
├── docs/
│ ├── algorithm.md
│ ├── AI_overview.md
│ ├── database_overview.md
│ ├── deep_learning.md
│ ├── quick_sort.md
│ ├── machine_learning_overview.md
│ └── nosql_overview.md
└── examples/
├── activity_selection_greedy_example.py
├── bfs_graph_example.py
├── binary_search.py
├── dijkstra_example.py
├── dfs_graph_example.py
├── knapsack_dp_example.py
├── linear_regression_example.py
├── merge_sort_example.py
├── quick_sort_example.py
└── subset_sum_bruteforce_example.py


---

## 📖 What’s Inside `docs/`

1. **machine_learning_overview.md**  
   High-level introduction to machine learning paradigms, workflow, and a simple linear regression example.

2. **quick_sort.md**  
   Explanation of Quick Sort’s divide-and-conquer strategy, time/space complexity, pseudocode, and Python implementation.

3. **algorithm.md**  
   Definition of algorithms, key properties, classification by technique, plus a binary search example.

4. **deep_learning.md**  
   Overview of deep learning architectures (CNN, RNN, Transformers) and a minimal Keras model snippet.

5. **AI_overview.md**  
   Broad survey of AI subfields (ML, NLP, Computer Vision, Robotics) and their relationships.

6. **database_overview.md**  
   Fundamentals of relational databases: schema design, ACID properties, SQL examples.

7. **nosql_overview.md**  
   Introduction to NoSQL database types (document, key–value, column-family, graph) and a MongoDB document example.

---

## 💻 What’s Inside `examples/`

Each Python script demonstrates a classic algorithm or workflow:

- **Linear Regression** (`linear_regression_example.py`): scikit-learn regression demo  
- **Quick Sort** (`quick_sort_example.py`) & **Merge Sort** (`merge_sort_example.py`): sorting algorithms  
- **Binary Search** (`binary_search.py`): efficient ordered lookup  
- **Knapsack DP** (`knapsack_dp_example.py`): dynamic programming on optimization  
- **Activity Selection** (`activity_selection_greedy_example.py`): greedy strategy  
- **Subset Sum** (`subset_sum_bruteforce_example.py`): brute-force enumeration  
- **BFS & DFS** (`bfs_graph_example.py`, `dfs_graph_example.py`): graph traversals  
- **Dijkstra’s Algorithm** (`dijkstra_example.py`): shortest-path on weighted graphs  

Each script includes a `__main__` section so you can run it directly:

```bash
python examples/linear_regression_example.py

