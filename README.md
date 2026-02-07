<p align="center">
  <img src="https://github.com/anshkunj/two-pointers-greedy/blob/1fea7f35098bf55d72b6a9fcb6305d6cdaa92335/file_000000002b1c71fa99af67ad8fc90e33.png" alt="Two Pointers & Greedy Patterns" width="1200">
</p>

<h1 align="center">Two Pointers & Greedy Patterns</h1>
<p align="center">Optimize and Solve Efficient Algorithms Using Two Pointers & Greedy Techniques 🚀</p>

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
├── main.py          # FastAPI app & routes
├── logic.py         # Core algorithm implementations  
├── models.py        # Pydantic request models  
├── requirements.txt  
├── README.md  
└── LICENSE  

---

## 🏗️ How This Repo Works
- logic.py contain logic of all problems  
- Two pointers logic explained  
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

## ⚙️ Installation & Run

1) Clone the repository  
git clone https://github.com/anshkunj/two-pointers-greedy.git  
cd two-pointers-greedy  

2) Install dependencies  
pip install -r requirements.txt  

3) Run the server  
uvicorn main:app --reload  

---

## 🌐 API Documentation

Swagger UI: http://127.0.0.1:8000/docs  

ReDoc: http://127.0.0.1:8000/redoc  

---

## 🌐 Live API

Base URL: https://two-pointers-greedy.onrender.com  
Docs: https://two-pointers-greedy.onrender.com/docs  

---

## 🔗 Endpoints – Two Pointers & Greedy Patterns

This section documents conceptual API-style endpoints mapped to the functions in logic.py.
Each endpoint shows example input and expected output.

### 1️⃣ Container With Most Water
Endpoint: /two-pointers/max-area

Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
maxArea = 49

### 2️⃣ 3Sum
Endpoint: /two-pointers/three-sum

Input:
nums = [-1,0,1,2,-1,-4]

Output:
triplets = [[-1,-1,2],[-1,0,1]]

### 3️⃣ 3Sum Closest
Endpoint: /two-pointers/three-sum-closest

Input:
nums = [-1,2,1,-4]
target = 1

Output:
closestSum = 2

### 4️⃣ Two Sum II - Input array sorted
Endpoint: /two-pointers/two-sum-sorted

Input:
numbers = [2,7,11,15]
target = 9

Output:
indices = [1,2]

### 5️⃣ Remove Duplicates from Sorted Array
Endpoint: /two-pointers/remove-duplicates

Input:
nums = [0,0,1,1,1,2,2,3,3,4]

Output:
length = 5
nums (first 5 elements) = [0,1,2,3,4]

### 6️⃣ Squares of a Sorted Array
Endpoint: /two-pointers/sorted-squares

Input:
nums = [-4,-1,0,3,10]

Output:
squares = [0,1,9,16,100]

### 7️⃣ Merge Sorted Array
Endpoint: /two-pointers/merge-sorted

Input:
nums1 = [1,2,3,0,0,0], m=3
nums2 = [2,5,6], n=3

Output:
nums1 after merge = [1,2,2,3,5,6]

### 8️⃣ Intersection of Two Arrays II
Endpoint: /two-pointers/intersect

Input:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
intersection = [2,2]

### 9️⃣ Remove Element
Endpoint: /two-pointers/remove-element

Input:
nums = [3,2,2,3]
val = 3

Output:
length = 2
nums (first 2 elements) = [2,2]

### 1️⃣0️⃣ Valid Palindrome
Endpoint: /two-pointers/valid-palindrome

Input:
s = "racecar"

Output:
isValid = true

### 1️⃣1️⃣ Longest Mountain in Array
Endpoint: /two-pointers/longest-mountain

Input:
arr = [2,1,4,7,3,2,5]

Output:
length = 5

### 1️⃣2️⃣ Candy (Greedy)
Endpoint: /greedy/candy

Input:
ratings = [1,0,2]

Output:
totalCandies = 5

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

## 🤝 Contributing
Contributors are welcome!  
• Add new ```two-pointers``` problems  
• Improve explanations  
• Optimise exists code  

---

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  
LinkedIn: https://linkedin.com/in/anshkunj 

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new two pointers and greedy problems and explanations.
