from tkinter import *
root = Tk()
root.geometry('600x600')
root.title('Made by Ankush Mallick')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)



text = Text(root, yscrollcommand=scrollbar.set)
text.insert(END, '''In brief, the mummification process may be summarized as follows: extract, sterilize, dehydrate, perfume, seal, tag, and stock. All were done ceremoniously and with due respect to the dead body. The viscera were extracted through an incision about 10 inches long, usually made in the left side of the abdomen. Through this incision, all the “floating” contents of the abdominal cavity, namely, the stomach, the liver, the spleen, and the intestines, were removed but the kidneys were left in place. The diaphragm was then cut and the thoracic contents removed through the abdominal incision. The heart, which was considered the center of emotions and the seat of conscience, was left in place. The ancient Egyptians seem to have attached no importance to the brain, which was removed through the ethmoid bone. Following these extractions began the slow process of sterilization and dehydration of the body, accomplished by osmosis with dry natron. Resterilization of the cavities, perfuming, closing the incision, and wrapping the body with linen and with beeswax completed the process. Molten resin was used to seal the body and its wrappings, providing a barrier against insects and anaerobes.''')


text.pack(fill=BOTH, side='right')
scrollbar.config(command=text.yview)

root.mainloop()
