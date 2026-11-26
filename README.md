# CPU Scheduling Visualizer & Performance Analyzer

A Python-based Operating Systems project that implements and compares four CPU scheduling algorithms: **First Come First Serve (FCFS), Shortest Job First (SJF), Priority Scheduling, and Round Robin (RR)**.

The project demonstrates how an operating system allocates CPU time to different processes and evaluates the performance of each scheduling algorithm using standard scheduling metrics.

---

## 1. Project Overview

CPU scheduling is one of the most important functions of an operating system. When multiple processes are ready to execute, the operating system must decide which process should receive CPU time first.

Different scheduling algorithms follow different approaches to determine the execution order. These approaches affect waiting time, turnaround time, response time, and overall CPU utilization.

This project provides an interactive, input-driven terminal application that:

- Accepts process details from the user.
- Executes four different CPU scheduling algorithms.
- Generates a scheduling timeline (Gantt chart representation).
- Calculates performance metrics for every process.
- Computes average scheduling metrics.
- Compares the performance of all four algorithms.

The main purpose is to understand how different CPU scheduling techniques work and how their performance changes with different process inputs.

## 2. Objectives

The primary objectives of this project are:

1. Understand the concept of CPU scheduling in operating systems.
2. Implement four commonly used CPU scheduling algorithms using Python.
3. Understand the difference between preemptive and non-preemptive scheduling.
4. Calculate completion time, turnaround time, waiting time, and response time.
5. Represent process execution through a Gantt chart.
6. Compare scheduling algorithms based on their performance.
7. Apply Python data structures such as lists and queues to solve an operating systems problem.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Collections – Deque | Ready queue implementation in Round Robin |
| Lists and Dictionaries | Process storage and scheduling information |
| Terminal / Command Line | User input and program execution |
| Git and GitHub | Version control and project hosting |

## 4. CPU Scheduling Concepts

Before understanding the algorithms, it is important to understand the following terms.

### 4.1 Process

A process is a program that is currently being executed by the operating system.

Each process in this project has:
- Process ID
- Arrival Time
- Burst Time
- Priority

### 4.2 Arrival Time (AT)

The time at which a process enters the ready queue and becomes available for execution.

### 4.3 Burst Time (BT)

The total amount of CPU time required by a process to complete its execution.

### 4.4 Completion Time (CT)

The time at which a process finishes its execution.

### 4.5 Priority

A numerical value assigned to a process to determine its execution preference.

In this project, a smaller priority number represents a higher priority.

### 4.6 Time Quantum

The maximum amount of CPU time allocated to a process during one turn in the Round Robin algorithm.

---

## 5. CPU Scheduling Algorithms Implemented

The project implements four CPU scheduling algorithms.

### 5.1 First Come First Serve (FCFS)

FCFS is a non-preemptive scheduling algorithm.

It executes processes in the order in which they arrive in the ready queue.

**Working:**
1. Processes are sorted according to arrival time.
2. The process that arrives first gets the CPU.
3. It executes until completion.
4. The next process is selected.
5. The same procedure continues until all processes finish.

**Advantages:**
- Simple to implement.
- Easy to understand.
- Processes are executed in arrival order.

**Disadvantages:**
- A long process can make shorter processes wait.
- Can result in high average waiting time.

**Implementation function:** `fcfs()`

### 5.2 Shortest Job First (SJF)

SJF is implemented as a non-preemptive scheduling algorithm.

It selects the process with the shortest burst time among the processes that have already arrived.

**Working:**
1. Check which processes have arrived.
2. Select the available process with the smallest burst time.
3. Execute that process until completion.
4. Repeat the selection process until all processes finish.

If two processes have the same burst time, arrival time and input order are used as tie-breakers.

**Advantages:**
- Can reduce average waiting time.
- Gives preference to shorter processes.

**Disadvantages:**
- Longer processes may experience starvation.
- The burst time must be known or estimated.

**Implementation function:** `sjf()`

### 5.3 Priority Scheduling

Priority Scheduling is implemented as a non-preemptive scheduling algorithm.

Each process is assigned a priority, and the process with the highest priority is selected first.

**Working:**
1. Check all processes that have arrived.
2. Select the process with the highest priority.
3. Execute it until completion.
4. Repeat until all processes have finished.

In this implementation, a smaller numerical priority value indicates a higher priority.

If two processes have the same priority, arrival time and input order are used as tie-breakers.

**Advantages:**
- Important processes can be executed first.
- Useful when processes have different levels of importance.

**Disadvantages:**
- Low-priority processes may experience starvation.
- The priority assignment directly affects execution order.

**Implementation function:** `priority_scheduling()`

### 5.4 Round Robin (RR)

Round Robin is a preemptive CPU scheduling algorithm.

Each process receives a fixed amount of CPU time called the time quantum. If a process does not finish within its allocated time, it is moved to the end of the ready queue.

**Working:**
1. Processes are added to a ready queue according to their arrival time.
2. The first process is removed from the queue.
3. It executes for the time quantum or until completion.
4. If it is unfinished, it is added back to the end of the queue.
5. Newly arrived processes are added to the ready queue as they become available.
6. The process continues until every process completes.

This project uses Python's `deque` data structure to manage the ready queue.

**Advantages:**
- Provides CPU time to processes in a cyclic manner.
- Improves responsiveness in time-sharing systems.
- Prevents one process from continuously occupying the CPU.

**Disadvantages:**
- A very small time quantum can cause excessive context switching.
- A very large time quantum makes it behave more like FCFS.

**Implementation function:** `round_robin()`

---

## 6. Performance Metrics

The project calculates four important scheduling metrics.

### 6.1 Completion Time (CT)

The time at which a process finishes execution.

### 6.2 Turnaround Time (TAT)

The total time taken by a process from arrival to completion.

**Formula:**

`TAT = Completion Time - Arrival Time`

### 6.3 Waiting Time (WT)

The total time a process spends waiting in the ready queue.

**Formula:**

`WT = Turnaround Time - Burst Time`

### 6.4 Response Time (RT)

The time between the arrival of a process and its first CPU execution.

**Formula:**

`RT = First Start Time - Arrival Time`

### 6.5 Average Metrics

The program calculates the average waiting time, turnaround time, and response time for all processes.

**Formula:**

`Average = Sum of individual process values / Total number of processes`

These values help compare the efficiency of the four scheduling algorithms.

---

## 7. System Workflow

The application follows this execution workflow:

1. The program starts.
2. The user enters the total number of processes.
3. The user provides arrival time, burst time, and priority for every process.
4. The user enters the time quantum for Round Robin.
5. The program executes FCFS scheduling.
6. The program executes SJF scheduling.
7. The program executes Priority Scheduling.
8. The program executes Round Robin scheduling.
9. A scheduling timeline is generated for each algorithm.
10. Process-wise performance metrics are calculated.
11. Average performance metrics are displayed.
12. The program presents a comparison of all four algorithms.

---

## 8. Project Structure

```text
CPU-Scheduling-Visualizer/
│
├── main.py
│
└── README.md
```

### File Description

**main.py**

Contains the complete Python implementation, including:
- Process input and validation.
- FCFS scheduling.
- SJF scheduling.
- Priority Scheduling.
- Round Robin scheduling.
- Performance metric calculations.
- Gantt chart generation.
- Algorithm comparison.
- Main program execution.

**README.md**

Contains project documentation, setup instructions, algorithm explanations, and usage information.

---

## 9. Installation and Execution

### Prerequisites

Make sure you have:

- Python 3 installed.
- VS Code or another code editor.
- A terminal or command prompt.

### Step 1: Clone the Repository

Open your terminal and execute:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Navigate to the Project Folder

```bash
cd CPU-Scheduling-Visualizer
```

### Step 3: Run the Python Program

```bash
python main.py
```

If your system uses `python3`, execute:

```bash
python3 main.py
```

### Step 4: Enter Process Details

The program will ask for:
- Number of processes.
- Arrival time of each process.
- Burst time of each process.
- Priority of each process.
- Time quantum for Round Robin.

Enter valid values when prompted.

The program will then execute all four algorithms and display their results.

---

## 10. Sample Input

The following sample data can be used to test the project.

| Process | Arrival Time | Burst Time | Priority |
|---|---:|---:|---:|
| P1 | 0 | 4 | 3 |
| P2 | 5 | 1 | 1 |
| P3 | 4 | 3 | 1 |
| P4 | 2 | 1 | 2 |

**Round Robin Time Quantum:** 2

The program uses the same process data to execute all four scheduling algorithms, making their results comparable.

---

## 11. Expected Output

For each algorithm, the program displays:

- Process execution order.
- Gantt chart / execution timeline.
- Completion time.
- Turnaround time.
- Waiting time.
- Response time.
- Average waiting time.
- Average turnaround time.
- Average response time.

Finally, the program displays a comparison table containing the average performance metrics of all four algorithms.

The actual results depend on the process inputs and Round Robin time quantum entered by the user.

---

## 12. Testing

The project can be tested using different process configurations.

| Test Case | Input Condition | Expected Behaviour |
|---|---|---|
| Test 1 | Single process | Process executes and completes successfully |
| Test 2 | Multiple processes with same arrival time | Algorithm-specific selection rules are followed |
| Test 3 | Different arrival times | Processes are considered only after arrival |
| Test 4 | Different burst times | SJF selects the shortest available process |
| Test 5 | Different priorities | Priority Scheduling selects the highest-priority available process |
| Test 6 | Small Round Robin quantum | Processes receive CPU time in multiple turns |
| Test 7 | CPU has no available process | Idle time is represented in the timeline |
| Test 8 | Invalid burst time | Input validation rejects non-positive values |

---

## 13. Challenges and Solutions

| Challenge | Solution |
|---|---|
| Managing processes with different arrival times | Used arrival-time-based process selection |
| Handling CPU idle periods | Added idle segments to the scheduling timeline |
| Implementing Round Robin execution | Used Python's `deque` as a ready queue |
| Tracking unfinished processes | Maintained remaining burst time for each process |
| Calculating scheduling metrics accurately | Implemented a separate metric calculation function |
| Comparing multiple algorithms | Used the same input data for all four algorithms |

---

## 14. Learning Outcomes

Through this project, we gained practical knowledge of:

1. CPU scheduling concepts in operating systems.
2. Implementation of FCFS, SJF, Priority, and Round Robin algorithms.
3. Differences between preemptive and non-preemptive scheduling.
4. Python programming and modular function design.
5. Use of queues and lists for process management.
6. Calculation of CPU scheduling performance metrics.
7. Gantt chart representation of process execution.
8. Testing and comparing different scheduling strategies.
9. Collaborative development and project documentation.

---

## 15. Future Scope

The project can be enhanced with the following features:

- Develop a graphical user interface using Streamlit.
- Add visual Gantt charts with a graphical timeline.
- Implement additional algorithms such as Shortest Remaining Time First (SRTF).
- Implement Preemptive Priority Scheduling.
- Add Multilevel Queue Scheduling.
- Add Multilevel Feedback Queue Scheduling.
- Display graphical comparisons of average waiting and turnaround times.
- Allow users to save scheduling results as CSV or PDF reports.
- Add automated test cases for validating scheduling algorithms.

---

## 16. Team Contributions

The project work is divided between two members.

### Member 1 – CPU Scheduling Algorithms

Responsibilities:
- Developed process input and validation.
- Implemented FCFS scheduling.
- Implemented SJF scheduling.
- Implemented Priority Scheduling.
- Managed process selection and CPU idle-time handling.

### Member 2 – Round Robin and Performance Analysis

Responsibilities:
- Implemented Round Robin scheduling.
- Managed the ready queue using `deque`.
- Implemented performance metric calculations.
- Developed Gantt chart and scheduling output.
- Implemented average metric calculations.
- Developed the comparison of all four algorithms.
- Assisted with integration and testing.

*Note: This division describes the proposed allocation of project responsibilities. Update it if the actual contributions differed.*

---

## 17. Conclusion

The CPU Scheduling Visualizer & Performance Analyzer demonstrates the working of four fundamental CPU scheduling algorithms: FCFS, SJF, Priority Scheduling, and Round Robin.

By applying these algorithms to the same set of processes, the project makes it possible to compare their execution order and performance using waiting time, turnaround time, and response time.

The project provides practical exposure to operating system concepts and demonstrates how Python can be used to simulate and analyze CPU scheduling techniques.

It also highlights that no single scheduling algorithm is ideal for every situation. The choice of algorithm depends on process requirements and system objectives.

---

## 18. References

1. Operating System Concepts – Abraham Silberschatz, Peter B. Galvin, and Greg Gagne.
2. Python Official Documentation – https://docs.python.org/3/
3. Python Collections Documentation – https://docs.python.org/3/library/collections.html
4. GeeksforGeeks – CPU Scheduling in Operating Systems: https://www.geeksforgeeks.org/operating-systems/cpu-scheduling-in-operating-systems/
5. Operating Systems course notes and classroom material.

---

**Project:** CPU Scheduling Visualizer & Performance Analyzer  
**Domain:** Operating Systems  
**Programming Language:** Python  
**Project Type:** Academic / Mini Project
