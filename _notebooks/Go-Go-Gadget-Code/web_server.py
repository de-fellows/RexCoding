# Author: Christina Kampel
from flask import Flask, render_template
import data_stats_graphs as dsg

app = Flask(__name__)

# Static Route:
# if someone requests the root route, execute the following (i.e. what the page shows when nothing or / is typed in the address bar after localhost:5000)

@app.route("/")

def index():

    # Generate PNG Graphs for the Data
    dsg.line_graph_temp(dsg.filename)
    dsg.line_graph_humi(dsg.filename)

    # Template Method:
    return render_template('index.html', t_avg_percent_diff=dsg.avg_percent_diff_temp(dsg.filename), h_avg_percent_diff=dsg.avg_percent_diff_humi(dsg.filename))    # Have the HTML code ready as a template and ask flask to read it back to the user
                                            # Templates separate the HTML from the logic and allow you to easily adjust content


if __name__ == "__main__":
    app.debug = True    # When we run the server, will run debug mode. Will automatically relaunch server when we change the code!
    app.run(host="0.0.0.0")     # Tells web server to listen on all network interfaces. Allows web server to be viewed by other devices on the same network.