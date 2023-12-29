import streamlit as st
import pandas as pd
from streamlit_elements import elements, mui, html
from streamlit_elements import nivo
import nivo_chart as nc
st.set_page_config(page_title='Semester Tracker',layout='wide')
st.title("Calculate overall Cgpa")
grades = []
Cgpa = 0.000
n=int(st.number_input("How many semester Have you appered so far ?",min_value=1,max_value=8))
for i in range(n):
    grades.append(float(st.number_input(f'Enter semester {i+1} sgpa ',min_value=5.0,max_value=10.0,step=0.001)))

SemesterGrades = [{"x": i + 1, "y": grades[i]} for i in range(n)]


for i in grades :
    Cgpa = Cgpa + i
# st.info(f"Expected GPA ={Cgpa/n}")
TCgpa = Cgpa/n
stringg = r'''\huge \color{skyblue} \text{ Expected GPA } =  \color{darkorange} '''+str(TCgpa)
st.latex(stringg)

def LineChart():
    with elements("Semester"):
        DATA = [
            {
                "id": "Performance",
                "color": "hsl(191, 70%, 50%)",
                # "color": "hsl(320, 70%, 50%)",
                "data": SemesterGrades
            }
        ]
        with mui.Box(sx={"height": 600}):
            nivo.Line(
                data=DATA,
                margin={ "top": 50, "right": 110, "bottom": 100, "left": 60 },
                xScale={ "type": "point" },
                yScale={
                    "type": "linear",
                    "min": 5,
                    "max": "auto",
                    "stacked": True,
                    "reverse": False
                },
                # yFormat=">-.2f",
                axisTop= None,
                axisRight= None,
                axisBottom={
                    "tickSize": 20,
                    "tickPadding": 15,
                    "tickRotation": 0,
                    "legend": 'Semester',
                    "legendOffset": 90,
                    "legendPosition": 'middle'
                },
                axisLeft={
                    "tickSize": 11,
                    "tickPadding": 13,
                    "tickRotation": 15,
                    "legend": "Grades",
                    "legendOffset": -54,
                    "legendPosition": "middle"
                },
                enableGridX=False,
                enableGridY=False,
                # enableSlices="y",
                colors={ 'scheme': 'accent' },
                enablePointLabel=True,
                pointLabel="y",
                pointLabelYOffset=-24,
                lineWidth=6,
                pointSize=15,
                pointColor={ "theme": "background" },
                pointBorderWidth=5,
                pointBorderColor={ "from": "serieColor" },
                # pointLabelYOffset=-12,
                enableArea=True,
                useMesh=True,
                legends=[
                    {
                        "anchor": "bottom-left",
                        "direction": "column",
                        "justify": True,
                        "translateX": 110,
                        "translateY": 60,
                        "itemsSpacing": 0,
                        "itemDirection": "left-to-right",
                        "itemWidth": 100,
                        "itemHeight": -50,
                        "itemOpacity": 0.75,
                        "symbolSize": 20,
                        'symbolShape': "circle",
                        "symbolBorderColor": "rgba(0, 0, 0, .5)",
                        "effects": [
                            {
                                "on": 'hover',
                                "style": {
                                    "itemBackground": "#0e1016",
                                    "itemOpacity": 1
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#0e1016",
                    "textColor": "#fff",
                    "tooltip": {
                        "container": {
                            "background": "#0e1016",
                            "color": "#fff",
                        }
                    }
                }

                )
st.divider()
st.subheader("Performance :")            
LineChart()