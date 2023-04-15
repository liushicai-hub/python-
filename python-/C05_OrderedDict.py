from collections import OrderedDict

x = OrderedDict(
    [
        ('nbr-id', '167902977'),
        ('address', '10.1.1.2'),
        ('dr', '0'),
        ('bdr', '0'),
        ('dr-ip', '0.0.0.0'),
        ('bdr-ip', '0.0.0.0'),
        ('event-count', '6'),
        ('retrans-count', '0'),
        ('state', 'ospf-nbr-full'),
        ('dead-timer', '34')
    ]
)
# print(x['nbr-id'])
# print(type(x))
for i in x:
    print(x[i])
