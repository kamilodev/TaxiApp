class Prices():
	def __init__(self):
		self.stop = 0.2
		self.move = 0.5
		
	def ticket(self, stop_time, move_time):
		bill_stop = round(stop_time * self.stop, 2)
		bill_move = round(move_time * self.move, 2)
		total_bill = round(bill_stop + bill_move, 2)
		
		return bill_stop, bill_move, total_bill