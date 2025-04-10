import subprocess
import sys

def run_command(command):
    """Runs a shell command and prints output in real-time."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        print(line, end='')
    process.stdout.close()
    process.wait()
    if process.returncode != 0:
        print(f"Error: {process.stderr.read()}")
        sys.exit(process.returncode)

def install_prometheus():
    print("Adding Prometheus Helm repository...")
    run_command("helm repo add prometheus-community https://prometheus-community.github.io/helm-charts")
    run_command("helm repo update")
    print("Installing Prometheus...")
    run_command("helm install prometheus prometheus-community/prometheus")

def main():
    install_prometheus()
    print("\nInstallation complete! You can access Prometheus by running:\n")
    print("kubectl port-forward svc/prometheus-server 9090:80 &")
    print("Then open: http://localhost:9090")

if __name__ == "__main__":
    main()
