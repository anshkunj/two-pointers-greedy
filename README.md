# 🚀 Two Pointers & Greedy Patterns

A curated collection of **two pointers and greedy algorithm problems** focusing on array manipulation, interval handling, and in-place optimization. Each solution is optimized, explained with diagrams, and mapped to real-world scenarios like scheduling, merging intervals, and subarray analysis.

---

## 🧠 Features
- Well-structured Python solutions  
- Optimized O(n) or O(n log n) algorithms  
- Clear explanation of pointer movement and greedy decisions  
- ASCII diagrams showing pointer progression  
- Real-world problem analogies  

---

## 📂 Repo Structure

two-pointers-greedy/  
├── README.md                  # This file  
├── 15_3sum.py                 # Three sum problem, two pointers  
├── 16_3sum_closest.py         # Closest sum using two pointers  
├── 18_4sum.py                 # Four sum with sorting + pointers  
├── 167_two_sum_II.py          # Two sum in sorted array  
├── 345_reverse_vowels.py      # Two pointers, string manipulation  
├── 881_boats_to_save_people.py# Greedy interval packing  
├── 435_non_overlapping_intervals.py # Greedy interval scheduling  
└── ... (add more two pointers & greedy problems)  

---

## 🏗️ How This Repo Works
- Each `.py` file contains a single problem solution  
- Two pointers logic explained in **comments + diagrams**  
- Greedy approach clearly justified step-by-step  
- Focus on **O(n)/O(n log n) efficiency** and real-world mapping  

---

## 📌 Problem Patterns Covered
- Two pointers on sorted arrays  
- In-place array manipulation  
- Sliding interval / merging intervals  
- Greedy choices for optimization  
- Maximum / minimum count problems  

---

## ⚙️ How to Use
1. Clone the repository  
git clone https://github.com/anshkunj/two-pointers-greedy.git  
cd two-pointers-greedy  

2. Open any `.py` file, read problem statement, and understand the pointer/greedy logic  

3. Solve or adapt the code for your own projects  
   - Add diagrams  
   - Experiment with different pointer strategies or greedy choices  

---

## 🧪 Example (Boats to Save People)

people = [3,2,2,1]  
limit = 3  
print(num_rescue_boats(people, limit))  
# Output: 3  

- Sort array, use two pointers (lightest + heaviest)  
- Greedy: pair heaviest with lightest to minimize boats  
- Optimal O(n log n) solution using sorting + pointers  

---

## 🚧 Edge Cases Handled
- Empty arrays / lists  
- Single element arrays  
- Large input sizes  
- Unsorted input handled via sorting if needed  

---

## 🛠️ Tech Stack
- Python 3.x  
- Standard libraries (`collections`, `heapq`)  
- Optional: Jupyter Notebook for visualization  

---

## 📄 Licence
MIT Licence  

---

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new two pointers and greedy problems and explanations.