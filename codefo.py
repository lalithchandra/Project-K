from flask import Flask,render_template,request
app=Flask(_name_)
@app.route('/')
def home():
    return render_template('index.html')
with open('project.pkl','rb')as f:
    model=pickle.load(f)
@app.route('/',methods=['GET'])
def predict():
    Score = int(request.form['score'])
    Q1 = int(request.form['question1'])
    Q2 = int(request.form['question2'])
    Q3 = int(request.form['question3'])
    Q4 = int(request.form['question4'])
    Q5 = int(request.form['question5'])
    Q6 = int(request.form['question6'])
    #now take the above form data and convert to array
    input_data = np.array([[Score,Q1,Q2]])
    #by taking above data we will predict the House_price
    prediction = model.predict(input_data)[0]
    #now we will pass above predicted data to template
    return render_template('index.html',
                           prediction = prediction)
app.run()
