import requests

from conf.settings import STRIPE_AUTH


def get_payment_url(product, price):
    headers = {
        'Authorization': f'Bearer {STRIPE_AUTH}'
    }
    data = {
        'name': product
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/products', headers=headers, data=data)
    product_id = response.json()['id']
    price *= 100  # тк там в копейках
    data = {
        'unit_amount': price,
        'currency': 'rub',
        'recurring[interval]': 'month',
        'product': product_id
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/prices', headers=headers, data=data)
    price_id = response.json()['id']

    data = {
        'line_items[0][price]': price_id,
        'line_items[0][quantity]': 1,
        'mode': 'subscription',
        'success_url': 'https://example.com/success'
    }
    response = requests.request('POST', 'https://api.stripe.com/v1/checkout/sessions', headers=headers, data=data)
    return response.json()['url']

# if __name__ == '__main__':
#     print(get_url_payment('course', 1000))