import json
import os
from datetime import datetime

class History:
	def __init__(self, total_time, stop_time, move_time, bill_stop, bill_move, bill_total):
		self.total_time = total_time
		self.stop_time = stop_time
		self.move_time = move_time
		self.bill_stop = bill_stop
		self.bill_move = bill_move
		self.bill_total = bill_total
		self.today = datetime.now().strftime("%d-%m-%Y")
		self.hour = datetime.now().strftime("%H:%M")
		self.id = id(self.hour)

	def to_json(self):
		data = {
			"id": self.id,
			"today": self.today,
			"hour": self.hour,
			"total_time": self.total_time,
			"total_stopped_time": self.stop_time,
			"total_movement_time": self.move_time,
			"total_bill_stop": self.bill_stop,
			"total_bill_move": self.bill_move,
			"total_bill_total": self.bill_total,
		}
		return json.dumps(data, indent=4)
	
	def save_history_to_file(self, json_data):
		if not os.path.isfile('history.json'):
			with open('history.json', 'w') as file:
				file.write('[')
		else:
			# Leer el contenido actual del archivo
			with open('history.json', 'r') as file:
				content = file.read().strip()
			
			# Verificar si el contenido termina con una coma
			if content.endswith('],'):
				# Eliminar la coma y el corchete final
				content = content[:-2]
			elif content.endswith(']'):
				# Eliminar el corchete final
				content = content[:-1]
			
			# Escribir el contenido actualizado
			with open('history.json', 'w') as file:
				file.write(content)
		
		# Agregar el objeto JSON al archivo
		with open('history.json', 'a') as file:
			if os.stat('history.json').st_size > 1:
				file.write(',')
			file.write(json_data)
		
		# Cerrar la lista de objetos JSON en el archivo
		with open('history.json', 'a') as file:
			file.write(']')