import json

def lambda_handler(event, context):
    # Extracting information from the event
    http_method = event['httpMethod']
    query_parameters = event['queryStringParameters']

    # Responding based on the HTTP method
    if http_method == 'GET':
        name = query_parameters.get('name', 'World')
        message = f'Hello, {name}!'
    else:
        message = 'Unsupported HTTP method'

    # Constructing the response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': message}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    return response
