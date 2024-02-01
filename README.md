# bill-authentication-predictions

![Code_4Y983w2he7](https://github.com/MisterAare/bill-authentication-predictions/assets/109184556/4f72f5da-10f4-4598-a99e-7bf72a883719)

### Dataset:

The dataset used for this project is the "Bill Authentication" dataset obtained from Kaggle. It consists of the following variables:

- Variance: A statistical measurement of the spread between numbers in a data set.
- Skewness: A measure of asymmetry or deviation from the normal distribution.
- Curtosis: Indicates how sharply a probability distribution function increases and decreases around the mean.
- Entropy: Measures the impurity, disorder, or uncertainty in a set of examples.
- Class: The target variable used to classify the quality of bill authentication based on the above variables.

### Libraries and Frameworks:

The Python libraries used in this project include pandas, numpy, scikit-learn, matplotlib, pickle, Flask, and other related libraries for data manipulation, model building, visualization, and deployment.

### Model Building:

For this project, a Decision Tree model was used with an accuracy score of 0.9 for the test data and 1 for the train data, indicating good generalization. The independent variables (Variance, Skewness, Curtosis, Entropy) were used to predict the dependent variable (Class). The model was evaluated using a classification report and confusion matrix. Additionally, a feature importance visualization indicated the contribution of each variable to the model's prediction.

### Deployment:

The model was deployed using the Flask framework along with HTML and CSS for the user interface. Users can input values for Variance, Skewness, Curtosis, and Entropy, and the model predicts the authenticity of the bill based on these features.

