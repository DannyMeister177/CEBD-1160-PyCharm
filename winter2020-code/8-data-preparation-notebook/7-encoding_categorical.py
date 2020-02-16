from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

np.warnings.filterwarnings('ignore')

titanic = pd.read_csv('data/titanic/train.csv')
titanic['Embarked'] = titanic['Embarked'].fillna(value='S')

# Overall exploration before cleanup
print('\n\n********************************** Dataset BEFORE Cleanup ***************************************')
print(titanic.head(4).to_string())

# Encoding categorical variables using dummy variables
print('\n\n********************************** Dummy Encoded ***************************************')
encoded_sex = pd.get_dummies(titanic['Sex'], drop_first=True)
encoded_embarked = pd.get_dummies(titanic['Embarked'], drop_first=True)
dummy_encoded = pd.concat([titanic, encoded_sex, encoded_embarked], axis=1)
print(dummy_encoded.head(4).to_string())


# Encoding categorical variables using LabelEncoder
print('\n\n********************************** Label Encoded ***************************************')
le = LabelEncoder()
label_encoded_categories = titanic[['Sex', 'Embarked']].apply(lambda col: le.fit_transform(col))
label_encoded_df = pd.concat([titanic, label_encoded_categories], axis=1)
print(label_encoded_df.head(4).to_string())

# Encoding categorical variables using OneHotEncoder - to be done
print('\n\n********************************** OneHot Encoded ***************************************')
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [4])],
    remainder='passthrough'
)

x = np.array(ct.fit_transform(titanic))
print(pd.DataFrame(x, columns=titanic.columns))