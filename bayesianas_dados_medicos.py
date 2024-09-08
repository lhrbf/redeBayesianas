import pandas as pd
from sklearn.datasets import load_diabetes
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['diabetes'] = data.target

threshold = df['diabetes'].median()
df['diabetes'] = (df['diabetes'] > threshold).astype(int)

model = BayesianNetwork([
    ('age', 'diabetes'),
    ('bmi', 'diabetes'),
    ('bp', 'diabetes'),
    ('s1', 'diabetes'),
    ('s2', 'diabetes'),
    ('s3', 'diabetes'),
    ('s4', 'diabetes'),
    ('s5', 'diabetes'),
    ('s6', 'diabetes')
])

model.fit(df, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

evidence = {
    'age': 50,
    'bmi': 30,
    'bp': 80,
    's1': 0,
    's2': 0,
    's3': 0,
    's4': 0,
    's5': 0,
    's6': 0
}

query_result = infer.map_query(variables=['diabetes'], evidence=evidence)
print(f"Probabilidade de diabetes: {query_result['diabetes']}")

train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)

model.fit(train_df, estimator=MaximumLikelihoodEstimator)

true_values = test_df['diabetes']
predictions = [infer.map_query(variables=['diabetes'], evidence=row.to_dict())['diabetes'] for _, row in test_df.iterrows()]

accuracy = accuracy_score(true_values, predictions)
print(f'Acurácia do modelo: {accuracy:.2f}')