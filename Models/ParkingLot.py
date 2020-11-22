import heapq


class ParkingLot():
	def __init__(self):
		''' Contructor for parking lot '''

		self.slot_vehicle_map = {}
		self.age_vehicle_map = {}
		self.age_slot_map = {}
		self.available_slots = []

	def create_n_slots(self, number_of_slots):
		''' This method will create the parking slots '''

		for i in range(1,number_of_slots+1):
			heapq.heappush(self.available_slots, i)
		return "Created parking of {} slots".format(number_of_slots)

	def all_slots(self):
		''' This method to get all the available slots '''
		return self.available_slots

	def get_available_slot(self):
		''' This method to get the particular slot '''

		if self.available_slots:
			return heapq.heappop(self.available_slots)

	def issue_ticket(self, vehicle_number, driver_age):
		''' This method will allocate a slot to customer '''

		available_slot = self.get_available_slot()
		if not available_slot:
			return "No slot available for parking."
		if self.age_vehicle_map.get(driver_age):
			self.age_vehicle_map[driver_age].append(vehicle_number)
		else:
			self.age_vehicle_map[driver_age] = [vehicle_number]
		if self.age_slot_map.get(driver_age):
			self.age_slot_map[driver_age].append(available_slot)
		else:
			self.age_slot_map[driver_age] = [available_slot]
		self.slot_vehicle_map[available_slot] = {"vehicle_number": vehicle_number, "driver_age": driver_age}
		return "Car with vehicle registration number \"{0}\" has been parked at slot number {1}".format(vehicle_number,available_slot)

	def get_all_slot_numbers_for_given_age(self, age):
		''' This method will give all the available slot numbers for a given age '''

		if self.age_slot_map.get(age):
			return ",".join(str(slot_no) for slot_no in self.age_slot_map[age])
		return ""

	def get_slot_number_for_vehicle(self, vehicle_number):
		''' This method will give the slot number for given car registration number '''

		for slot, sub_dict in self.slot_vehicle_map.iteritems():
			if sub_dict["vehicle_number"] == vehicle_number: 
				return slot
		return ""

	def leave_parking_slot(self, slot_number):
		''' This method will empty the slot when customer leaves the parking and make the slot available for other customers '''

		if not self.slot_vehicle_map.get(slot_number):
			return "Sorry! Slot is not occupied by any car."
		vehicle_number = self.slot_vehicle_map[slot_number]["vehicle_number"]
		driver_age = self.slot_vehicle_map[slot_number]["driver_age"]
		del self.slot_vehicle_map[slot_number]
		self.age_vehicle_map[driver_age].remove(vehicle_number)
		self.age_slot_map[driver_age].remove(slot_number)
		heapq.heappush(self.available_slots, slot_number)
		return "Slot number {0} vacated, the car with vehicle registration number \"{1}\" left the space, the driver of the car was of age {2}".format(slot_number,vehicle_number,driver_age)

	def get_vehicle_number_for_age(self, age):
		''' This method will give the all vehicle number for given age of customer '''
		
		if self.age_vehicle_map.get(age):
			return ",".join(self.age_vehicle_map[age])
		return ""
