from os import wait
import sys
import asyncio
from matplotlib.pyplot import xlabel

from numpy import positive
from test import extract_values_from_each_member
from utils_functions import quadrant_classifier_label, collect_member_data
from graph import check_matrix, check_matrix_template

# create an if statement where we input values based on the number of users voting

async def play():
    # print('\nFind out how to prioritise your objectives...')
    # await asyncio.sleep(4)
    # print('\nAre you ready?')
    # await asyncio.sleep(4)
    num_of_users = int(input('\nHow many members will be voting?: '))
    # await asyncio.sleep(2)
    name = input('\nEnter your matrix name: ')
    # await asyncio.sleep(2)
    # print('\nThank you.')
    # await asyncio.sleep(2)
    problem = input('\nNow enter your problem/objective/question you intend to solve: ')
    await asyncio.sleep(2)
    class_name = input('\nWhat would you like to name this preferred class and category?: ')
    # await asyncio.sleep(2)
    # print('\nNow we need to define the labels for the X and Y AXIS. This should be the metric you wish to measure this against.')
    # await asyncio.sleep(4)
    # print('\nI will give you an example.')
    # await asyncio.sleep(4)
    # print('\nI want to know what my colleagues think about a feature and how feasible it might be.')
    # await asyncio.sleep(4)
    # print('\nBetween 0 to 100, I want to know whether this feature is worth taking onboard.')
    # await asyncio.sleep(4)
    # print("\nI will make the X axis a metric of 'Time', and the Y axis a metric of 'Effort'.")
    # await asyncio.sleep(5)
    # print('\nNow, please enter your X axis label. This should be a label, not a number.')
    # await asyncio.sleep(2)
    x_label = input('\nX axis label: ')
    await asyncio.sleep(2)
    print('\nNow, please enter your Y axis label. This should also be a label, not a number.')
    await asyncio.sleep(2)
    y_label = input('\nY axis label: ')
    # await asyncio.sleep(2)
    # print('\nNow we need to measure if this is a positive or a negative metric.')
    # await asyncio.sleep(4)
    # print('\nMeaning, would the increase of this value be good/positive or bad/negative?')
    # await asyncio.sleep(4)
    x_polarity = None
    y_polarity = None
    while x_polarity not in ['positive', 'negative']:
        x_polarity = input(f'\nX axis - {x_label} (positive or negative): ')
    if x_polarity == 'positive':
        x_polarity = True
    if x_polarity == 'negative':
        x_polarity = False
    await asyncio.sleep(2)
    while y_polarity not in ['positive', 'negative']:
        y_polarity = input(f'\nY axis - {y_label} (positive or negative): ')
    if y_polarity == 'positive':
        y_polarity = True
    if y_polarity == 'negative':
        y_polarity = False
    await asyncio.sleep(2)
    print('\nNow we have all the data we need, we will display your matrix.')
    await asyncio.sleep(2)
    preferred_quadrant = quadrant_classifier_label(x_polarity, y_polarity)
    print(f'\nYour preferred quadrant is {preferred_quadrant}.')
    await asyncio.sleep(2)
    # template_generator = check_matrix_template(preferred_quadrant)
    # await asyncio.sleep(2)
    # print('Generating template...')
    # await asyncio.sleep(2)
    # template_generator(name=name, problem=problem, class_name=class_name, x_label=x_label, y_label=y_label, x_polarity=x_polarity, y_polarity=y_polarity)
    # await asyncio.sleep(2)
    print('\nNow we need to collect the values of your members.')
    await asyncio.sleep(2)
    print('\nPlease enter the X and Y values of all your members.')
    await asyncio.sleep(2)
    data = collect_member_data(num_of_users=num_of_users)
    x_values, y_values = extract_values_from_each_member(data)
    await asyncio.sleep(2)
    print('Generating template...')
    matrix = check_matrix(preferred_quadrant)
    matrix(num_of_users=num_of_users, name=name, problem=problem, class_name=class_name, x_label=x_label, y_label=y_label, x_polarity=x_polarity, y_polarity=y_polarity, x_values=x_values, y_values=y_values)
    await asyncio.sleep(2)
    print('Ta Da!')
    
    # await input_args()
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(input_args())
    # finally:
    #     loop.close()

if __name__ == '__main__':
    asyncio.run(play())
