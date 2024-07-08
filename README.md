# Methods of Advanced Data Engineering 
# Jayvee Exercises (Exercise Badges)

![](https://byob.yarr.is/FerdoushiNahar/MADE_SS_2024/score_ex1) ![](https://byob.yarr.is/FerdoushiNahar/MADE_SS_2024/score_ex2) ![](https://byob.yarr.is/FerdoushiNahar/MADE_SS_2024/score_ex3) ![](https://byob.yarr.is/FerdoushiNahar/MADE_SS_2024/score_ex4) ![](https://byob.yarr.is/FerdoushiNahar/MADE_SS_2024/score_ex5)

# Project: "Climate Change: Greenhouse Gas(Co2) Emissions and Temperature Trends in Rathaus area of konstanz"
<img src="project\image\konstanz.jpg" width="800" height="466">

## Main Question
1.How do Greenhouse Gas (CO₂) emissions affect climate change in the Rathaus area of Konstanz?

## Project Overview
This project aims to explore the relationship between Greenhouse Gas (CO₂) emissions and regional temperature trends in the Rathaus area of Konstanz. By analyzing historical data on CO₂ levels and temperature records, we aim to identify patterns and correlations that can provide insights into the impact of greenhouse gas emissions on local climate changes. The study seeks to contribute to the understanding of how human activities influence environmental conditions, which is essential for developing effective climate policies and mitigation strategies. This analysis will leverage publicly available datasets to examine temporal trends and potential causal relationships, offering a localized perspective on the broader issue of global climate change.
### Datasets
For this project we are using two open data sources [**Greenhouse Data**](https://offenedaten-konstanz.de/dataset/co-werte-konstanz) contains information on greenhouse gas emissions specifically Co2 in Rathaus area of konstanz and [**Temperature Data**](https://offenedaten-konstanz.de/dataset/temperaturwerte-konstanz) which provides information on temperatuure trend in Rathaus area of konstanz.



## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
