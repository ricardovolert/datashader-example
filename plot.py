import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
from datashader.colors import Greys9, Hot, colormap_select as cm 

def bg(img): return tf.set_background(img,"black")

df = pd.read_csv('pos.csv')

cvs = ds.Canvas(plot_width=pixels, plot_height=pixels)
agg = cvs.points(df, 'x_col', 'y_col')

img = bg(tf.interpolate(agg, cmap = cm(Greys9,0.2), how='log')) 
img2 = img.to_pil()
img2.save('output.png')
