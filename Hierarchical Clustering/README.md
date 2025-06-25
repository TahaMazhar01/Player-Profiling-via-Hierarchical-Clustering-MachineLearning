
````markdown
![CourtClusters Banner](https://i.imgur.com/EfK57Uh.png)

# 🏀 CourtClusters
### *Player Profiling via Hierarchical Clustering*

Cluster NBA players by their physical attributes — visualize hidden player types using unsupervised learning.


---

## 📌 Project Overview

**CourtClusters** uses *Hierarchical Agglomerative Clustering* to analyze and group NBA players based on:

- 🏗️ Height  
- ⚖️ Weight  
- ⏳ Age (derived from year of birth)

This unsupervised learning approach reveals natural clusters among players — helpful for scouting, analytics, and building strategy.

---

## 🧠 Algorithm: Hierarchical Clustering

We use **Agglomerative Clustering** with **Ward's linkage**:

> Starts by treating each player as its own cluster, then repeatedly merges the closest pairs until 3 final clusters remain.

### 🔬 Features Used:
- `height`
- `weight`
- `age = 2025 - born`

### 📊 Visual Tools:
- 📈 **Dendrogram** to explore cluster merges
- 🔵 **PCA 2D Scatter Plot** to show final clusters

---

## ⚙️ Workflow

```mermaid
graph TD
A[Load NBA Dataset] --> B[Drop Missing Values]
B --> C[Compute Age from Birth Year]
C --> D[Standardize Data]
D --> E[Plot Dendrogram (sample)]
E --> F[Apply Agglomerative Clustering]
F --> G[Project with PCA]
G --> H[Visualize Clusters]
H --> I[Save Clustered CSV]
````

---

## 📁 Files Included

| File                      | Description                         |
| ------------------------- | ----------------------------------- |
| `courtclusters.py`        | Python script with clustering logic |
| `Players.csv`             | NBA player data (input)             |
| `NBA_Player_Clusters.csv` | Output file with cluster labels     |
| `README.md`               | This documentation                  |

---

## 📸 Sample Output

### 📉 Dendrogram (sample of 200)

![Dendrogram](https://i.imgur.com/b96RJCU.png)

### 📊 Final Clusters (PCA projection)

![Clusters](https://i.imgur.com/Gw3cWZ7.png)

---

## 🛠️ How to Run

```bash
# 1. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn scipy

# 2. Run the script
python courtclusters.py
```

Output will be saved as:

* `NBA_Player_Clusters.csv`

---

## 🎯 Real-World Use Cases

* Player similarity profiling
* Uncovering hidden player roles
* Strategy for recruitment or matchups
* Data-driven performance analysis

---

## 👨‍💻 Author

**Taha Mazhar**
📘 BSCS-AI Student
💡 GitHub: [@TahaMazhar01](https://github.com/TahaMazhar01)

---

> Made with 💙 for Data Science, Machine Learning, and Sports Analytics.

```

---

