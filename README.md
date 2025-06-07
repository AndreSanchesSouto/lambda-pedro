# Função Lambda Simples

## Descrição
Função "Hello World" que retorna uma mensagem personalizada.

## Entrada
Exemplo:
```json
{"name": "Seu Nome"}
```

## Saída
Exemplo:
```json
{
  "message": "Olá, Seu Nome! Sua função Lambda funciona!",
  "input_event": {"name": "Seu Nome"}
}
```

## Como Usar
1. Acesse o [Console AWS Lambda](https://console.aws.amazon.com/lambda)
2. Crie função Python 3.12
3. Cole o código:
```python
def lambda_handler(event, context):
    name = event.get('name', 'visitante')
    return {
        'message': f'Olá, {name}! Sua função Lambda funciona!',
        'input_event': event
    }
```

## Teste
Use este evento de teste:
```json
{"curso": "Arquitetura Cloud"}
```
