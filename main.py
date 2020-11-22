import sys
from Utils.utils import is_valid_vehicle_number
from Models.ParkingLot import ParkingLot


def main():
	try:
		parking_lot = ParkingLot()
		input_file = sys.argv[1]
		with open(input_file,'r') as file:
			lines = file.readlines()
			for command in lines:
				split_command = command.rstrip('\n').split(' ')
				if split_command[0] == "Create_parking_lot":
					if int(split_command[1]) <= 0:
						print("Please provide a valid number of slots")
						return
					print(parking_lot.create_n_slots(int(split_command[1])))
				elif split_command[0] == "Park":
					if is_valid_vehicle_number(split_command[1]) and split_command[2] == "driver_age":
						print(parking_lot.issue_ticket(split_command[1], split_command[3]))
					else:
						print("Not a valid command!")
				elif split_command[0] == "Slot_numbers_for_driver_of_age":
					print(parking_lot.get_all_slot_numbers_for_given_age(split_command[1]))
				elif split_command[0] == "Slot_number_for_car_with_number":
					print(parking_lot.get_slot_number_for_vehicle(split_command[1]))
				elif split_command[0] == "Leave":
					print(parking_lot.leave_parking_slot(int(split_command[1])))
				elif split_command[0] == "Vehicle_registration_number_for_driver_of_age":
					print(parking_lot.get_vehicle_number_for_age(split_command[1]))
				else:
					print("Not a valid command!")
	except Exception as e:
		print(str(e))


if __name__ == '__main__':
	main()