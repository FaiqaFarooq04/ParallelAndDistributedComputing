Lab 1: Introduction to Parallel and Distributed Computing (P&DC)
📌 Overview
This project demonstrates the fundamental concepts of Parallel Computing using Python multithreading.
The objective of this lab is to understand how concurrent execution improves performance by running multiple tasks simultaneously instead of one after another.

🎯 Objectives
Understand the basics of Parallel Computing
Compare Sequential vs Parallel execution
Implement multithreading using Python
Measure and analyze execution time
Observe thread interleaving behavior

🛠️ Technologies Used
Python 
threading module
time module

⚙️ Program Description
The program performs the same task in two different ways:

1️⃣ Sequential Execution
Workers run one after another
Each worker waits for a fixed delay
Total execution time = Sum of all delays

2️⃣ Parallel Execution (Multithreading)
Multiple threads run simultaneously
Each thread performs work independently
Total execution time ≈ Longest delay (not total delays)

💻 Code Features
Reusable worker function
Separate functions for sequential and parallel execution
Execution time measurement
Clean and modular structure

🔍 Key Observation:
Parallel execution significantly reduces total runtime because tasks are executed concurrently instead of sequentially.

🧠 Key Concepts Learned
Parallel Computing uses multiple cores of a single machine
Threads enable concurrent task execution
Shared memory model in multithreading
Execution time in parallel systems depends on the longest running task

🎓 Academic Relevance
This lab provides a foundational understanding of:
Concurrency
Multithreading
Performance optimization
High Performance Computing (HPC)
Distributed Systems (Conceptual)

🚀 Future Improvements
Use time.perf_counter() for higher precision timing
Add graphical performance comparison
Implement multiprocessing for CPU-bound tasks
Extend to distributed computing using sockets or MPI

