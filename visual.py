import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    slices=list(categories.values())
    print(slices)
    nos=[]
    nos.append(int(len(slices[0])))
    nos.append(int(len(slices[1])))
    labels=list(categories.keys())
    print(labels)
    print(nos)
    plt.pie(nos,labels=labels,autopct='%1.1f%%',shadow=True)
    plt.title("Pie Chart")
    plt.legend()
    plt.show()
#entities_pie({"Planets": ["Earth", "Mars", "Jupiter"], "non-planets":["star", "moon"]})
def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    x=list(categories.values())
    x1=[]
    x1.append(len(x[0]))
    x1.append(len(x[1]))
    x1.append(len(x[2]))
    #print(x1)
    labels=list(categories.keys())
    print(labels)
    plt.bar(labels,x1, width=0.3)
    plt.xlabel("Category")
    plt.ylabel("Number of Entries")
    plt.show()
#entities_bar({"low":[1,4,5,6],"medium":[7,8,9], "high":[12,4,6]})

def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    keys=summary.keys()
    for i in keys:
        orbtd=summary[i]
        labels=orbtd.keys()
        print(labels)
        v=list(orbtd.values())
        v1=[]
        v1.append(len(v[0]))
        v1.append(len(v[1]))
        print(v1)
        plt.bar(labels,v1, width=0.3)
        plt.xlabel("Category Type")
        plt.ylabel("Number of Entries")
        plt.title(i)
        plt.show()
#orbits({"orbited planet": {"small": ["entity1", "entity2", "entity3"],"large": ["entity", "entity"]},"orbited planet1": {"small": ["entity11", "entity21", "entity31"],"large": ["entity1", "entity1"]}})

def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    x = list(categories.values())
    x1 = []
    x1.append(len(x[0]))
    x1.append(len(x[1]))
    x1.append(len(x[2]))
    print(x1)
    labels = list(categories.keys())
    #represents the labels in numeric form
    labelsn=[1,2,3]
    print(labels)
    style.use('fivethirtyeight')
    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    def animate(i):
        xs=[]
        ys=[]
        for l in range(len(x1)):
            xs.append(float(labelsn[l]))
            ys.append(float(x1[l]))

        ax1.clear()
        ax1.plot(xs,ys)
        plt.xlabel("(Category)1-Low, 2-medium ,3-high")
        plt.ylabel("Number")
        plt.title('Gravity Animation')

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()



    '''
    def an(i):
        ax1.clear()
        ax1.plot(x1,labelsn)
    ani=animation.FuncAnimation(fig,an,interval=100000000000)
    plt.show()
    '''

'''
    fig, ax =plt.subplots()
    ax.set_xlim(0,105)
    ax.set_ylim(0,12)
    line,=ax.plot(0,0)
    def ani():
        line.set_xdata(labels)
        line.set_ydata(x1)
        return line,
    animation=FuncAnimation(fig,func=ani(), frames=np.arange(0,10,0.01), interval=10)
    plt.show()
'''

#gravity_animation({"low":[1,4,5,6],"medium":[7,8,9], "high":[12,4,6]})

