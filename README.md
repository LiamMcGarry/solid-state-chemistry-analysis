# 🧪 Solid-State Chemistry Analysis

This project demonstrates basic data analysis and visualization of X-ray diffraction (XRD) data using Python. It is designed to showcase coding proficiency, good documentation practices, and interest in solid-state chemistry.

---

## 📊 What This Project Does

- Loads XRD data from a CSV file
- Normalizes the intensity values
- Plots the normalized XRD pattern using `matplotlib`

---

## 📁 Project Structure

```
solid-state-chemistry-analysis/
├── data/                  # Folder for datasets
│   └── sample_xrd.csv     # Sample XRD data
├── notebooks/             # Jupyter notebooks for exploration
│   └── xrd_analysis_demo.ipynb
├── src/                   # Python source code
│   └── xrd_analysis.py    # Core functions
├── tests/                 # (Optional) Folder for future test scripts
├── requirements.txt       # Dependencies list
└── README.md              # Project documentation
```


---

## 🧬 Sample Dataset

A small simulated dataset is provided in `data/sample_xrd.csv` with two columns:

```csv
2Theta,Intensity
10,100
15,250
20,300
25,200
30,100
35,50
40,75

---

## ▶️ How to Run the Project

1. **Install the requirements**  
   Open a terminal and run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main Python script**  
   This will load and plot the sample XRD data:

   ```bash
   python src/xrd_analysis.py
   ```

3. **(Optional) Use the Jupyter Notebook**  
   If you prefer to explore the data interactively:

   ```bash
   jupyter notebook notebooks/xrd_analysis_demo.ipynb
   ```


---

## 📦 Requirements

- Python 3.8+
- pandas
- matplotlib
- jupyter (optional for running notebooks)

To install all dependencies at once:

```bash
pip install -r requirements.txt
```

---

## 🎯 Purpose

This project was developed to:

- Demonstrate practical data analysis and visualization skills using Python
- Apply computational techniques to problems in solid-state and materials chemistry
- Showcase best practices in code organization, documentation, and reproducibility
- Serve as a foundation for more advanced workflows in scientific data processing

---

## 📬 Contact

**Author**: Liam F  
If you have any questions, feedback, or collaboration ideas, feel free to reach out via GitHub or email.
