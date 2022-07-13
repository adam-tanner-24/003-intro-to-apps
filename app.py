######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
shows=['Noblesville IN 6-5-22', 'Noblesville IN 6-4-22', 'Noblesville IN 6-3-22', 'Charleston SC 6-1-22']
phishnet_rating=[3.86, 4.1, 3.791, 3.72]
songs_in_setlist=[19, 17, 18, 24]
color1='darkred'
color2='yellow'
mytitle='Phish Show Rating & Songs in Setlist (Prev 4 Shows)'

label1='Rating'
label2='Setlist'

########### Set up the chart

def make_that_cool_barchart(shows, phishnet_rating, songs_in_setlist, color1, color2, mytitle):
    rating = go.Bar(
        x=shows,
        y=phishnet_rating,
        name=label1,
        marker={'color':color1}
    )
    setlist = go.Bar(
        x=shows,
        y=songs_in_setlist,
        name=label2,
        marker={'color':color2}
    )

    phish_data = [rating, setlist]
    phish_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    phish_fig = go.Figure(data=phish_data, layout=phish_layout)
    return phish_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(shows, phishnet_rating, songs_in_setlist, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')
