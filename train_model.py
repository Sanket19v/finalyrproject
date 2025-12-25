import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load your data
df = pd.read_csv('data.csv')

# Use only the fields needed
FIELDS = [
    'Fwd Packet Length Max', 'Avg Fwd Segment Size', 'Subflow Fwd Bytes',
    'Total Length of Fwd Packets', 'Flow IAT Max', 'Average Packet Size',
    'Bwd Packet Length Std', 'Flow Duration', 'Avg Bwd Segment Size',
    'Bwd Packets/s', 'Packet Length Mean', 'Init_Win_bytes_forward',
    'Init_Win_bytes_backward', 'Packet Length Std', 'Fwd IAT Max',
    'Fwd Packet Length Std', 'Packet Length Variance',
    'Flow Packets/s', 'Fwd Packet Length Mean', 'Total Length of Bwd Packets'
]

# Encode labels
le = LabelEncoder()
df['Label'] = le.fit_transform(df['Label'])

X = df[FIELDS]
y = df['Label']

# Train a basic model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# Save label mapping
class_mapping = dict(zip(le.transform(le.classes_), le.classes_))
with open('class_mapping.pkl', 'wb') as f:
    pickle.dump(class_mapping, f)

print("✅ model.pkl and class_mapping.pkl saved!")
