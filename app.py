import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from flask import Flask, render_template, request, jsonify

from sklearn.linear_model import LinearRegression

app = Flask(__name__)

X = None
y = None
model = None
df_rows = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global X, y, model, df_rows

    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected.')

        file = request.files['file']

        # Check if the file has a CSV extension
        if file.filename == '' or not file.filename.endswith('.csv'):
            return render_template('index.html', error='Please select a CSV file.')

        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)

        # Check if the DataFrame has the required columns
        if 'X' not in df.columns or 'Y' not in df.columns:
            return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

        # Assign X and y based on the DataFrame
        X = df['X'].values.reshape(-1, 1)
        y = df['Y'].values

        # Save the first 5 rows of the DataFrame to display in the template
        df_rows = df.head().to_dict(orient='records')

        # Train the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        return render_template('index.html', message='File uploaded successfully.', df_rows=df_rows)

    return render_template('index.html', df_rows=[])

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

    x_value = float(request.form['x'])
    prediction = model.predict([[x_value]])
    return jsonify({'prediction': prediction[0]})

@app.route('/plot', methods=['POST'])
def plot():
    if model is None:
        return render_template('index.html', error='Model not trained. Please upload a dataset first.')

    x_value_str = request.form.get('x')
    if not x_value_str:
        return render_template('index.html', error='Please enter a valid value for X.')

    try:
        x_value = float(x_value_str)
    except ValueError:
        return render_template('index.html', error='Invalid value for X. Please enter a valid number.')

    plt.switch_backend('Agg')
    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

    y_predicted = model.predict([[x_value]])

    plt.scatter(x_value, y_predicted, color='orange', label='Prediction', linewidth=5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.ylim(0, 3000000000)
    plt.xlim(0, 450000000)
    plt.title('Linear Regression on Custom Dataset')
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template('plot_page.html', plot_base64=plot_base64)

if __name__ == '__main__':
    app.run(debug=True)


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO
# from flask import Flask, render_template, request, jsonify

# from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

# X = None
# y = None
# model = None
# df_rows = None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global X, y, model, df_rows

#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file selected.')

#         file = request.files['file']

#         # Check if the file has a CSV extension
#         if file.filename == '' or not file.filename.endswith('.csv'):
#             return render_template('index.html', error='Please select a CSV file.')

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(file)

#         # Check if the DataFrame has the required columns
#         if 'X' not in df.columns or 'Y' not in df.columns:
#             return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

#         # Assign X and y based on the DataFrame
#         X = df['X'].values.reshape(-1, 1)
#         y = df['Y'].values

#         # Save the first 5 rows of the DataFrame to display in the template
#         df_rows = df.head().to_dict(orient='records')

#         # Train the linear regression model
#         model = LinearRegression()
#         model.fit(X, y)

#         return render_template('index.html', message='File uploaded successfully.', df_rows=df_rows)

#     return render_template('index.html', df_rows=[])

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

#     x_value = float(request.form['x'])
#     prediction = model.predict([[x_value]])
#     return jsonify({'prediction': prediction[0]})

# @app.route('/plot', methods=['POST'])
# def plot():
#     if model is None:
#         return render_template('index.html', error='Model not trained. Please upload a dataset first.')

#     x_value_str = request.form.get('x')
#     if not x_value_str:
#         return render_template('index.html', error='Please enter a valid value for X.')

#     try:
#         x_value = float(x_value_str)
#     except ValueError:
#         return render_template('index.html', error='Invalid value for X. Please enter a valid number.')

#     plt.switch_backend('Agg')
#     plt.scatter(X, y, color='blue', label='Data Points')
#     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

#     y_predicted = model.predict([[x_value]])

#     plt.scatter(x_value, y_predicted, color='green', label='Prediction')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Linear Regression on Custom Dataset')
#     plt.legend()

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()

#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     return render_template('index.html', df_rows=df_rows, plot_base64=plot_base64)

# if __name__ == '__main__':
#     app.run(debug=True)



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO
# from flask import Flask, render_template, request, jsonify

# from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

# X = None
# y = None
# model = None
# df_rows = None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global X, y, model, df_rows

#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file selected.')

#         file = request.files['file']

#         # Check if the file has a CSV extension
#         if file.filename == '' or not file.filename.endswith('.csv'):
#             return render_template('index.html', error='Please select a CSV file.')

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(file)

#         # Check if the DataFrame has the required columns
#         if 'X' not in df.columns or 'Y' not in df.columns:
#             return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

#         # Assign X and y based on the DataFrame
#         X = df['X'].values.reshape(-1, 1)
#         y = df['Y'].values

#         # Save the first 5 rows of the DataFrame to display in the template
#         df_rows = df.head().to_dict(orient='records')

#         # Train the linear regression model
#         model = LinearRegression()
#         model.fit(X, y)

#         return render_template('index.html', message='File uploaded successfully.', df_rows=df_rows)

#     return render_template('index.html', df_rows=[])

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

#     x_value = float(request.form['x'])
#     prediction = model.predict([[x_value]])
#     return jsonify({'prediction': prediction[0]})

# @app.route('/plot')
# def plot():
#     if model is None:
#         return render_template('plot.html', error='Model not trained. Please upload a dataset first.')

#     plt.scatter(X, y, color='blue', label='Data Points')
#     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

#     x_value = float(request.args.get('x'))
#     y_predicted = model.predict([[x_value]])

#     plt.scatter(x_value, y_predicted, color='green', label='Prediction')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Linear Regression on Custom Dataset')
#     plt.legend()

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()

#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     return render_template('plot.html', plot=plot_base64)

# if __name__ == '__main__':
#     app.run(debug=True)





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO
# from flask import Flask, render_template, request, jsonify

# from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

# X = None
# y = None
# model = None
# df_rows = None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global X, y, model, df_rows

#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file selected.')

#         file = request.files['file']

#         # Check if the file has a CSV extension
#         if file.filename == '' or not file.filename.endswith('.csv'):
#             return render_template('index.html', error='Please select a CSV file.')

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(file)

#         # Check if the DataFrame has the required columns
#         if 'X' not in df.columns or 'Y' not in df.columns:
#             return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

#         # Assign X and y based on the DataFrame
#         X = df['X'].values.reshape(-1, 1)
#         y = df['Y'].values

#         # Save the first 5 rows of the DataFrame to display in the template
#         df_rows = df.head().to_dict(orient='records')

#         # Train the linear regression model
#         model = LinearRegression()
#         model.fit(X, y)

#         return render_template('index.html', message='File uploaded successfully.', df_rows=df_rows)

#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

#     x_value = float(request.form['x'])
#     prediction = model.predict([[x_value]])
#     return jsonify({'prediction': prediction[0]})

# @app.route('/plot')
# def plot():
#     if model is None:
#         return render_template('plot.html', error='Model not trained. Please upload a dataset first.')

#     plt.scatter(X, y, color='blue', label='Data Points')
#     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

#     x_value = float(request.args.get('x'))
#     y_predicted = model.predict([[x_value]])

#     plt.scatter(x_value, y_predicted, color='green', label='Prediction')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Linear Regression on Custom Dataset')
#     plt.legend()

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()

#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     return render_template('plot.html', plot=plot_base64)

# if __name__ == '__main__':
#     app.run(debug=True)



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO
# from flask import Flask, render_template, request, jsonify

# from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

# X = None
# y = None
# model = None
# df_rows = None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global X, y, model, df_rows

#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file selected.')

#         file = request.files['file']

#         # Check if the file has a CSV extension
#         if file.filename == '' or not file.filename.endswith('.csv'):
#             return render_template('index.html', error='Please select a CSV file.')

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(file)

#         # Check if the DataFrame has the required columns
#         if 'X' not in df.columns or 'Y' not in df.columns:
#             return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

#         # Assign X and y based on the DataFrame
#         X = df['X'].values.reshape(-1, 1)
#         y = df['Y'].values

#         # Save the first 5 rows of the DataFrame to display in the template
#         df_rows = df.head()

#         # Train the linear regression model
#         model = LinearRegression()
#         model.fit(X, y)

#         return render_template('index.html', message='File uploaded successfully.', df_rows=df_rows.to_dict(orient='records'))

#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

#     x_value = float(request.form['x'])
#     prediction = model.predict([[x_value]])
#     return jsonify({'prediction': prediction[0]})

# @app.route('/plot')
# def plot():
#     if model is None:
#         return render_template('plot.html', error='Model not trained. Please upload a dataset first.')

#     plt.scatter(X, y, color='blue', label='Data Points')
#     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

#     x_value = float(request.args.get('x'))
#     y_predicted = model.predict([[x_value]])

#     plt.scatter(x_value, y_predicted, color='green', label='Prediction')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Linear Regression on Custom Dataset')
#     plt.legend()

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()

#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     return render_template('plot.html', plot=plot_base64)

# if __name__ == '__main__':
#     app.run(debug=True)












# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO
# from flask import Flask, render_template, request, jsonify

# from sklearn.linear_model import LinearRegression

# app = Flask(__name__)

# X = None
# y = None
# model = None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global X, y, model

#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file selected.')

#         file = request.files['file']

#         # Check if the file has a CSV extension
#         if file.filename == '' or not file.filename.endswith('.csv'):
#             return render_template('index.html', error='Please select a CSV file.')

#         # Read the CSV file into a Pandas DataFrame
#         df = pd.read_csv(file)

#         # Check if the DataFrame has the required columns
#         if 'X' not in df.columns or 'Y' not in df.columns:
#             return render_template('index.html', error='CSV file must have "X" and "Y" columns.')

#         # Assign X and y based on the DataFrame
#         X = df['X'].values.reshape(-1, 1)
#         y = df['Y'].values

#         # Train the linear regression model
#         model = LinearRegression()
#         model.fit(X, y)

#         return render_template('index.html', message='File uploaded successfully.')

#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model not trained. Please upload a dataset first.'})

#     x_value = float(request.form['x'])
#     prediction = model.predict([[x_value]])
#     return jsonify({'prediction': prediction[0]})

# @app.route('/plot')
# def plot():
#     if model is None:
#         return render_template('plot.html', error='Model not trained. Please upload a dataset first.')

#     plt.scatter(X, y, color='blue', label='Data Points')
#     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')

#     x_value = float(request.args.get('x'))
#     y_predicted = model.predict([[x_value]])

#     plt.scatter(x_value, y_predicted, color='green', label='Prediction')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Linear Regression on Custom Dataset')
#     plt.legend()

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()

#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     return render_template('plot.html', plot=plot_base64)

# if __name__ == '__main__':
#     app.run(debug=True)













# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import base64
# # from io import BytesIO
# # from flask import Flask, render_template, request, jsonify

# # from sklearn.linear_model import LinearRegression


# # app = Flask(__name__)

# # # Load your custom dataset
# # custom_data = pd.read_csv('cost-revenue-clean.csv')
# # X = custom_data['production_budget_usd'].values.reshape(-1, 1)
# # y = custom_data['worldwide_gross_usd'].values


# # # Train the model
# # model = LinearRegression()
# # model.fit(X, y)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/predict')
# # def predict():
# #     x_value = float(request.args.get('x'))
# #     prediction = model.predict([[x_value]])
# #     return jsonify({'prediction': prediction[0]})

# # @app.route('/plot')
# # def plot():

# #     # plt.subplot(1,2,1)
# #     # plt.scatter(X, y, color='blue', label='Data Points')
# #     # # plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')
# #     # plt.xlabel('production_budget_usd')
# #     # plt.ylabel('worldwide_gross_usd')
# #     # plt.title('Film Cost VS world wide revenue')
# #     # plt.legend()

# #     # plt.subplot(1,2,1)
# #     # plt.scatter(X, y, color='blue', label='Data Points')
# #     # plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')
# #     # plt.xlabel('production_budget_usd')
# #     # plt.ylabel('worldwide_gross_usd')
# #     # plt.title('Linear Regression on Custom Dataset')
# #     # plt.legend()


# #     plt.scatter(X, y, color='blue', label='Data Points',alpha=0.3)
# #     plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')
# #     plt.ylim(0, 3000000000);
# #     plt.xlim(0, 450000000);
# #     plt.xlabel('production_budget_usd')
# #     plt.ylabel('worldwide_gross_usd')
# #     plt.title('Linear Regression on Custom Dataset')
# #     plt.legend()



# #     # Save the plot to a BytesIO buffer
# #     buffer = BytesIO()
# #     plt.savefig(buffer, format='png')
# #     buffer.seek(0)
# #     plt.close()

# #     # Encode the plot to base64 to embed in the HTML
# #     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

# #     return render_template('plot.html', plot=plot_base64)

# # if __name__ == '__main__':
# #     app.run(debug=True)
