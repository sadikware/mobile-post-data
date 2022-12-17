mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here


# print(mobile_data.get('data')[0].get('name'))


for data in mobile_data.get('data'):
    # print(data.get('name'))
    name = data.get('name')
    price = data.get('price')
    # print(float(price.replace(' USD', '')))
    made = data.get('made')
    bdt = int(float(price.replace(' USD', ''))
              * mobile_data.get('exchnage_rate'))

    print(f"{name} is made in {made}. The price is {price} which is almost equal to {bdt} BDT")
