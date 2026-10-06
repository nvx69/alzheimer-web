from flask import Flask, request, jsonify, send_from_directory
import pickle, os

BASE=os.path.dirname(os.path.abspath(__file__))
app=Flask(__name__, static_folder=BASE, static_url_path='')
with open(os.path.join(BASE,'model.pkl'),'rb') as f:
    model=pickle.load(f)

FIELDS=['age','bmi','gender','bp','diabetes','chol','exercise','smoke','sleep','family','memory']

def row_from(data):
    # gender is included for demographic completeness but has no scoring weight.
    return [
        float(data['age']), float(data['bmi']), str(data.get('gender','male')),
        int(data.get('bp',0)), int(data.get('diabetes',0)), int(data.get('chol',0)),
        int(data.get('exercise',0)), int(data.get('smoke',0)), int(data.get('sleep',0)),
        int(data.get('family',0)), int(data.get('memory',0))
    ]

@app.after_request
def cors(resp):
    resp.headers['Access-Control-Allow-Origin']='*'
    resp.headers['Access-Control-Allow-Headers']='Content-Type'
    return resp

@app.get('/')
def home():
    return send_from_directory(BASE,'index.html')

@app.post('/api/predict')
def predict():
    data=request.get_json(silent=True) or {}
    missing=[f for f in ['age','bmi'] if f not in data]
    if missing:
        return jsonify(error='Missing fields: '+', '.join(missing)),400
    try:
        age=float(data['age'])
        bmi=float(data['bmi'])

        if age > 100:
            return jsonify(error='Age cannot exceed 100 years.'),400
        if bmi > 50:
            return jsonify(error='BMI cannot exceed 50.'),400
        if age <= 0 or bmi <= 0:
            return jsonify(error='Age and BMI must be greater than 0.'),400

        row=row_from(data)
        score=model.predict_score(row)
        level='low' if score<30 else ('medium' if score<60 else 'high')
        return jsonify(score=score, level=level, gender=row[2], model='model.pkl', disclaimer='Educational screening only; not a medical diagnosis.')
    except (ValueError,TypeError,KeyError) as e:
        return jsonify(error=str(e)),400

if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=False)
