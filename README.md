---

# **SuperStore Sales and Profit Analysis**

## **Project Overview**  
This project analyzes SuperStore sales and profit data across various U.S. states, leveraging data visualization, clustering techniques, and geographic mapping. The goal is to identify key insights that can drive strategic business decisions and improve profitability.

---

## **Project Structure**  
The project files are organized as follows:  

### **Data Analysis & Visualizations**  
- **`BI_EDA.ipynb`** – Exploratory Data Analysis (EDA) notebook for analyzing sales trends, customer behavior, and regional patterns.  
- **`kmeans_cluster.ipynb`** – Implements K-Means clustering to identify customer segments based on purchasing behavior.  

### **Visualizations & Dashboards**  
- **`BI Dashboard.twb`** – Interactive Tableau dashboard visualizing key insights.  
- **`discount_map.html`**, **`profit_map.html`**, **`sales_map.html`** – Interactive geographic visualizations showing sales, profit, and discount distribution.  
- **State-specific visualizations:**  
   - `pennsylvania sales vs profit.png`  
   - `repeat customer pennsylvania.png`  
   - `repeat customers washington.png`  
   - `texas sales vs profit.png`  
   - `washington sales:profit.png`  

### **Supporting Files**  
- **`SuperStore.db`** – Database containing structured data for analysis.  
- **`SuperStore_Database.py`** – Python script for data cleaning, transformation, and visualization.  
- **`Bi_analysis_powerpoint.pptx`** – Presentation summarizing key insights and actionable recommendations.  

---

## **Key Insights**  
### 🔍 **Profit vs Sales Analysis**  
- Identified profitable and underperforming regions, revealing that states like **Texas** and **Washington** had high sales volumes but struggled with profitability.  
- Visualized key trends with interactive maps to highlight discount-heavy regions impacting profit margins.  

### 📊 **Customer Segmentation**  
- Applied **K-Means Clustering** to categorize customer types, identifying repeat customers and potential high-value clients.  

### 🌍 **Geographic Visualizations**  
- Created dynamic HTML maps that provide intuitive insights into sales, discounts, and profit trends across regions.  

---

## **Technologies Used**  
- **Python** (Pandas, NumPy, Seaborn, Matplotlib)  
- **Tableau** for interactive dashboards  
- **SQL** for database management and querying  
- **HTML** for interactive geographic visualizations  
- **PowerPoint** for insights presentation  

---

## **Installation & Usage**  

### **Step 1: Clone the Repository**  
```bash
git clone <repository_url>
cd SuperStoreAnalysis
```

### **Step 2: Install Dependencies**  
```bash
pip install pandas numpy seaborn matplotlib
```

### **Step 3: View Visualizations**  
- Open the `.html` files in your browser to explore interactive maps.  
- Open the `.twb` file in Tableau for detailed insights.  

### **Step 4: Run Python Analysis**  
- Use Jupyter Notebook to run analysis scripts like `BI_EDA.ipynb` and `kmeans_cluster.ipynb`.  

---

## **Future Improvements**  
✅ Incorporate real-time data for dynamic insights  
✅ Develop an automated reporting system for ongoing performance tracking  
✅ Expand customer segmentation with advanced machine learning models  

---

## **Contact**  
For questions, feedback, or collaboration opportunities, feel free to connect with me on [GitHub](https://github.com/enzo253) or via email.  

---
