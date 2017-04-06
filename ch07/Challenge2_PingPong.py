# PingPong_Challenge.py
def convert_in2cm(inches):
    return inches * 2.54
def convert_lb2kg(pounds):
    return pounds / 2.2
def convert_cm2in(cm):
    return cm / 2.54
def convert_kg2lb(kg):
    return kg * 2.2
number_ping_pong = eval(input("Enter a number of Ping-Pong balls: "))

height_ping_pong_cm = 4 * number_ping_pong
height_ping_pong_kg = 2.7 * number_ping_pong / 1000

height_in = round(convert_cm2in(height_ping_pong_cm))
weight_lb = round(convert_kg2lb(height_ping_pong_kg))

feet = height_in // 12
inch = height_in % 12

print ("If you had", number_ping_pong, "Ping-Pong balls, they would measure")
print (feet,"feet",inch,"inches tall, and weigh",weight_lb,"pounds,")

