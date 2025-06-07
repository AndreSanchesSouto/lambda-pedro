def lambda_handler(event, context):
    name = event.get('name', 'visitante')
    return {
        'message': f'Olá, {name}! Sua função Lambda funciona!',
        'input_event': event
    }
