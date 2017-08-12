class Employee:

    def __init__(self, name, ID, department, job):

        self.__name = name
        self.__id = ID
        self.__department = department
        self.__job = job

    def __str__(self):

        return "Name: " + self.__name + \
                "\n ID: " + self.__id + \
                "\n Department: " + self.__department + \
                "\n Job: " + self.__job



def main():

    dict = {}

    s_n = "Susan Meyers"
    s_id = "47899"
    s_department = "Accounting"
    s_title = "Vice President"

    m_n = "Mark Jones"
    m_id = "39119"
    m_department = "IT"
    m_title = "Programmer"

    j_n = "Joy Rogers"
    j_id = "81774"
    j_department = "Manufacturing"
    j_title = "Engineer"

    employee_susan = Employee(s_n, s_id, s_department, s_title)
    employee_mark = Employee(m_n, m_id, m_department, m_title)
    employee_joy = Employee(j_n, j_id, j_department, j_title)

    #print(employee_susan)

    dict[s_n] = (employee_susan)
    dict[m_n] = (employee_mark)
    dict[j_n] = (employee_joy)

    for x in dict:
        print(dict[x])

    #print(dict[s_n])
    #print(dict)

main()
