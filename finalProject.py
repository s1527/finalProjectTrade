# Class name must be Strategy
class Strategy():
    # option setting needed
    def __setitem__(self, key, value):
        self.options[key] = value

    # option setting needed
    def __getitem__(self, key):
        return self.options.get(key, '')

    def __init__(self):
        # strategy property needed
        self.subscribedBooks = {
            'Binance': {
                'pairs': ['BTC-USDT'],
            },
        }
        self.period = 10 * 60
        self.options = {}
        self.close_price_trace = np.array([])
        self.last_type = 'sell'
        self.order_book={}
        self.order_price = {'9500':False,'9300':False,'9100':False,'8900':False,'8700':False}

    # called every self.period
    def trade(self, information):
        exchange = list(information['candles'])[0]
        pair = list(information['candles'][exchange])[0]
        close_price = information['candles'][exchange][pair][0]['close']
        if(close_price<=9500 and close_price>=9300 and self.order_price['9500']==False):
            self.order_price['9500']=True
            return [
                {
                    'exchange': exchange,
                    'amount': 0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]

        elif(close_price<=9300 and close_price>=9100 and self.order_price['9300']==False):
            self.order_price['9300']=True
            return [
                {
                    'exchange': exchange,
                    'amount': 0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        elif(close_price<=9100 and close_price>=8900 and self.order_price['9100']==False):
            self.order_price['9100']=True
            return [
                {
                    'exchange': exchange,
                    'amount': 0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]

        elif(close_price<=8900 and close_price>=8700 and self.order_price['8900']==False):
            self.last_type = 'buy'
            self.order_price['8900']=True
            return [
                {
                    'exchange': exchange,
                    'amount': 0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]

        elif(close_price<=8700 and close_price>=8500 and self.order_price['8700']==False):
            self.order_price['8700']=True
            return [
                {
                    'exchange': exchange,
                    'amount': 0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]

        if(self.order_price['9500'] ==True and close_price>9700 and close_price<9900 ):
            self.order_price['9500']=False
            return [
                {
                    'exchange': exchange,
                    'amount': -0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        ##########################
        elif(self.order_price['9300'] ==True and close_price>9500 and close_price<9700 ):
            self.order_price['9300']=False
            return [
                {
                    'exchange': exchange,
                    'amount': -0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        elif(self.order_price['9100'] ==True and close_price>9300 and close_price<9500 ):
            self.order_price['9100']=False
            return [
                {
                    'exchange': exchange,
                    'amount': -0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        elif(self.order_price['8900'] ==True and close_price>9100 and close_price<9300 ):
            self.order_price['8900']=False
            return [
                {
                    'exchange': exchange,
                    'amount': -0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        elif(self.order_price['8700'] ==True and close_price>8900 and close_price<9100 ):
            self.order_price['8700']=False
            return [
                {
                    'exchange': exchange,
                    'amount': -0.2,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        return []