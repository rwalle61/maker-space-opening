from sense_hat import SenseHat
sense = SenseHat()

while True:
  t = sense.get_temperature()

  # Round the value to one decimal place
  t = round(t, 1)

  message = "Temperature: " + str(t)
  
  sense.show_message(message, scroll_speed=0.05)