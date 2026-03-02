# 🔢 Project Euler — Python Solutions

This repository contains my personal solutions to [Project Euler](https://projecteuler.net) problems, written in Python. Each solution comes with detailed comments explaining not just *what* the code does, but *why* I chose that particular approach to solve the problem.

---

## 📁 Repository Structure

```
project-euler/
│
├── README.md
│
├── problem_001/
│   └── solution.py
│
├── problem_067/
│   ├── solution.py
│   └── triangle.txt        ← some problems require an external file
│
└── ...
```

Each problem lives in its own folder named `problem_XXX`. If a problem requires an external data file to run, that file is included in the same folder as the solution.

---

## ▶️ How to Run

Make sure you have **Python 3** installed. Then:

```bash
# Clone the repository
git clone https://github.com/yourusername/project-euler.git
cd project-euler

# Run any solution
python problem_067/solution.py
```

---

## ⚠️ Problems That Require an External File

Some Project Euler problems provide a separate data file (a `.txt` file) that the solution reads from. These files are already included in the corresponding problem folder, so you do not need to download anything separately.

However, **the solution and the data file must be in the same folder** when you run the code. If you move the solution file somewhere else, it will not find the data file and will throw an error.

The problems that require an external file are listed below:

| Problem | File Required | Description |
|---------|--------------|-------------|
| 067 | `triangle.txt` | 100-row triangle for Maximum Path Sum II |

> More will be added as I solve problems that require data files.

If you ever see this error when running a solution:

```
FileNotFoundError: [Errno 2] No such file or directory: 'triangle.txt'
```

It means you are running the script from a different directory. Fix it by navigating into the problem folder first:

```bash
cd problem_067
python solution.py
```

---

## 🧠 My Approach

For each problem I try to:

1. **Understand why the naive/brute force solution fails** — usually because it is too slow at scale
2. **Find the key insight** that makes the problem solvable efficiently
3. **Choose an algorithm** that is both correct and fast enough
4. **Write readable code** with comments that explain the reasoning, not just the syntax

The comments in each file are intentionally detailed. My goal is that someone who has never seen the problem before can read the solution and understand both what is happening and why.

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required — all solutions use the Python standard library only

---

## 📝 Notes

- I do not publish the raw answers in this README intentionally — working through the problems yourself is the whole point
- Solutions are written for clarity first, performance second
- If you are also solving Project Euler problems and want to discuss approaches, feel free to open an issue

---

*Solutions are my own work. Problem statements belong to [projecteuler.net](https://projecteuler.net).*"

---
## 👤 Author

Ece Melisa Aksoy 
