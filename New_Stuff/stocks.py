import numpy
import pandas
import matplotlib.pyplot
import seaborn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

from IPython.display import display

import warnings

warnings.filterwarnings("ignore")


df = pandas.read_csv(
    r"D:\Coding\VSCode\Directories\PythonBeginner\Python-Beginner\New_Stuff\data_folder\TSLA.csv"
)
display(df.head())
print(df.shape())
