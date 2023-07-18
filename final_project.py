from psychopy import visual, core, event
win = visual.Window([600,600])
message = visual.TextStim(win, text='one')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'two'  # Change properties of existing stim
win.flip()
core.wait(2.0)
message.text = '13'  # Change properties of existing stim
win.flip()
core.wait(2.0)
message.text = 'seventeen'  # Change properties of existing stim
win.flip()
core.wait(2.0)
message.text = '6'  # Change properties of existing stim
win.flip()
core.wait(2.0)
message.text = '37'  # Change properties of existing stim
win.flip()
core.wait(2.0)
message.text = 'fifty'  # Change properties of existing stim
win.flip()
core.wait(2.0)
