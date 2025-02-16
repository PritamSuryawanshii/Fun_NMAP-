from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    scan_type = request.form.get('scan_type')


    if scan_type == "ping_scan":
        cmd = f"nmap -sn {target}"
    
    elif scan_type == "port_scan":
        cmd = f"nmap -p 1-1000 {target}"
    
    elif scan_type == "service_scan":
        cmd = f"nmap -sV {target}"
    
    elif scan_type == "os_scan":
        cmd = f"nmap -O {target}"
    
    elif scan_type == "quick_scan":
        cmd = f"nmap -T4 -F {target}"
        
    else:
        return "Invalid scan type selected!"

    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
    except Exception as e:
        result = f"Error executing Nmap: {e}"

    return render_template('result.html', target=target, scan_type=scan_type, result=result)

if __name__ == '__main__':
    app.run(debug=True)
