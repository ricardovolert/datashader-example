import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
from datashader.colors import Greys9, Hot, colormap_select as cm 

pixels=800 # size of image
filename='pos.csv' # name of input file

def bg(img):
  return tf.set_background(img,"black")

df = pd.read_csv(filename)

cvs = ds.Canvas(plot_width=pixels, plot_height=pixels)
agg = cvs.points(df, 'x_col', 'y_col')

img = bg(tf.shade(agg, cmap = cm(Greys9,0.2), how='log'))
img2 = img.to_pil()
img2.save('output.png')
