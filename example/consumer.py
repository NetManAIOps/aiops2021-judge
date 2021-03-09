'''
Example for data consuming.

Before running this script, execute

    pip3 install kafka-python
'''
import json
import requests

from kafka import KafkaConsumer
import logging


AVAILABLE_TOPICS = set(['a-kpi', 'a-metric', 'a-trace', 'a-log'])
CONSUMER = KafkaConsumer('a-kpi', 'a-metric', 'a-trace', 'a-log',
                         bootstrap_servers=['10.3.2.41', '10.3.2.4', '10.3.2.36'],
                         auto_offset_reset='latest',
                         enable_auto_commit=False,
                         security_protocol='PLAINTEXT')


def submit(ctx):
    assert (isinstance(ctx, list))
    for tp in ctx:
        assert(isinstance(tp, list))
        assert(len(tp) == 2)
        assert(isinstance(tp[0], str))
        assert(isinstance(tp[1], str) or (tp[1] is None))
    data = {'content': json.dumps(ctx)}
    r = requests.post('http://10.3.2.25:5000/standings/submit/', data=json.dumps(data))
    return r.text


def main():
    '''Consume data and react'''
    assert AVAILABLE_TOPICS <= CONSUMER.topics(), 'Please contact admin'
    print('test consumer')
    i = 0
    for message in CONSUMER:
        i += 1
        data = json.loads(message.value.decode('utf8'))
        timestamp = data['timestamp']
        print(i, message.topic, timestamp)
        if 'log' in message.topic:
            print(data['value'])


if __name__ == '__main__':
    '''
        test part
    '''
    r = submit([["docker_003","container_cpu_used"]])
    print(r)

    '''
        start to consume kafka
    '''
    main()
