class AlzheimerRiskModel:
    """Educational rule-based model saved with pickle; not a medical diagnostic model."""
    def predict_score(self, row):
        age,bmi,gender,bp,diabetes,chol,exercise,smoke,sleep,family,memory = row
        s=0
        if age>=80: s+=25
        elif age>=70: s+=18
        elif age>=60: s+=10
        if bmi>=30: s+=8
        s += 1 if bp==1 else (8 if bp==2 else 0)
        s += 7*diabetes
        s += 5 if chol==2 else 0
        s += 7 if exercise==1 else (-2 if exercise==2 else 0)
        s += 5*smoke + 5*sleep + 15*family + 20*memory
        return max(0,min(100,round(s)))
    def predict_proba(self, rows):
        out=[]
        for row in rows:
            score=self.predict_score(row)/100
            out.append([1-score, score])
        return out
    def predict(self, rows):
        return [1 if self.predict_score(r)>=60 else 0 for r in rows]
