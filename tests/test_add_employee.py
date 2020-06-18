import pdb

from faker import Faker

from HRMpytestProject import HRM

hrm = HRM()


def test_add_employee_success():
    """
    make sure if we call function with correct parameters
    1. user login
    2. create valid employee request data
    3. call function add_employee  with employee data
    4. ensure that employee was created
    """
    # l1.login
    resp = hrm.login()
    # 2
    f = Faker()

    first_name = f.first_name()
    last_name = f.last_name()
    emp_number = str(f.random_number(6))
    # 3
    response = hrm.add_employee(emp_number, first_name, last_name)
    assert '/pim/viewPersonalDetails/empNumber' in response.url

    # 4.Optional step, to check that data posted correctly
    resp = hrm.get_employee_details(resp.url)
    # soup = bs4.BeautifulSoup(resp.content, 'html5lib')
    print(resp.html_data)
    actual_emp_id = resp.html_data.select_one('#personal_txtEmployeeId')['value']

    assert str(emp_number) == actual_emp_id