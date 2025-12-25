from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data
users = {
    'admin': {'password': 'admin123'},
    'test': {'password': 'test123'}
}

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define the expected fields for manual form input
FIELDS = [
    'Fwd Packet Length Max', 'Avg Fwd Segment Size', 'Subflow Fwd Bytes',
    'Total Length of Fwd Packets', 'Flow IAT Max', 'Average Packet Size',
    'Bwd Packet Length Std', 'Flow Duration', 'Avg Bwd Segment Size',
    'Bwd Packets/s', 'Packet Length Mean', 'Init_Win_bytes_forward',
    'Init_Win_bytes_backward', 'Packet Length Std', 'Fwd IAT Max',
    'Fwd Packet Length Std', 'Packet Length Variance',
    'Flow Packets/s', 'Fwd Packet Length Mean', 'Total Length of Bwd Packets'
]


# Class labels mapping from prediction output
CLASS_MAPPING = {
    0: 'BENIGN',
    1: 'DoS Hulk',
    2: 'DDoS',
    3: 'PortScan',
    4: 'DoS GoldenEye'
}
# Load the label mapping
with open('class_mapping.pkl', 'rb') as f:
    CLASS_MAPPING = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    results = []  # to hold (index, label) pairs for display
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in request.', 'error')
            return redirect(url_for('dashboard'))

        file = request.files['file']
        if file.filename == '':
            flash('No selected file.', 'error')
            return redirect(url_for('dashboard'))

        try:
            df = pd.read_csv(file)
            # Drop 'Label' if it exists
            if 'Label' in df.columns:
             df = df.drop('Label', axis=1)
            predictions = model.predict(df)

            # Mapping predictions to readable labels
            for i, pred in enumerate(predictions, 1):
                label = CLASS_MAPPING.get(int(pred), 'Unknown')
                results.append({
                    'sr': i,
                    'index': int(pred),
                    'label': label
                })

            flash('Prediction completed successfully!', 'success')

        except Exception as e:
            flash(f'Error processing file: {e}', 'error')

    return render_template('dashboard.html', username=session['username'], results=results, fields=FIELDS)

@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        df = pd.read_csv(file)
        if 'Label' in df.columns:
          df = df.drop('Label', axis=1)
        predictions = model.predict(df)

        results = []
        for i, pred in enumerate(predictions):
            results.append({
                'sr': i + 1,
                'index': int(pred),
                'label': CLASS_MAPPING.get(int(pred), 'Unknown')
            })

        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500



@app.route('/predict_single', methods=['POST'])
def predict_single():
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        input_data = [float(request.form.get(field)) for field in FIELDS]
        df = pd.DataFrame([input_data], columns=FIELDS)
        prediction = model.predict(df)[0]
        label = CLASS_MAPPING.get(prediction, "Unknown")

        return jsonify({'result': label})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))

    predictions = []

    if request.method == 'POST':
        file = request.files.get('file')
        if not file or not file.filename.endswith('.csv'):
            flash("Please upload a valid CSV file.", "error")
            return redirect(url_for('upload'))

        try:
            df = pd.read_csv(file)
            if 'Label' in df.columns:
                df = df.drop('Label', axis=1)

            preds = model.predict(df)

            for i, pred in enumerate(preds):
                predictions.append({
                    'sr': i + 1,
                    'index': int(pred),
                    'label': CLASS_MAPPING.get(int(pred), 'Unknown')
                })

        except Exception as e:
            flash(f"Error during prediction: {str(e)}", "error")

    return render_template('upload.html', predictions=predictions)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
