


<h1 align="center">Data Mining a Divorce Dataset</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/mitchellkolb/divorce-dataset?color=013243">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/mitchellkolb/divorce-dataset?color=013243">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mitchellkolb/divorce-dataset?color=013243">

  <img alt="Github stars" src="https://img.shields.io/github/stars/mitchellkolb/divorce-dataset?color=013243" />
</p>

<p align="center">
<img
    src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"
    alt="Website Badge" />
</p>

I used data mining techniques like Agglomerative Clustering and Statistical Analysis on a dataset of people who were asked questions after they were divorced, to analyze and draw conclusions.

![project image](resources/divorce.gif)

<details>
<summary style="color:#5087dd">Watch the Full Video Demo Here</summary>

[![Full Video Demo Here](https://img.youtube.com/vi/zz9x_9CdKhU/0.jpg)](https://www.youtube.com/watch?v=zz9x_9CdKhU)

</details>

---


# Table of Contents
- [What I Learned](#what-i-learned-in-this-project)
- [Tools Used / Development Environment](#tools-used--development-environment)
- [Team / Contributors / Teachers](#team--contributors--teachers)
- [How to Set Up](#how-to-set-up)
- [Project Overview](#project-overview)
- [Project Details](#project-details)
- [Dataset](#dataset)
- [Technical Skills Used](#technical-skills-used)
- [Results and Observations](#results-and-observations)
- [Acknowledgments](#acknowledgments)

---

# What I Learned in this Project
- How to use **Pandas** to clean and preprocess data, for effective data manipulation.
- How to apply **Agglomerative Clustering** with scikit-learn to identify patterns and predictors of divorce.
- How to conduct **Statistical Analysis** to calculate key metrics, providing insights into significant divorce factors.
- How to utilize **Matplotlib** to create visualizations that enhance the interpretation of clustering results and response distributions.



# Tools Used / Development Environment
- Python
- Pandas
- Numpy
- Matplotlib
- VS Code
- Terminal





# Team / Contributors / Teachers
- [Mitchell Kolb](https://github.com/mitchellkolb)
- Professor. Reet Barik





# How to Set Up
This project was implemented on my windows laptop:
- Clone this repository 
- Open terminal at the codebase `~.../divorce-dataset/Project315Mk/`
- Install the needed libraries:
    -  ```bash pip install pandas numpy ```
    -  ```bash python -m pip install -U matplotlib ```
    -  ```bash pip install -U scikit-learn ```
- Run `project315.py` and check the results.txt for the output




# Project Overview
This project utilizes data mining techniques to analyze the Divorce Predictors Data Set from the UC Irvine Machine Learning Repository. The objective is to discover patterns and predictors of divorce by applying clustering and other data mining methods to the dataset.

## Project Details
The goal of this project is to investigate the predictors of divorce by analyzing responses to a questionnaire. The dataset contains 170 entries, each with answers to 54 questions, which are rated on a scale from 1 (bad/low) to 4 (excellent/high). The analysis aims to identify key factors contributing to divorce and explore whether clustering can effectively group responses to reveal significant patterns.

## Dataset
The dataset used in this project is the Divorce Predictors Data Set from the UC Irvine Machine Learning Repository. It includes 170 responses to a questionnaire with 54 questions designed to assess various aspects of marital relationships. Each response is labeled with a class attribute indicating whether the respondent is from a couple that is divorced (1) or not divorced (0). The dataset is available at [UC Irvine Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/divorce+predictors+data+set).

## Technical Skills Used
The project employs a range of data mining techniques and tools, including:
- **Python**: For data processing and analysis.
- **Pandas**: For data manipulation and cleaning.
- **Scikit-learn**: For applying clustering algorithms.
- **Matplotlib**: For visualizing the results of the data analysis.
- **Agglomerative Clustering**: To identify patterns and group similar responses.

## Results and Observations
- **Data Grouping**: The dataset was divided into two groups based on the class attribute. Group 1 included responses from couples that are divorced, while Group 2 included responses from couples that are not divorced.
- **Key Findings**: Analysis revealed that communication and intimacy issues were the most significant predictors of divorce. Group 1 showed a higher degree of dissatisfaction in these areas compared to Group 2.
- **Clustering Effectiveness**: The use of agglomerative clustering effectively grouped responses and highlighted areas of agreement and disagreement among respondents. This method provided clear visualizations of the most common responses and their distribution.
- **Statistical Analysis**: The maximum, minimum, and mean values for each question were calculated for both groups, showing distinct differences in how each group responded to the questionnaire.



--- 
# Acknowledgments
This codebase and all supporting materials was made as apart of a course for my undergrad at WSU for CPTS 315 - Introduction to Data Mining in the Fall of 2022. 

