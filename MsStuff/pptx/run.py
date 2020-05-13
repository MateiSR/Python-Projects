import os
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

title_slide_layout = prs.slide_layouts[0]
slide_1 = prs.slides.add_slide(title_slide_layout)

title_1 = slide_1.shapes[0]
title_1.text_frame.text = 'Pong'

content_1 = slide_1.shapes[1]
content_1.text_frame.text = 'made using python-pptx'

content_slide_layout = prs.slide_layouts[1]
slide_2 = prs.slides.add_slide(content_slide_layout)

title_2 = slide_2.shapes[0]
title_2.text_frame.text = 'What is Pong?'

content_2 = slide_2.shapes[1]
content_2.text_frame.text = 'Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth. The goal is for each player to reach eleven points before the opponent; points are earned when one fails to return the ball to the other.'

picture_slide_layout = prs.slide_layouts[8]
slide_3 = prs.slides.add_slide(picture_slide_layout)

picture_3 = slide_3.placeholders[1]
picture_3.insert_picture('Pong.png')

title_3 = slide_3.shapes[0]
title_3.text_frame.text = 'Picture of the Pong game'

slide_4 = prs.slides.add_slide(content_slide_layout)

title_4 = slide_4.shapes[0]
title_4.text_frame.text = 'Development process'

content_4 = slide_4.shapes[1]
content_4.text_frame.text = 'Pong was the first game developed by Atari. After producing Computer Space, Bushnell decided to form a company to produce more games by licensing ideas to other companies. In August 1972, Bushnell and Alcorn installed the Pong prototype at a local bar, Andy Capp\'s Tavern. After the success of Pong, in 1974, Atari engineer Harold Lee proposed a home version of Pong that would connect to a television: Home Pong.'

slide_5 = prs.slides.add_slide(prs.slide_layouts[5])

title_5 = slide_5.shapes[0]
title_5.text_frame.text = 'Thanks for watching!'

#
prs.save('pong.pptx')
os.startfile('pong.pptx')