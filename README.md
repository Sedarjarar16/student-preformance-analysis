# Student Performance Analysis
## Dataset

This project uses the Student Performance dataset from the UCI Machine Learning Repository.

- Source: UCI Machine Learning Repository
- Dataset: Student Performance
- Instances: 649 students
- Features: 30
- Target: Final grade (G3)

The dataset contains student information and academic-related attributes collected from two Portuguese secondary schools.
## Methodology

The analysis was performed using Python and included:

- Loading the dataset using ucimlrepo
- Checking the dataset structure and missing values
- Exploring the relationship between study time and final grade
- Analyzing absences and their relationship with final grade
- Comparing previous failures with final grade
- Measuring correlations between previous grades (G1, G2) and final grade (G3)
- Creating visualizations using Matplotlib

## Results

### Absences vs Final Grade

The correlation between the number of absences and the final grade (G3) was:

*r = -0.091*

This indicates a very weak negative linear relationship between absences and final grade in the dataset.
### Previous Failures vs Final Grade
Students with no previous failures had an average final grade of 12.51. Students with one or more previous failures had lower average final grades, ranging from 8.07 to 8.81 across the failure groups.
This shows a noticeable association between previous failures and final grade in the dataset.
### Study Time vs Final Grade

Students with higher weekly study-time levels generally had higher average final grades.

The average G3 increased from 10.84 for study-time level 1 to 13.23 for level 3. Level 4 had a similar average of 13.06, but it represented only 35 students.

This suggests an association between study-time level and final grade, with the clearest increase observed from levels 1 to 3.
### Previous Grades vs Final Grade

Previous grades showed strong positive correlations with the final grade.

- G1 vs G3: r = 0.826
- G2 vs G3: r = 0.919

G2 showed a stronger correlation with G3 than G1. Since G1 and G2 are previous-period grades for the same students, these results indicate a strong predictive/associative relationship rather than a causal effect.
## Limitations

- The analysis shows associations between variables and final grades, but it does not establish causation.
- The dataset was collected from two Portuguese secondary schools, so the findings may not generalize to all students or educational systems.
- Study-time level 4 contains only 35 students, which makes comparisons with the other study-time groups less reliable.
- G1 and G2 are previous-period grades, so their strong correlation with G3 should be interpreted as predictive or associative rather than causal.