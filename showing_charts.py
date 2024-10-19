import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_ch(py_code):
    print(py_code)
    exec(py_code)