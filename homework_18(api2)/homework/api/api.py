from utils.utils import post_api_request

URL_API = 'https://demowebshop.tricentis.com/'

def add_product_to_cart(product_id, quantity):
    result = post_api_request(
        url=URL_API + f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnterQuantity': {quantity}}
    )
    return result

def add_product_with_cookies(product_id, quantity, cookies):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'Nop.customer={cookies}'
    }

    result = post_api_request(
        url=URL_API + f'addproducttocart/details/{product_id}/1',
        data={f'addtocart_{product_id}.EnterQuantity': {quantity}},
        headers=headers
    )

    return result

def get_cookies(result):
    cookies = result.cookies.get('Nop.customer')
    return cookies