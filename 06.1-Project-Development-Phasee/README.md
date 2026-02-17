## Visualizing Housing Market Trends Using Tableau & Flask

---

## 📌 Overview

This phase represents the complete implementation stage of the Housing Market Analysis project.

It includes:

- Raw dataset handling  
- Data preprocessing & transformation  
- Business question formulation  
- Tableau dashboard development  
- Web integration using Flask  

This folder contains all development-level assets before final documentation and deployment.

---

# 📁 Folder Structure

```

06.1-Project-Development-Phase/
│
├── 01_Dataset/
│     └── Transformed_Housing_Data2.csv
│
├── 02_Preprocessing_and_Business_Analysis/
│     ├── Preprocessing_Code.ipynb
│     ├── Cleaned_Dataset.csv
│     └── Preprocessing_and_Business_Questions.pdf
│
├── 03_Dashboard_and_Web_Screenshots/
│     ├── Dashboard_Screenshot.png
│     ├── Story_Screenshot.png
│     ├── Web_App_Screenshot.png
│     └── Dashboard_and_Web_Outputs.pdf
│
├── 04_Flask_Web_App/
│     ├── app.py
│     ├── requirements.txt
│     ├── templates/
│     │     └── index.html
│     └── static/
│           ├── css/
│           ├── js/
│           └── images/
│
└── README.md

```

---

# 🔹 01 – Dataset

Contains the original dataset:

**Transformed_Housing_Data2.csv**

### Dataset Details:
- Total Records: 21,613
- Domain: Housing Market
- Type: Structured CSV

### Key Attributes:
- Sale Price  
- Bedrooms  
- Bathrooms  
- Floors  
- House Age  
- Renovation Status  
- Basement Area  
- Lot Area  

This dataset serves as the base input for preprocessing and visualization.

---

# 🔹 02 – Preprocessing and Business Analysis

This section includes all data transformation and analytical logic.

### Activities Performed:

- Handling missing values  
- Feature engineering (House Age, Price Categories, etc.)  
- Outlier removal using IQR method  
- Derived metrics (Price per Sqft)  
- Business question formulation  

### Output Generated:

- **Cleaned_Dataset.csv**  
- Structured preprocessing notebook (.ipynb or .py)  
- PDF containing business questions mapped to visualizations  

---

# 🔹 03 – Dashboard and Web Screenshots

Contains visual proof of implemented outputs:

### Tableau Dashboard
- KPI Tiles (Avg Price, Total Properties, etc.)
- Price vs Renovation Analysis
- Feature Comparisons

### Tableau Story
- Sequential storytelling of housing insights

### Flask Web Application
- Dynamic metric display
- Integration with cleaned dataset
- Structured frontend layout

Screenshots are included for evaluation and documentation.

---

# 🔹 04 – Flask Web Application

This module integrates the processed dataset into a lightweight web interface.

### Technologies Used:
- Python
- Flask
- Pandas
- HTML
- CSS
- JavaScript

### Features:
- Displays dynamic housing metrics
- Reads from Cleaned_Dataset.csv
- Structured MVC-style folder organization
- Local deployment capability

### Run Instructions:

1. Install dependencies:
```

pip install -r requirements.txt

```

2. Ensure Cleaned_Dataset.csv is in the same directory as app.py

3. Run the application:
```

python app.py

```

4. Open in browser:
```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

# 📊 Development Outcomes

✔ Cleaned and structured dataset  
✔ Business-driven analytical insights  
✔ Interactive Tableau dashboard  
✔ Story-based data narrative  
✔ Web-based data integration  
✔ End-to-end project implementation  

---

# 🚀 Conclusion

The Project Development Phase successfully transforms raw housing data into:

- Business insights  
- Interactive visualizations  
- A functional web application  

This phase demonstrates full-cycle implementation from data preprocessing to user-facing deployment.
