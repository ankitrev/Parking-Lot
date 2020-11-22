import unittest
from Models.ParkingLot import ParkingLot

class ParkingLotUnitTesting(unittest.TestCase):
	''' Unit test to test each of the individual methods '''
	
	def test_create_parking_slot(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		self.assertEqual(len(parking_lot.all_slots()), 10)

	def test_issue_ticket(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		self.assertNotEqual("No slot available for parking.",parking_lot.issue_ticket("UP-32-MK-5474","26"))

	def test_parking_slot_full(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(2)
		res_str = parking_lot.issue_ticket("UP-32-MK-5474","26")
		res_str = parking_lot.issue_ticket("UP-78-LI-2342","27") 
		self.assertEqual("No slot available for parking.", parking_lot.issue_ticket("UP-35-LO-2390","28"))

	def test_leave_parking_slot(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		res_str = parking_lot.issue_ticket("UP-32-MK-5474","26")
		self.assertNotEqual("Sorry! Slot is not occupied by any car.",parking_lot.leave_parking_slot(1))

	def test_get_all_slot_numbers_for_given_age(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		res_str = parking_lot.issue_ticket("UP-32-MK-5474","26")
		res_str = parking_lot.issue_ticket("UP-78-LI-2342","27") 
		self.assertNotEqual("",parking_lot.get_all_slot_numbers_for_given_age("26"))

	def test_get_slot_number_for_vehicle(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		res_str = parking_lot.issue_ticket("UP-32-MK-5474","26")
		res_str = parking_lot.issue_ticket("UP-78-LI-2342","27")
		self.assertEqual(2,parking_lot.get_slot_number_for_vehicle("UP-78-LI-2342"))

	def test_get_vehicle_number_for_age(self):
		parking_lot = ParkingLot()
		res_str = parking_lot.create_n_slots(10)
		res_str = parking_lot.issue_ticket("UP-32-MK-5474","26")
		res_str = parking_lot.issue_ticket("UP-78-LI-2342","27")
		self.assertEqual("UP-32-MK-5474",parking_lot.get_vehicle_number_for_age("26"))
		self.assertEqual("UP-78-LI-2342",parking_lot.get_vehicle_number_for_age("27"))

if __name__ == '__main__':
	unittest.main()
