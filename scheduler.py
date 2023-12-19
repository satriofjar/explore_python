import sched
import time
import random


# we try to create scheduler to short data by score and showing the top 5
# This is used to reduce requests to the database and sord the data
data_students = [
    {'name': 'jojo',
    'score': 80}
]  

def rating():
    for i in range(5):
        data_students.append({
            'name': f'joni{random.randint(1, 100)}',
            'score': random.randint(0, 100)
        })

    new_data =  sorted(data_students, key=lambda x: x['score'], reverse=True)

    print(new_data[:5])



scheduler = sched.scheduler(time.time, time.sleep)

def repeat_task():
    scheduler.enter(3, 1, rating, ())
    scheduler.enter(3, 1, repeat_task, ())

if __name__ == '__main__':
    repeat_task()
    scheduler.run()
