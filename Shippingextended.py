weight = 84
premium_ground = 125.00
premium_ground_reminder = "(The price of premium ground shipping does not change with the weight of the package.)"
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif (weight > 2) and (weight <= 6):
  cost_ground = weight * 3.00 + 20
elif (weight > 6) and (weight <= 10):
  cost_ground = weight * 4.00 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

print('Ground Shipping: ${:.2f}'.format(cost_ground))
print("Premium Ground: ${:.2f}{}".format(premium_ground,premium_ground_reminder))

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif (weight > 2) and (weight <= 6):
  cost_drone = weight * 9.00
elif (weight > 6) and (weight <= 10):
  cost_drone = weight * 12.00
elif weight > 10:
  cost_drone = weight * 14.25

print('Drone Shipping: ${:.2f}'.format(cost_drone))
all_costs = (cost_ground, premium_ground, cost_ground)

if min(all_costs) == [0]:
  shipping_type = "Ground Shipping"
elif min(all_costs) == [1]:
  shipping_type = "Premium Ground"
else:
  shipping_type = "Drone Shipping"


print("Your lowest cost of shipping would be {} at ${:.2f}".format(shipping_type,min(all_costs)))
