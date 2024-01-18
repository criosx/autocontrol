import json
import requests
import server
import socket
import time

port = 5003


def print_queue():
    print('\n')
    print('Current Queue')
    url = 'http://localhost:' + str(port) + '/queue_inspect'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({})
    response = requests.get(url, headers=headers, data=data)

    print('Waiting for 2 seconds.')

    time.sleep(2)


def submit_task(task):
    print('\n')
    print('Submitting Task')
    url = 'http://localhost:' + str(port) + '/put'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(task)
    response = requests.post(url, headers=headers, data=data)

    print('Waiting for 2 seconds.')
    time.sleep(2)


def integration_test():
    print('Starting integration test')

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("The IP address of your machine is:", IPAddr)
    print('\n')

    # ------------------ Starting Flask Server----------------------------------

    server.start_server(host='localhost', port=port)

    time.sleep(2)
    print('Waiting for 2 seconds.')
    time.sleep(2)

    # ------------------ Printing Queue ----------------------------------

    print_queue()

    # ------------------ Submitting Task ----------------------------------

    task = {
        'task': 'test_task',
        'sample_number': 1,
        'channel': 0,
        'md':  {
            'favorite_color': 'red',
            'favorite_actor': 'Mickey Mouse'
        },
        'task_type': 'init',
        'device': 'qcmd'
    }
    submit_task(task)

    # ------------------ Printing Queue ----------------------------------

    print_queue()

    # ------------------ Stopping Flask Server ----------------------------------

    print('\n')
    print('Stopping Flask')
    url = 'http://localhost:' + str(port) + '/shutdown'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({})
    response = requests.post(url, headers=headers, data=data)

    time.sleep(2)

    print('Integration test done.')
    print('Program exit.')


if __name__ == '__main__':
    integration_test()
