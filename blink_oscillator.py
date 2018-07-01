from fcframe import FCFrame

class BlinkOscillator(object):
	def __init__(self, first_color, second_color, frames):
		self.first_color = first_color
		self.second_color = second_color
		self.frames = frames
		self.idx = 0

	def get_frames(self, requested_frames) -> object:
		output_frames = []
		for i in range(0, requested_frames):
			f = FCFrame()
            f.fill_solid