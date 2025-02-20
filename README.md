# 🏛️ University Management System

## 📋 Overview
The University Management System is a Python command-line application designed to manage university operations, including student enrollment, exam administration, library management, and scholarship distribution. The system supports state persistence between sessions.

## 🛠️ Key Features
- **Student Management**: Register students, assign to groups, manage scholarships
- **Exam System**: Create exams, conduct tests, evaluate results
- **Library Control**: Track books, handle checkouts/returns
- **Department Structure**: Manage faculties and departments hierarchy
- **Scholarship Automation**: Calculate stipends based on academic performance
- **CLI Interface**: Interactive command-line management
- **State Persistence**: Save/load system state
- **Comprehensive Testing**: Full unit test coverage

## ⚙️ Installation
```sh
# Clone the repository
git clone https://github.com/bogdansemchenko/university-system.git
cd university-system

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## 🎮 Usage
```sh
python -m main
```


### 🖼️ UML Diagrams

### Class Diagram
![Classes Diagram](/diagrams/classes.png)


### Class Diagram
![State Diagram](/diagrams/state.png)



# ✅ Testing
```sh
python -m unittest discover -s tests
```
## 📊 Test Coverage  

To check test coverage, use `coverage.py`:  

1. **Install `coverage` (if not installed):**  
   ```sh
   pip install coverage
   ```

2. **Run tests with coverage tracking:**  
   ```sh
   coverage run -m unittest discover -s tests
   ```

3. **Display the coverage report in the terminal:**  
   ```sh
   coverage report -m
   ```

4. **Generate an HTML report:**  
   ```sh
   coverage html
   ```
   Open `htmlcov/index.html` in a browser to view a detailed report.
