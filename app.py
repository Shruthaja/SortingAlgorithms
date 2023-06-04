from urllib import request
from flask import *
import random
import time
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
pd.options.plotting.backend = "plotly"
import threepointquicksort
from heapsort import *
from mergesort import *
from quicksort import *
from insertionsort import *
from selectionsort import *
from bubblesort import *
app = Flask(__name__, static_url_path='/', static_folder="C:/Users/shrut/PycharmProjects/SortingAlgorithms/static")

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    table=""
    html=""
    randomlist = []
    randomlist100 = []
    randomlist1000 = []
    randomlist10000 = []
    randomlist100000=[]
    for i in range(0, 10):
        n = random.randint(1, 10)
        randomlist.append(n)
    for i in range(0, 100):
        n = random.randint(100, 1000)
        randomlist100.append(n)
    for i in range(0, 1000):
        n = random.randint(1, 10000)
        randomlist1000.append(n)
    for i in range(0, 10000):
        n = random.randint(1, 100000)
        randomlist10000.append(n)
    for i in range(0, 25000):
        n = random.randint(0, 1000000)
        randomlist100000.append(n)
    if request.method == 'POST':
        selectedsort = request.form['select']
        if (selectedsort == "MergeSort"):
            start1 = time.time()
            mergesort(randomlist)
            end1 = time.time()
            start2 = time.time()
            mergesort(randomlist100)
            end2 = time.time()
            start3 = time.time()
            mergesort(randomlist10000)
            end3 = time.time()
            start4 = time.time()
            mergesort(randomlist1000)
            end4 = time.time()
            start5 = time.time()
            mergesort(randomlist100000)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000,100000], y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3,end5-start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "QuickSort"):
            start1 = time.time()
            quickSort(randomlist, 0, len(randomlist) - 1)
            end1 = time.time()
            start2 = time.time()
            quickSort(randomlist100, 0, len(randomlist100) - 1)
            end2 = time.time()
            start3 = time.time()
            quickSort(randomlist10000, 0, len(randomlist10000) - 1)
            end3 = time.time()
            start4 = time.time()
            quickSort(randomlist1000, 0, len(randomlist1000) - 1)
            end4 = time.time()
            start5 = time.time()
            quickSort(randomlist100000,0, len(randomlist100000) - 1)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]

            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "HeapSort"):
            start1 = time.time()
            heapSort(randomlist)
            end1 = time.time()
            start2 = time.time()
            heapSort(randomlist100)
            end2 = time.time()
            start3 = time.time()
            heapSort(randomlist10000)
            end3 = time.time()
            start4 = time.time()
            heapSort(randomlist1000)
            end4 = time.time()
            start5 = time.time()
            heapSort(randomlist100000)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "3pointQuickSort"):
            start1 = time.time()
            threepointquicksort.quicksort(randomlist, 0, len(randomlist) - 1)
            end1 = time.time()
            start2 = time.time()
            threepointquicksort.quicksort(randomlist100, 0, len(randomlist100) - 1)
            end2 = time.time()
            start3 = time.time()
            threepointquicksort.quicksort(randomlist10000, 0, len(randomlist10000) - 1)
            end3 = time.time()
            start4 = time.time()
            threepointquicksort.quicksort(randomlist1000, 0, len(randomlist1000) - 1)
            end4 = time.time()
            start5 = time.time()
            threepointquicksort.quicksort(randomlist100000,0, len(randomlist100000) - 1)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "InsertionSort"):
            start1 = time.time()
            insertion_sort(randomlist)
            end1 = time.time()
            start2 = time.time()
            insertion_sort(randomlist100)
            end2 = time.time()
            start3 = time.time()
            insertion_sort(randomlist10000)
            end3 = time.time()
            start4 = time.time()
            insertion_sort(randomlist1000)
            end4 = time.time()
            start5 = time.time()
            selectionsort(randomlist100000)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "BubbleSort"):
            start1 = time.time()
            bubblesort(randomlist)
            end1 = time.time()
            start2 = time.time()
            bubblesort(randomlist100)
            end2 = time.time()
            start3 = time.time()
            bubblesort(randomlist10000)
            end3 = time.time()
            start4 = time.time()
            bubblesort(randomlist1000)
            end4 = time.time()
            start5 = time.time()
            bubblesort(randomlist100000)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
        elif (selectedsort == "SelectionSort"):
            start1 = time.time()
            selectionsort(randomlist)
            end1 = time.time()
            start2 = time.time()
            selectionsort(randomlist100)
            end2 = time.time()
            start3 = time.time()
            selectionsort(randomlist10000)
            end3 = time.time()
            start4 = time.time()
            selectionsort(randomlist1000)
            end4 = time.time()
            start5 = time.time()
            selectionsort(randomlist100000)
            end5 = time.time()
            data = [go.Scatter(x=[10, 100, 1000, 10000, 100000],
                           y=[end1 - start1, end2 - start2, end4 - start4, end3 - start3, end5 - start5])]
            fig = go.Figure(data=data)
            html = pio.to_html(fig)
            table = """<table id='tablearray' > <h2>Time taken to sort arrays for """ + selectedsort + """</h2> <tr> <td>""" + str(10) + """</td> <td>""" + str(100) + """</td> <td>""" + str(1000) + """</td> <td>""" + str(10000) + """</td> <td>""" + str(25000) + """</td> </tr> <tr> <td>""" + str(end1 - start1) + """</td> <td>""" + str(end2 - start2) + """</td> <td>""" + str(end4 - start4) + """</td> <td>""" + str(end3 - start3) + """</td> <td>""" + str(end5 - start5) + """</td> </tr></table><style> table, th, td { border: 1px solid black; border-collapse: collapse; }</style>"""
            return render_template("results.html", table=table,sortedarray=randomlist100,plotly_figure=html)
    return render_template("index.html", table=table, sortedarray=randomlist100, plotly_figure=html)

if (__name__ == "__main__"):
    app.run(debug=True)