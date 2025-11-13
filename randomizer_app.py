from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# health check
@app.route('/health', methods = ['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200


@app.route('/rand/num', methods = ['POST'])
def random_number():
    in_data = request.get_json()
    type = in_data.get_json('type')
    start = in_data.get_json('start')
    end = in_data.get_json('end')

    # no type, error
    if not type:
        return jsonify({'status': 'error',
                        'error_message': 'need a type (int or float) to return'})
    # no start, error
    if not start:
        return jsonify({'status': 'error',
                        'error_message': 'need a start value'})
    # no end, error
    if not end:
        return jsonify({'status': 'error',
                        'error_message': 'need an end value'})

    # create a random int or float as requested
    rand_num = 0
    if type == 'int':
        rand_num = random.randrange(start, end)
    elif type == 'float':
        rand_num = random.uniform(start, end)

    # success
    return jsonify({'status': 'success',
                    'return_value': rand_num})


@app.route('/rand/event', methods = ['POST'])
def random_event():
    in_data = request.get_json()
    events = in_data.get_json('events', [])

    # no events, error
    if not events:
        return jsonify({'status': 'error',
                        'error_message': 'need a list of events'})

    # success
    return jsonify({'status': 'success',
                    'return_value': random.choice(events)})


@app.route('/rand/weighted', methods = ['POST'])
def random_weighted_event():
    in_data = request.get_json()
    events = in_data.get_json('events', [])
    weights = in_data.get_json('weights', [])

    # no events, error
    if not events:
        return jsonify({'status': 'error',
                        'error_message': 'need a list of events'})
    # no weights, error
    if not weights:
        return jsonify({'status': 'error',
                        'error_message': 'need a list of weights for each event'})
    # check len weights and events
    if len(weights) != len(events):
        return jsonify({'status': 'error',
                        'error_message': 'need a weight for each event'})

    # success
    return jsonify({'status': 'success',
                    'return_value': random.choices(events, weights, k = 1)})