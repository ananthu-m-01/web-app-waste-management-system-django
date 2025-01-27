from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    userType = models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pinCode = models.CharField(max_length=100)
    wardnumber = models.CharField(default=1,max_length=100)
    houseNumber = models.CharField(default=1,max_length=100)

class Materials(models.Model):
    materialName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    quantity = models.CharField(default=1,max_length=100)

class Area(models.Model):
    panchayath = models.CharField(max_length=100)
    wardNumber = models.CharField(max_length=100)

class Krishibhavan(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pinCode = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    logtitude = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)

class PickupVehicle(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=100)
    vehicleNumber = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    email = models.CharField(default=1,max_length=100)
    fuelType = models.CharField(max_length=100)

class WasteDetails(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    wasteType = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(default=1,max_length=100)


class PickupReports(models.Model):
    PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)
    WASTEDETAILS = models.ForeignKey(WasteDetails, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    wasteQuantity = models.CharField(max_length=100)

class Payment(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    paymentStatus = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    paymentType = models.CharField(max_length=100)
    amount = models.CharField(default=1,max_length=100)


class Notification(models.Model):
    notification = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)


class Complaint(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=1000)
    complaintDate = models.CharField(max_length=100)
    reply = models.CharField(max_length=1000)
    replyDate = models.CharField(max_length=100)
# PICKUPVEHICLE
class Feedback(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    # PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)

class Allocatedarea(models.Model):
    AREA = models.ForeignKey(Area, default=1, on_delete=models.CASCADE)
    PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)



class CollectionDate(models.Model):
    WASTEDETAILS = models.ForeignKey(WasteDetails, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    collectedWaste = models.CharField(default=1, max_length=100)
    status = models.CharField(max_length=100)
    PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)


class WasteEntry(models.Model):
    PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)
    COLLECTIONDATE = models.ForeignKey(CollectionDate, default=1, on_delete=models.CASCADE)

class Ownstock(models.Model):
    MATERIALS = models.ForeignKey(Materials, default=1, on_delete=models.CASCADE)
    KRISHIBHAVAN = models.ForeignKey(Krishibhavan, default=1, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Vegetable(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    vegetableName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    Amount = models.CharField(default=1,max_length=100)

class VegetableCollectionRequest(models.Model):
    VEGETABLE = models.ForeignKey(Vegetable, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    Quantity = models.CharField(default=1,max_length=100)
    Price = models.CharField(default=1,max_length=100)
    date = models.CharField(default=1,max_length=100)


class VegetableStock(models.Model):
    KRISHIBHAVAN = models.ForeignKey(Krishibhavan, default=1, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    Amount = models.CharField(default=1,max_length=10)
    VegetableName = models.CharField(default=1,max_length=10)

class VegetableOrder(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    VEGETABLESTOCK = models.ForeignKey(VegetableStock, default=1, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paymentStatus = models.CharField(max_length=100)


class VegetableOrderSub(models.Model):
    VEGETABLEORDER = models.ForeignKey(VegetableOrder, default=1, on_delete=models.CASCADE)
    VEGETABLESTOCK = models.ForeignKey(VegetableStock, default=1, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=100)

class VegetableCart(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    VEGETABLESTOCK = models.ForeignKey(VegetableStock, default=1, on_delete=models.CASCADE)


class MaterialOrder(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    MATERIALS = models.ForeignKey(Materials, default=1, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paymentStatus = models.CharField(default=1,max_length=100)

class MaterialOrderSub(models.Model):
    MATERIALORDER = models.ForeignKey(MaterialOrder, default=1, on_delete=models.CASCADE)
    MATERIALS = models.ForeignKey(Materials, default=1, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=100)

class MaterialsCart(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    MATERIALS = models.ForeignKey(Materials, default=1, on_delete=models.CASCADE)

class PickupPayment(models.Model):
    PICKUPVEHICLE = models.ForeignKey(PickupVehicle, default=1, on_delete=models.CASCADE)
    paymentStatus = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount = models.CharField(default=1,max_length=100)
    COLLECTIONDATE = models.ForeignKey(CollectionDate, default=1, on_delete=models.CASCADE)

class supercoins(models.Model):

    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    coins=models.CharField(max_length=100)
