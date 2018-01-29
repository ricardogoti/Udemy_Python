from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/stock/')
def stock():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    def inc_dec(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    start = datetime.datetime.now() - datetime.timedelta(days=30)
    end   = datetime.datetime.now()

    df = data.DataReader(name = "GOOG", data_source = "yahoo", start = start, end = end)

    df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open+df.Close)/2
    df["Height"] = abs(df.Close-df.Open)

    hours_12 = 12 * 60 * 60 * 1000

    p = figure(x_axis_type ='datetime', width = 1000, height = 300, sizing_mode='scale_width')
    p.title.text = "Candlestick Chart for Google Stock for Last Month"
    p.title.text_font_size="24pt"
    p.title.align="center"
    p.grid.grid_line_alpha = 0.5


    p.segment(df.index, df.High, df.index, df.Low, color= "black")

    p.rect(x=df.index[df.Status == "Increase"], y=df.Middle[df.Status == "Increase"], width=hours_12,
           height=df.Height[df.Status=="Increase"], fill_color="#90EE90", line_color="black")

    p.rect(x=df.index[df.Status == "Decrease"], y=df.Middle[df.Status == "Decrease"], width=hours_12,
           height=df.Height[df.Status=="Decrease"], fill_color="#F08080", line_color="black")

    #Se crea el html localmente y con show el sistema nos muestra el objeto
    #output_file('stock.html')
    #show(p)

    #Exportamos los archivos generados para la creacion de la grafica y lo alamacenamos en 4 variables
    script1, div1 = components(p)
    cdn_js  = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("stock.html",
    div1    = div1,
    scrip1  = script1,
    cdn_js  = cdn_js,
    cdn_css = cdn_css)

@app.route('/info/')
def ricardo():
    return render_template("ricardo.html")

if __name__ == "__main__":
    app.run(debug=True)
