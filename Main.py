import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Clean_data(data):
    # data = pd.read_excel("Data1.xlsx")
    print(data)

    print("\n \n \n")
    data["EmpSalary"] = data["EmpSalary"].fillna(0)
    data["EmpBonus"] = data["EmpBonus"].fillna(0)
    data.fillna("NULL", inplace=True)
    data.to_excel("Data_cleaned.xlsx", index=False)
    print(data)


def DropDuplicate(data):
    cleanData = data.drop_duplicates()
    print("Uniue data : \n")
    data.to_excel("data_unique.xlsx", index=False)
    print(cleanData)


def CapitalData(data):
    data["EmpName"] = data["EmpName"].str.title()
    data.to_excel("Data_capital.xlsx",index=False)
    print(data)

#
def find_Avg(data):
    Avg_sal = data["Total Salary"].mean()
    print("\n Average of total salary : ",Avg_sal)

    data["Total Salary"] = data["EmpSalary"] + data["EmpBonus"]
    # print(data["Total Salary"])
    data.to_excel("Data1.xlsx",index=False)


def find_sum(data):
    Sum_sal = data["Total Salary"].sum()
    print("\n Sum of total salary : ",Sum_sal)

def find_min(data):
    minSal = data["Total Salary"].min()
    print("\n minimum of total salary : ",minSal)

def find_max(data):
    maxSal = data["Total Salary"].max()
    print("\n Maximum of total salary : ",maxSal)

def sortSalary(data):
    sortedSalary = data.sort_values(by='EmpSalary', ascending=True)
    print(sortedSalary)


#

def BarPlot(data):
    Salary = data["Total Salary"]
    dept = data["EmpAddress"]
    plt.bar(dept,Salary)
    plt.title("Salary Bar graph City Wise")
    plt.xlabel("Address")
    plt.ylabel("Salary")
    plt.show()
   
def ScatterPlot(data):
    x = data["age"]
    y=data["EmpSalary"]
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.title("Age wise salary")
    plt.scatter(x, y, color='teal', marker='o', edgecolors='blue')
    plt.show()

def histogram(data):
    showdata = data["age"]
    plt.hist(showdata,bins=10, color='orange', edgecolor='black')
    plt.show()


data = pd.read_excel("Data.xlsx")
data2 = pd.read_excel("data_uncleaned.xlsx")


# Clean_data(data2)
# DropDuplicate(data2)
CapitalData(data)

find_Avg(data)
find_sum(data)
find_min(data)
find_max(data)
# sortSalary(data)

# BarPlot(data)
# ScatterPlot(data)
# histogram(data)






